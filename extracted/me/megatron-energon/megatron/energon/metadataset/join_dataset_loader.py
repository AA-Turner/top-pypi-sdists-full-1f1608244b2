# Copyright (c) 2025, NVIDIA CORPORATION.
# SPDX-License-Identifier: BSD-3-Clause

import hashlib
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from megatron.energon.edataclass import edataclass
from megatron.energon.epathlib.epath import EPath
from megatron.energon.flavors import (
    BaseCoreDatasetFactory,
    BaseWebdatasetFactory,
    JoinedWebdatasetFactory,
    Sample,
)
from megatron.energon.flavors.webdataset.config import MAIN_FOLDER_NAME
from megatron.energon.flavors.webdataset.indexing import JoinIndexWriter
from megatron.energon.flavors.webdataset.metadata import WebdatasetMeta
from megatron.energon.metadataset.dataset_loader import DatasetLoader
from megatron.energon.metadataset.loader_interface import (
    DatasetBlendMode,
    DatasetLoaderInterface,
    LoadedDataset,
    LoadedDatasetList,
)
from megatron.energon.worker import WorkerConfig


def filter_samples_with_excludes(
    conn,
    db_alias: str,
    meta: "JoinedDatasetMetaInfo",
):
    """
    Filter the samples in the database with the given excludes.
    """
    filtered_name = f"{db_alias}_filtered"

    conn.execute(f"DROP VIEW IF EXISTS {filtered_name}")

    if not meta.excludes:
        # Nothing to exclude, just use the original table
        conn.execute(f"CREATE TEMP VIEW {filtered_name} AS SELECT * FROM {db_alias}.samples")
        return

    # Split the excludes into shard-level excludes and sample-level excludes
    excluded_shard_ids = []
    excluded_sample_keys = []
    for exclude in meta.excludes:
        if exclude in meta.shard_name_to_info_idx:
            excluded_shard_ids.append(meta.shard_name_to_info_idx[exclude])
        else:
            # Find the shard name for the sample key
            # Trivial split by .tar/
            if ".tar/" in exclude:
                tarname, sample_key = exclude.split(".tar/", 1)
                shard_idx = meta.shard_name_to_info_idx[tarname + ".tar"]
                excluded_sample_keys.append((shard_idx, sample_key))
            elif exclude.endswith(".tar"):
                # This is a shard and was probably already excluded outside this function
                pass
            else:
                raise ValueError(
                    f"Invalid exclusion: Cannot split exclude {exclude} into shard and sample key"
                )

    # Create a temporary table for the shard excludes
    # The key will be integers according to the tar_file_id column of the samples table
    conn.execute(f"DROP TABLE IF EXISTS temp_shard_excludes_{db_alias}")
    conn.execute(
        f"""
            CREATE TEMP TABLE temp_shard_excludes_{db_alias} (
                exclude_key INTEGER PRIMARY KEY
            )
        """
    )
    for shard_id in excluded_shard_ids:
        conn.execute(
            f"INSERT INTO temp_shard_excludes_{db_alias}(exclude_key) values (?)", (shard_id,)
        )

    # Create a temporary table for the sample excludes
    conn.execute(f"DROP TABLE IF EXISTS temp_sample_excludes_{db_alias}")
    conn.execute(
        f"""
            CREATE TEMP TABLE temp_sample_excludes_{db_alias} (
                shard_idx INTEGER,
                exclude_key TEXT,
                PRIMARY KEY (shard_idx, exclude_key)
            )
        """
    )
    conn.executemany(
        f"INSERT INTO temp_sample_excludes_{db_alias}(shard_idx, exclude_key) values (?, ?)",
        [(shard_idx, sample_key) for shard_idx, sample_key in excluded_sample_keys],
    )

    # Create view for filtered samples
    conn.execute(
        f"""
            CREATE TEMP VIEW {filtered_name} AS
            SELECT *
            FROM {db_alias}.samples s
            WHERE s.tar_file_id NOT IN (
                SELECT exclude_key
                FROM temp_shard_excludes_{db_alias}
            )
            AND NOT EXISTS (
                SELECT 1
                FROM temp_sample_excludes_{db_alias} e
                WHERE e.shard_idx = s.tar_file_id
                  AND e.exclude_key = s.sample_key
            )
        """
    )


def join_multiple_indices(
    meta_infos: List["JoinedDatasetMetaInfo"],
    output_join_index_path: EPath,
):
    """
    Joins the 'samples' table of one primary_db with multiple secondary_dbs
    by 'sample_key'. For each secondary DB, we select three columns:
      - tar_file_id
      - byte_offset
      - byte_size
    The result is streamed out row-by-row and written to join index.
    Note that the order of samples is determined by the shard_map of the primary DB.

    Args:
        meta_infos: List of meta infos for all datasets.
        output_join_index_path: Path to the output join index.
    """

    primary = meta_infos[0]
    secondaries = meta_infos[1:]

    assert primary.nonmatch == "error", (
        "Primary join dataset must have nonmatch set 'error' (default)"
    )

    import sqlite3

    # 1. Connect to the primary DB in 'main'
    conn = sqlite3.connect(f"file:{primary.db_path!s}?mode=ro", uri=True)

    # For safety, enable a read-only or big timeouts
    conn.execute("PRAGMA busy_timeout = 5000;")
    conn.execute("PRAGMA journal_mode = WAL;")

    # 2. Attach each secondary DB under a unique alias, e.g. db1, db2, ...
    secondary_aliases = []
    for i, sec_mi in enumerate(secondaries, start=1):
        alias = f"db{i}"
        secondary_aliases.append(alias)
        conn.execute(f"ATTACH DATABASE ? AS {alias}", (f"file:{sec_mi.db_path}?mode=ro",))

    # Filter the primary and each secondary DB for excluded samples by creating
    # a new VIEW for each
    for alias, mi in zip(["main"] + secondary_aliases, meta_infos):
        filter_samples_with_excludes(conn, alias, mi)

    # Check each primary and secondary DB for duplicate sample_key values
    for alias, mi in zip(["main"] + secondary_aliases, meta_infos):
        duplicates = conn.execute(
            f"""
            SELECT sample_key, COUNT(*) AS c
            FROM {alias}_filtered
            GROUP BY sample_key
            HAVING c > 1
            LIMIT 5
        """
        ).fetchall()
        if duplicates:
            raise ValueError(
                f"Can't join. Found duplicate sample keys in {mi.db_path}: {duplicates}"
            )

    # Create a temporary table to order the shards as in the current split config
    conn.execute("DROP TABLE IF EXISTS primary_order")
    conn.execute(
        """
        CREATE TEMP TABLE primary_order (
            tar_file_id INTEGER PRIMARY KEY,
            split_index INTEGER
        )
    """
    )
    conn.executemany(
        "INSERT INTO primary_order(tar_file_id, split_index) values (?, ?)",
        ((n, i) for i, n in enumerate(primary.split_part_oder)),
    )

    # Map from tar_file_id to shard idx in the split part
    tar_files_id_mapping = {}
    for alias, mi in zip(["main"] + secondary_aliases, meta_infos):
        tar_files_id_mapping[alias] = {
            tar_file_id: shard_idx for shard_idx, tar_file_id in enumerate(mi.split_part_oder)
        }

    # These are the columns we want to select in the main SQL query
    select_cols = [
        "main_filtered.tar_file_id AS main_tar_file_id",
        "main_filtered.byte_offset AS main_byte_offset",
        "main_filtered.byte_size AS main_byte_size",
    ]

    for i, alias in enumerate(secondary_aliases, start=1):
        select_cols.append(f"{alias}_filtered.tar_file_id AS tar_file_id_{i}")
        select_cols.append(f"{alias}_filtered.byte_offset AS byte_offset_{i}")
        select_cols.append(f"{alias}_filtered.byte_size AS byte_size_{i}")

    # Build the LEFT JOIN or INNER JOIN clauses
    join_clauses = ""
    for alias, mi in zip(secondary_aliases, secondaries):
        if mi.nonmatch == "skip":
            join_type = "INNER JOIN"
        else:
            join_type = "LEFT JOIN"

        join_clauses += f" {join_type} {alias}_filtered ON main_filtered.sample_key = {alias}_filtered.sample_key"

    # Construct the full SQL query
    # We select three columns for the primary and each secondary DB
    # Those are (tar_file_id, byte_offset, and byte_size)
    # We join the secondary DBs to the primary DB using a LEFT JOIN, i.e.
    # we keep all rows from the primary DB and add columns from the secondary DBs if available
    # Finally, we also join the temporary shard order table to order the shards as in the split config.
    # This join is done using an INNER JOIN, i.e. we only keep rows that have a matching shard index in the primary dataset,
    # so we'll not include shards that come from other split parts
    sql = f"""
        SELECT
            {", ".join(select_cols)}
        FROM main_filtered
        {join_clauses}
        INNER JOIN primary_order o
            ON main_tar_file_id = o.tar_file_id
        ORDER BY o.split_index
    """

    # 3. Execute the query; this returns a cursor we can iterate over row by row
    cursor = conn.execute(sql)

    all_db_aliases = ["main"] + secondary_aliases

    # 4. Write the results to a binary file join index file row by row
    with JoinIndexWriter(output_join_index_path) as join_index_writer:
        # Example: We'll just show how to iterate the rows and pseudo-write them
        num_rows = 0
        num_missing = [0] * len(meta_infos)
        for row in cursor:
            # 'row' is a tuple of columns in the order of select_cols

            join_tuples = []
            for i, (alias, meta_info) in enumerate(zip(all_db_aliases, meta_infos)):
                tar_file_id = row[3 * i]

                if tar_file_id is None:
                    # This column is missing in this secondary dataset
                    # How we handle this case depends on the nonmatch setting
                    if meta_info.nonmatch == "none":
                        # The user accepts missing samples, we'll just add a dummy entry
                        join_tuples.append((-1, -1, -1))
                        num_missing[i] += 1
                    elif meta_info.nonmatch == "skip":
                        # The user wants to skip rows with missing samples.
                        # Skipping rows is already handled by the INNER JOIN above, so
                        # this case should not happen.
                        raise AssertionError(
                            f"Join has encountered a missing sample: Sample key {row[0]} missing from "
                            f"{meta_info.db_path}, although nonmatch_skip is set"
                        )
                    else:
                        # The user wants to raise an error on missing samples
                        raise ValueError(
                            f"Join has encountered a missing sample: Sample key {row[0]} missing from "
                            f"{meta_info.db_path}, although neither nonmatch_none nor nonmatch_skip are set"
                        )
                else:
                    shard_idx = tar_files_id_mapping[alias][tar_file_id]
                    byte_offset = row[3 * i + 1]
                    byte_size = row[3 * i + 2]
                    join_tuples.append((shard_idx, byte_offset, byte_size))
            else:
                # Each row contains (shard_idx, byte_offset, byte_size) for each secondary key.
                join_index_writer.append(*join_tuples)
                num_rows += 1

    any_skip = any(mi.nonmatch == "skip" for mi in meta_infos)

    num_samples = conn.execute(
        "SELECT COUNT(*) FROM main_filtered INNER JOIN primary_order o ON main_filtered.tar_file_id = o.tar_file_id"
    ).fetchone()[0]

    if not any_skip:
        # If no dataset has skipping active, we can check that the number of rows matches the number of samples in the primary DB
        assert num_rows == num_samples, (
            f"Number of rows in join index ({num_rows}) does not match number of samples in primary DB ({num_samples})"
        )

        print(f"Joined all {num_rows} samples")
    else:
        print(
            f"Joined {num_rows}/{num_samples} samples, skipped {num_samples - num_rows} samples due to join"
        )

    if any(num_missing):
        print(f"Non-matching samples filled with None for each dataset: {num_missing}")

    conn.close()


@edataclass
class JoinedDatasetInfo:
    """Internal for passing the joined datasets."""

    dataset: DatasetLoader

    nonmatch: Literal["skip", "none", "error"]


@edataclass
class JoinedDatasetMetaInfo:
    """Internal for passing the joined datasets."""

    db_path: EPath
    uuid: str
    excludes: List[str]
    shard_name_to_info_idx: Dict[str, int]
    split_part_oder: List[int]
    nonmatch: Literal["skip", "none", "error"]


@edataclass
class JoinDatasetLoader(DatasetLoaderInterface):
    """Loads a joined dataset from a path."""

    datasets: Union[List[JoinedDatasetInfo], Dict[str, JoinedDatasetInfo]]
    joiner: Union[Type[Sample], Callable[..., Sample]]
    cache_path: Optional[EPath] = None

    split_part: Optional[str] = None
    split_config: Optional[str] = None
    subflavors: Optional[Dict[str, Any]] = None
    shuffle_over_epochs_multiplier: Optional[int] = 1

    def _get_joined_meta(self, split_part: str) -> Tuple[EPath, List[JoinedDatasetMetaInfo]]:
        """
        Collect the metadata for the joined dataset.

        Returns:
            The hashfile path, and a list of the meta infos.
        """
        # Get list of joinable datasets
        datasets = self.datasets
        if isinstance(datasets, dict):
            datasets = list(datasets.values())

        meta_infos: List[JoinedDatasetMetaInfo] = []

        for dataset in datasets:
            print(f" - {dataset}")

            uuid_path = EPath(dataset.dataset.path) / MAIN_FOLDER_NAME / "index.uuid"
            try:
                uuid = uuid_path.read_text()
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Missing uuid file in {uuid_path}. You need to prepare the dataset "
                    "(with a recent version of energon). If you have already prepared the "
                    "dataset, it should be sufficient to run prepare with --tar-index-only."
                )
            db_path = EPath(dataset.dataset.path) / MAIN_FOLDER_NAME / "index.sqlite"

            # Precedence for split_part is:
            # 1. Join dataset split part (overrides individual dataset split parts)
            # 2. Individual dataset split part
            # 3. If none of the above is set, use the split part of the surrounding meta dataset
            cur_split_part = dataset.dataset.split_part or self.split_part or split_part
            assert cur_split_part is not None, "Missing split part"

            wds_meta = WebdatasetMeta.from_config(
                path=EPath(dataset.dataset.path),
                split_part=cur_split_part,
                split_config=dataset.dataset.split_config,
            )

            shard_name_to_info_idx = {name: i for i, name in enumerate(wds_meta.info_shard_files)}

            # Given wds_meta.split_part_files, translate their order to info idx IDs
            split_part_oder = [shard_name_to_info_idx[name] for name in wds_meta.split_part_files]

            meta_infos.append(
                JoinedDatasetMetaInfo(
                    db_path=db_path,
                    uuid=uuid,
                    excludes=list(wds_meta.sample_excludes),
                    shard_name_to_info_idx=shard_name_to_info_idx,
                    split_part_oder=split_part_oder,
                    nonmatch=dataset.nonmatch,
                )
            )

        # Combine the hashes into a single hash by xor
        hash = hashlib.sha256()
        for meta_info in meta_infos:
            hash.update(b"\0uuid=")
            hash.update(meta_info.uuid.encode())
            hash.update(b"\0excludes=")
            for exclude in meta_info.excludes:
                hash.update(exclude.encode())
                hash.update(b"\0")
            hash.update(f"\0nonmatch={meta_info.nonmatch}\0".encode())
        assert self.cache_path is not None
        return self.cache_path / f"join_index_{hash.hexdigest()}.bin", meta_infos

    def post_initialize(self, mds_path: Optional[EPath] = None):
        assert mds_path is not None
        self.cache_path = mds_path.parent / f"{mds_path.name}.cache"

    def prepare(self, split_part: Optional[str] = None) -> Sequence[EPath]:
        assert self.cache_path is not None
        assert split_part is not None
        join_index_path, meta_infos = self._get_joined_meta(split_part)
        if join_index_path.is_file():
            print(f"Joined dataset already prepared at {join_index_path} and up-to-date")
            return (join_index_path,)

        print(f"Preparing joined dataset in {join_index_path}")
        join_index_path.parent.mkdir(parents=True, exist_ok=True)
        join_multiple_indices(
            meta_infos=meta_infos,
            output_join_index_path=join_index_path,
        )
        return (join_index_path,)

    def get_dataset(
        self,
        *,
        training: bool,
        split_part: Optional[str] = None,
        worker_config: WorkerConfig,
        subflavors: Optional[Dict[str, Any]] = None,
        shuffle_over_epochs: Optional[int] = 1,
        split_config: Optional[str] = None,
        **kwargs,
    ) -> BaseCoreDatasetFactory:
        """
        Args:
            training: If true, apply training randomization.
            split_part: Default split part to use.
            worker_config: Worker configuration.
            shuffle_buffer_size: Size of the sample shuffle buffer (before task encoding).
            subflavors: Subflavors to use, might be overridden by inner datasets.
            shuffle_over_epochs: Shuffle the dataset over this many epochs.
            **kwargs: Additional arguments to the dataset constructor.

        Returns:
            The loaded dataset
        """
        if self.split_config is not None:
            split_config = self.split_config
        if self.split_part is not None:
            split_part = self.split_part
        if split_part is None:
            raise ValueError("Missing split part")
        if self.subflavors is not None:
            subflavors = {**self.subflavors, **(subflavors or {})}
        join_index_path, _ = self._get_joined_meta(split_part)

        if isinstance(self.datasets, list):
            inner_datasets = [
                dataset.dataset.get_dataset(
                    training=training,
                    split_part=split_part,
                    worker_config=worker_config,
                    subflavors=subflavors,
                    shuffle_over_epochs=shuffle_over_epochs,
                    split_config=split_config,
                    **kwargs,
                )
                for dataset in self.datasets
            ]
            assert all(isinstance(d, BaseWebdatasetFactory) for d in inner_datasets), (
                "Can only merge webdatasets efficiently"
            )
        elif isinstance(self.datasets, dict):
            inner_datasets = {
                key: dataset.dataset.get_dataset(
                    training=training,
                    split_part=split_part,
                    worker_config=worker_config,
                    subflavors=subflavors,
                    shuffle_over_epochs=shuffle_over_epochs,
                    split_config=split_config,
                    **kwargs,
                )
                for key, dataset in self.datasets.items()
            }
            assert all(isinstance(d, BaseWebdatasetFactory) for d in inner_datasets.values()), (
                "Can only merge webdatasets efficiently"
            )
        else:
            raise ValueError("Invalid join type")
        # Remove decoder from kwargs, it is already handled by the inner datasets
        kwargs.pop("decoder", None)
        return JoinedWebdatasetFactory(
            inner_datasets=inner_datasets,
            training=training,
            worker_config=worker_config,
            shuffle_over_epochs=shuffle_over_epochs,
            join_index=join_index_path,
            joiner=self.joiner,
            **kwargs,
        )

    def get_datasets(
        self,
        *,
        training: bool,
        split_part: Union[Literal["train", "val", "test"], str],
        worker_config: WorkerConfig,
        subflavors: Optional[Dict[str, Any]] = None,
        shuffle_over_epochs_multiplier: Optional[int] = 1,
        **kwargs,
    ) -> LoadedDatasetList:
        return LoadedDatasetList(
            blend_mode=DatasetBlendMode.NONE,
            datasets=[
                LoadedDataset(
                    dataset=self.get_dataset(
                        training=training,
                        split_part=split_part,
                        worker_config=worker_config,
                        subflavors=subflavors,
                        shuffle_over_epochs=shuffle_over_epochs_multiplier,
                        **kwargs,
                    ),
                    weight=None,
                )
            ],
        )

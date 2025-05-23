import asyncio
import os
from typing import AsyncGenerator, Callable, List, NamedTuple, Optional, Union

import aiofiles
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

import supervisely.volume.nrrd_encoder as nrrd_encoder
from supervisely import logger, volume
from supervisely._utils import batched, generate_free_name
from supervisely.api.module_api import ApiField, RemoveableBulkModuleApi
from supervisely.api.volume.volume_annotation_api import VolumeAnnotationAPI
from supervisely.api.volume.volume_figure_api import VolumeFigureApi
from supervisely.api.volume.volume_object_api import VolumeObjectApi

# from supervisely.api.volume.video_frame_api import VolumeFrameAPI
from supervisely.api.volume.volume_tag_api import VolumeTagApi
from supervisely.imaging.image import read_bytes
from supervisely.io.fs import (
    ensure_base_path,
    get_bytes_hash,
    get_file_ext,
    get_file_hash_async,
    get_file_name,
    get_file_name_with_ext,
)
from supervisely.task.progress import Progress, tqdm_sly
from supervisely.volume.volume import inspect_dicom_series, inspect_nrrd_series
from supervisely.volume_annotation.plane import Plane

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class VolumeInfo(NamedTuple):
    """
    Object with :class:`Volume<supervisely.volume.volume>` parameters from Supervisely.

    :Example:

     .. code-block:: python

        VolumeInfo(
            id=19581134,
            name='CTChest.nrrd',
            link=None,
            hash='+0K2oFHpqA5dwRKQlhCiiE2qwLNP76Xk0kvhXEh52cs=',
            mime=None,
            ext=None,
            sizeb=46073411,
            created_at='2023-03-29T12:30:37.078Z',
            updated_at='2023-03-29T12:30:37.078Z',
            meta={
                'ACS': 'RAS',
                'intensity': {'max': 3071, 'min': -3024},
                'windowWidth': 6095,
                'rescaleSlope': 1,
                'windowCenter': 23.5,
                'channelsCount': 1,
                'dimensionsIJK': {'x': 512, 'y': 512, 'z': 139}
                'IJK2WorldMatrix': [0.7617189884185793, 0, 0, -194.238403081894, 0, 0.7617189884185793, 0, -217.5384061336518, 0, 0, 2.5, -347.7500000000001, 0, 0, 0, 1],
                'rescaleIntercept': 0
            },
            path_original='/h5af-public/images/original/M/e/7R/vsytec8zX0p.nrrd',
            full_storage_url='https://app.supervisely.com/h5un-public/images/original/M/e/7R/zX0p.nrrd',
            tags=[],
            team_id=435,
            workspace_id=685,
            project_id=18949,
            dataset_id=61803,
            file_meta={
                    'mime': 'image/nrrd',
                    'size': 46073411,
                    'type': 'int32',
                    'extra': {'stride': [1, 512, 262144],
                    'comments': []
                }
                'sizes': [512, 512, 139]
                'space': 'right-anterior-superior'
                'endian': 'little'
                'encoding': 'gzip'
                'dimension': 3
                'space origin': [-194.238403081894, -217.5384061336518, -347.7500000000001]
                'space dimension': 3
                'space directions': [[0.7617189884185793, 0, 0], [0, 0.7617189884185793, 0], [0, 0, 2.5]]
            }
            figures_count=None,
            objects_count=None,
            processing_path='1/1560071'
        )
    """

    #: :class:`int`: Volume ID in Supervisely.
    id: int

    #: :class:`str`: Volume filename.
    name: str

    #: :class:`str`: Link to volume.
    link: str

    #: :class:`str`: Volume hash obtained by base64(sha256(file_content)).
    #: Use hash for files that are expected to be stored at Supervisely or your deployed agent.
    hash: str

    #: :class:`str`: MIME type of the volume.
    mime: str

    #: :class:`str`: File extension of the volume.
    ext: str

    #: :class:`int`: Size of the volume in bytes.
    sizeb: int

    #: :class:`str`: Volume creation time. e.g. "2019-02-22T14:59:53.381Z".
    created_at: str

    #: :class:`str`: Time of last volume update. e.g. "2019-02-22T14:59:53.381Z".
    updated_at: str

    #: :class:`dict`: A dictionary containing metadata associated with the volume.
    meta: dict

    #: :class:`str`: Original path of the volume.
    path_original: str

    #: :class:`str`: Full storage URL of the volume.
    full_storage_url: str

    #: :class:`list`: Volume :class:`VolumeTag<supervisely.volume_annotation.volume_tag.VolumeTag>` list.
    #: e.g. "[{'entityId': 19581134, 'tagId': 385328, 'id': 12259702, 'value': 'some info}]"
    tags: list

    #: :class:`int`: :class:`TeamApi<supervisely.api.team_api.TeamApi>` ID in Supervisely.
    team_id: int

    #: :class:`int`: :class:`WorkspaceApi<supervisely.api.workspace_api.WorkspaceApi>` ID in Supervisely.
    workspace_id: int

    #: :class:`int`: :class:`Project<supervisely.project.project.Project>` ID in Supervisely.
    project_id: int

    #: :class:`int`: :class:`Dataset<supervisely.project.project.Dataset>` ID in Supervisely.
    dataset_id: int

    #: :class:`dict`: A dictionary containing metadata about the volume file.
    file_meta: dict

    #: :class:`int`: Number of figures in the volume.
    figures_count: int

    #: :class:`int`: Number of objects in the volume.
    objects_count: int

    #: :class:`str`: Path to the volume file on the server.
    processing_path: str


class VolumeApi(RemoveableBulkModuleApi):
    """
    API for working with :class:`Volume<supervisely.volume.volume>`. :class:`VolumeApi<VolumeApi>` object is immutable.

    :param api: API connection to the server.
    :type api: Api
    :Usage example:

     .. code-block:: python

        import os
        from dotenv import load_dotenv

        import supervisely as sly

        # Load secrets and create API object from .env file (recommended)
        # Learn more here: https://developer.supervisely.com/getting-started/basics-of-authentication
        if sly.is_development():
            load_dotenv(os.path.expanduser("~/supervisely.env"))
        api = sly.Api.from_env()

        # Pass values into the API constructor (optional, not recommended)
        # api = sly.Api(server_address="https://app.supervisely.com", token="4r47N...xaTatb")

        volume_id = 19581134
        volume_info = api.volume.get_info_by_id(volume_id) # api usage example
    """

    def __init__(self, api):
        """
        :param api: Api class object
        """
        super().__init__(api)
        self.annotation = VolumeAnnotationAPI(api)
        self.object = VolumeObjectApi(api)
        # self.frame = VideoFrameAPI(api)
        self.figure = VolumeFigureApi(api)
        self.tag = VolumeTagApi(api)

    @staticmethod
    def info_sequence():
        """
        Get list of all :class:`VolumeInfo<VolumeInfo>` field names.

        :return: List of :class:`VolumeInfo<VolumeInfo>` field names.`
        :rtype: :class:`list`
        """

        return [
            ApiField.ID,
            ApiField.NAME,
            ApiField.LINK,
            ApiField.HASH,
            ApiField.MIME,
            ApiField.EXT,
            ApiField.SIZEB3,
            ApiField.CREATED_AT,
            ApiField.UPDATED_AT,
            ApiField.META,
            ApiField.PATH_ORIGINAL,
            ApiField.FULL_STORAGE_URL,
            ApiField.TAGS,
            ApiField.TEAM_ID,
            ApiField.WORKSPACE_ID,
            ApiField.PROJECT_ID,
            ApiField.DATASET_ID,
            ApiField.FILE_META,
            ApiField.FIGURES_COUNT,
            ApiField.ANN_OBJECTS_COUNT,
            ApiField.PROCESSING_PATH,
        ]

    @staticmethod
    def info_tuple_name():
        """
        Get string name of :class:`VolumeInfo<VolumeInfo>` NamedTuple.

        :return: NamedTuple name.
        :rtype: :class:`str`
        """

        return "VolumeInfo"

    def _convert_json_info(self, info: dict, skip_missing=True):
        """Private method. Convert volume information from json to VolumeInfo<VolumeInfo>"""

        res = super()._convert_json_info(info, skip_missing=skip_missing)
        return VolumeInfo(**res._asdict())

    def get_list(
        self,
        dataset_id: int,
        filters=None,
        sort: Literal["id", "name", "description", "createdAt", "updatedAt"] = "id",
        sort_order: Literal["asc", "desc"] = "asc",
    ) -> List[VolumeInfo]:
        """
        Get list of information about all volumes for a given dataset ID.

        :param dataset_id: :class:`Dataset<supervisely.project.project.Dataset>` ID in Supervisely.
        :type dataset_id: int
        :param filters: List of parameters to sort output Volumes. See: https://api.docs.supervisely.com/#tag/Volumes/paths/~1volumes.list/get
        :type filters: List[Dict[str, str]], optional
        :param sort: Attribute to sort the list by. The default is "id". Valid values are "id", "name", "description", "createdAt", "updatedAt".
        :type sort: :class:`str`
        :param sort_order: Order in which to sort the list. The default is "asc". Valid values are "asc" (ascending) and "desc" (descending).
        :type sort_order: :class:`str`
        :return: List of information about volumes in given dataset.
        :rtype: :class:`List[VolumeInfo]`

        :Usage example:

         .. code-block:: python

            import supervisely as sly

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()

            dataset_id = 61803

            volume_infos = api.volume.get_list(dataset_id)
            print(volume_infos)
            # Output: [VolumeInfo(id=19581134, ...), VolumeInfo(id=19581135, ...), VolumeInfo(id=19581136, ...)]

            sorted_volume_infos = api.volume.get_list(dataset_id, sort="id", sort_order="desc")
            # Output: [VolumeInfo(id=19581136, ...), VolumeInfo(id=19581135, ...), VolumeInfo(id=19581134, ...)]

            filtered_volume_infos = api.volume.get_list(dataset_id, filters=[{'field': 'id', 'operator': '=', 'value': '19581135'}])
            print(filtered_volume_infos)
            # Output: [VolumeInfo(id=19581135, ...)]
        """

        return self.get_list_all_pages(
            "volumes.list",
            {
                ApiField.DATASET_ID: dataset_id,
                ApiField.FILTER: filters or [],
                ApiField.SORT: sort,
                ApiField.SORT_ORDER: sort_order,
            },
        )

    def get_info_by_id(self, id: int):
        """
        Get Volume information by ID in VolumeInfo<VolumeInfo> format.

        :param id: Volume ID in Supervisely.
        :type id: int
        :return: Information about Volume. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`VolumeInfo`

        :Usage example:

         .. code-block:: python

            import supervisely as sly


            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()

            volume_id = 19581134
            volume_info = api.volume.get_info_by_id(volume_id)
            print(volume_info)
            # Output:
            # VolumeInfo(
            #     id=19581134,
            #     name='CTChest.nrrd',
            #     link=None,
            #     hash='+0K2oFHpqA5dwRKQlhkvhXEh52cs=',
            #     mime=None,
            #     ext=None,
            #     sizeb=46073411,
            #     created_at='2023-03-29T12:30:37.078Z',
            #     updated_at='2023-03-29T12:30:37.078Z',
            #     meta={
            #         'ACS': 'RAS',
            #         'intensity': {'max': 3071, 'min': -3024},
            #         'windowWidth': 6095,
            #         'rescaleSlope': 1,
            #         'windowCenter': 23.5,
            #         'channelsCount': 1,
            #         'dimensionsIJK': {'x': 512, 'y': 512, 'z': 139},
            #         'IJK2WorldMatrix': [0.7617189884185793, 0, 0, -194.238403081894, 0, 0.7617189884185793, 0, -217.5384061336518, 0, 0, 2.5, -347.7500000000001, 0, 0, 0, 1],
            #         'rescaleIntercept': 0
            #     },
            #     path_original='/h5af-public/images/original/M/e/7R/vs0p.nrrd',
            #     full_storage_url='https://app.supervisely.com/.../original/M/e/7R/zX0p.nrrd',
            #     tags=[],
            #     team_id=435,
            #     workspace_id=685,
            #     project_id=18949,
            #     dataset_id=61803,
            #     file_meta={
            #             'mime': 'image/nrrd',
            #             'size': 46073411,
            #             'type': 'int32',
            #             'extra': {'stride': [1, 512, 262144],
            #             'comments': []
            #         }
            #         'sizes': [512, 512, 139]
            #         'space': 'right-anterior-superior'
            #         'endian': 'little'
            #         'encoding': 'gzip'
            #         'dimension': 3
            #         'space origin': [-194.238403081894, -217.5384061336518, -347.7500000000001]
            #         'space dimension': 3
            #         'space directions': [[0.7617189884185793, 0, 0], [0, 0.7617189884185793, 0], [0, 0, 2.5]]
            #     }
            #     figures_count=None,
            #     objects_count=None,
            #     processing_path='1/1560071'
            # )
        """

        return self._get_info_by_id(id, "volumes.info")

    def upload_hash(self, dataset_id: int, name: str, hash: str, meta: dict = None):
        """
        Upload Volume from given hash to Dataset.

        :param dataset_id: Dataset ID in Supervisely.
        :type dataset_id: int
        :param name: Volume name with extension.
        :type name: str
        :param hash: Volume hash.
        :type hash: str
        :param meta: A dictionary containing data associated with the volume.
        :type meta: dict
        :return: Information about Volume. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`VolumeInfo`
        :Usage example:

         .. code-block:: python

            import supervisely as sly

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()

            dst_dataset_id = 61958
            src_volume_id = 19581134
            volume_info = api.volume.get_info_by_id(src_volume_id)
            hash = volume_info.hash
            # It is necessary to upload volume with the same extention as in src dataset
            name = volume_info.name
            meta = volume_info.meta
            new_volume_info = api.volume.upload_hash(dst_dataset_id, name, hash, meta)
            print(new_volume_info)
            # Output:
            # VolumeInfo(
            #     id=19613940,
            #     name='CTACardio.nrrd',
            #     link=None,
            #     hash='+0K2oFHpqA5dwRKQlh5bDUA0jkPsEE52cs=',
            #     mime=None,
            #     ext=None,
            #     sizeb=67614735,
            #     created_at='2023-03-29T12:30:37.078Z',
            #     updated_at='2023-03-29T12:30:37.078Z',
            #     meta={
            #         'ACS': 'RAS',
            #         'intensity': {'max': 3532, 'min': -1024},
            #         'windowWidth': 4556,
            #         'rescaleSlope': 1,
            #         'windowCenter': 1254,
            #         'channelsCount': 1,
            #         'dimensionsIJK': {'x': 512, 'y': 512, 'z': 321}
            #         'IJK2WorldMatrix': [0.9335939999999999, 0, 0, -238.53326699999997, 0, 0.9335939999999999, 0, -238.53326699999994, 0, 0, 1.25, -200.0000000000001, 0, 0, 0, 1],
            #         'rescaleIntercept': 0
            #     },
            #     path_original='/h5af-public/images/original/M/e/7R/zfsfX0p.nrrd',
            #     full_storage_url='https://app.supervisely.com/h5un-public/images/original/M/e/7R/zXdd0p.nrrd',
            #     tags=[],
            #     team_id=435,
            #     workspace_id=685,
            #     project_id=18949,
            #     dataset_id=61958,
            #     file_meta={
            #             'mime': 'image/nrrd',
            #             'size': 46073411,
            #             'type': 'int32',
            #             'extra': {'stride': [1, 512, 262144],
            #             'comments': []
            #         }
            #         'sizes': [512, 512, 139]
            #         'space': 'right-anterior-superior'
            #         'endian': 'little'
            #         'encoding': 'gzip'
            #         'dimension': 3
            #         'space origin': [-194.238403081894, -217.5384061336518, -347.7500000000001]
            #         'space dimension': 3
            #         'space directions': [[0.7617189884185793, 0, 0], [0, 0.7617189884185793, 0], [0, 0, 2.5]]
            #     }
            #     figures_count=None,
            #     objects_count=None,
            #     processing_path='1/1560071'
            # )
        """

        metas = None if meta is None else [meta]
        return self.upload_hashes(dataset_id, [name], [hash], metas=metas)[0]

    def upload_hashes(
        self,
        dataset_id: int,
        names: List[str],
        hashes: List[str],
        progress_cb: Optional[Union[tqdm, Callable]] = None,
        metas: List[dict] = None,
    ):
        """
        Upload Volumes from given hashes to Dataset.

        :param dataset_id: Dataset ID in Supervisely.
        :type dataset_id: int
        :param names: Volumes names with extension.
        :type names: List[str]
        :param hashes: Volumes hashes.
        :type hashes: List[str]
        :param progress_cb: Function for tracking download progress.
        :type progress_cb: tqdm or callable, optional
        :param metas: Volumes metadata.
        :type metas: List[dict], optional
        :return: List with information about Volumes. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`List[VolumeInfo]`
        :Usage example:

         .. code-block:: python

            import supervisely as sly
            from tqdm import tqdm

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()

            src_dataset_id = 61958
            dst_dataset_id = 55853

            hashes = []
            names = []
            metas = []
            volume_infos = api.volume.get_list(src_dataset_id)

            # Create lists of hashes, volumes names and meta information for each volume
            for volume_info in volume_infos:
                hashes.append(volume_info.hash)
                # It is necessary to upload volumes with the same names(extentions) as in src dataset
                names.append(volume_info.name)
                metas.append(volume_info.meta)

            p = tqdm(desc="api.volume.upload_hashes", total=len(hashes))
            new_volumes_info = api.volume.upload_hashes(
                dataset_id=dst_dataset_id,
                names=names,
                hashes=hashes,
                progress_cb=p,
                metas=metas,
            )

            # Output:
            # {"message": "progress", "event_type": "EventType.PROGRESS", "subtask": "Volumes upload: ", "current": 0, "total": 2, "timestamp": "2023-04-04T07:47:11.506Z", "level": "info"}
            # {"message": "progress", "event_type": "EventType.PROGRESS", "subtask": "Volumes upload: ", "current": 2, "total": 2, "timestamp": "2023-04-04T07:47:11.563Z", "level": "info"}
        """

        return self._upload_bulk_add(
            lambda item: (ApiField.HASH, item),
            dataset_id,
            names,
            hashes,
            progress_cb,
            metas=metas,
        )

    def _upload_bulk_add(
        self, func_item_to_kv, dataset_id, names, items, progress_cb=None, metas=None
    ):
        """
        Private method. Bulk upload volumes to Dataset.
        """

        results = []

        if len(names) == 0:
            return results
        if len(names) != len(items):
            raise RuntimeError('Can not match "names" and "items" lists, len(names) != len(items)')

        if metas is None:
            metas = [{}] * len(names)
        else:
            if len(names) != len(metas):
                raise RuntimeError('Can not match "names" and "metas" len(names) != len(metas)')

        for batch in batched(list(zip(names, items, metas))):
            volumes = []
            for name, item, meta in batch:
                item_tuple = func_item_to_kv(item)
                image_data = {ApiField.NAME: name, item_tuple[0]: item_tuple[1]}
                if len(meta) != 0 and type(meta) == dict:
                    image_data[ApiField.META] = meta
                volumes.append(image_data)

            response = self._api.post(
                "volumes.bulk.add",
                {ApiField.DATASET_ID: dataset_id, ApiField.VOLUMES: volumes},
            )
            if progress_cb is not None:
                progress_cb(len(volumes))

            for info_json in response.json():
                results.append(self._convert_json_info(info_json))
        return results

    def upload_np(
        self,
        dataset_id: int,
        name: str,
        np_data,
        meta: dict,
        progress_cb: Optional[Union[tqdm, Callable]] = None,
        batch_size: int = 30,
    ):
        """
        Upload given Volume in numpy format with given name to Dataset.

        :param dataset_id: Dataset ID in Supervisely.
        :type dataset_id: int
        :param name: Volume name with extension.
        :type name: str
        :param np_data: image in RGB format(numpy matrix)
        :type np_data: np.ndarray
        :param meta: Volume metadata.
        :type meta: dict, optional
        :param progress_cb: Function for tracking download progress.
        :type progress_cb: tqdm or callable, optional
        :return: Information about Volume. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`VolumeInfo`
        :Usage example:

         .. code-block:: python

            import supervisely as sly

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()

            np_volume, meta = sly.volume.read_nrrd_serie_volume_np(local_path)
            nrrd_info_np = api.volume.upload_np(
                dataset.id,
                "MRHead_np.nrrd",
                np_volume,
                meta,
            )
            print(f"Volume uploaded as NumPy array to Supervisely with ID:{nrrd_info_np.id}")

            # Output:
            # Volume uploaded as NumPy array to Supervisely with ID:18562982
        """

        ext = get_file_ext(name)
        if ext != ".nrrd":
            raise ValueError("Name has to be with .nrrd extension, for example: my_volume.nrrd")
        from timeit import default_timer as timer

        with logging_redirect_tqdm():
            logger.debug(f"Start volume {name} compression before upload...")

        start = timer()
        volume_bytes = volume.encode(np_data, meta)
        with logging_redirect_tqdm([logger]):
            logger.debug(f"Volume has been compressed in {timer() - start} seconds")
            logger.debug(f"Start uploading bytes of '{name}' volume ...")

        start = timer()
        volume_hash = get_bytes_hash(volume_bytes)
        self._api.image._upload_data_bulk(lambda v: v, [(volume_bytes, volume_hash)])

        with logging_redirect_tqdm([logger]):
            logger.debug(
                f"3D volume bytes has been sucessfully uploaded in {timer() - start} seconds"
            )

        volume_info = self.upload_hash(dataset_id, name, volume_hash, meta)
        if progress_cb is not None:
            progress_cb(1)  # upload volume

        # slice all directions
        # http://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/Python_html/03_Image_Details.html#Conversion-between-numpy-and-SimpleITK
        # x = 1 - sagittal
        # y = 1 - coronal
        # z = 1 - axial
        planes = [Plane.SAGITTAL, Plane.CORONAL, Plane.AXIAL]

        for plane, dimension in zip(planes, np_data.shape):
            for batch in batched(list(range(dimension))):
                slices = []
                slices_bytes = []
                slices_hashes = []
                try:
                    for i in batch:
                        normal = Plane.get_normal(plane)

                        if plane == Plane.SAGITTAL:
                            pixel_data = np_data[i, :, :]
                        elif plane == Plane.CORONAL:
                            pixel_data = np_data[:, i, :]
                        elif plane == Plane.AXIAL:
                            pixel_data = np_data[:, :, i]
                        else:
                            raise ValueError(f"Unknown plane {plane}")

                        img_bytes = nrrd_encoder.encode(
                            pixel_data, header={"encoding": "gzip"}, compression_level=1
                        )

                        img_hash = get_bytes_hash(img_bytes)
                        slices_bytes.append(img_bytes)
                        slices_hashes.append(img_hash)
                        slices.append(
                            {
                                "hash": img_hash,
                                "sliceIndex": i,
                                "normal": normal,
                            }
                        )

                    if len(slices) > 0:
                        self._api.image._upload_data_bulk(
                            lambda v: v,
                            zip(slices_bytes, slices_hashes),
                        )
                        self._upload_slices_bulk(volume_info.id, slices, progress_cb)

                except Exception as e:
                    exc_str = str(e)
                    logger.warn(
                        "File skipped due to error: {}".format(exc_str),
                        exc_info=True,
                        extra={
                            "exc_str": exc_str,
                            "file_path": name,
                        },
                    )
        return volume_info

    def upload_dicom_serie_paths(
        self,
        dataset_id: int,
        name: str,
        paths: List[str],
        log_progress: bool = True,
        anonymize: bool = True,
    ) -> VolumeInfo:
        """
        Upload given DICOM series from given paths to Dataset.

        :param dataset_id: Dataset ID in Supervisely.
        :type dataset_id: int
        :param name: Volume name with extension.
        :type name: str
        :param paths: Local volumes paths.
        :type paths: List[str]
        :param log_progress: Determine if additional technical logs are displaying.
        :type log_progress: bool, optional
        :param anonymize: Determine whether to hide PatientID and PatientName fields.
        :type anonymize: bool, optional
        :return: Information about Volume. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`VolumeInfo`
        :Usage example:

         .. code-block:: python

            import supervisely as sly

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()


            dicom_dir_name = "src/upload/MRHead_dicom/"
            series_infos = sly.volume.inspect_dicom_series(root_dir=dicom_dir_name)

            for serie_id, files in series_infos.items():
                item_path = files[0]
                name = f"{sly.fs.get_file_name(path=item_path)}.nrrd"
                dicom_info = api.volume.upload_dicom_serie_paths(
                    dataset_id=dataset.id,
                    name=name,
                    paths=files,
                    anonymize=True,
                )
                print(f"DICOM volume has been uploaded to Supervisely with ID: {dicom_info.id}")

            # Output:
            # DICOM volume has been uploaded to Supervisely with ID: 18630608
        """

        volume_np, volume_meta = volume.read_dicom_serie_volume_np(paths, anonymize=anonymize)
        progress_cb = None
        if log_progress is True:
            progress_cb = Progress(f"Upload volume {name}", sum(volume_np.shape)).iters_done_report
        res = self.upload_np(dataset_id, name, volume_np, volume_meta, progress_cb)
        return self.get_info_by_name(dataset_id, name)

    def _upload_slices_bulk(
        self, volume_id: int, items, progress_cb: Optional[Union[tqdm, Callable]] = None
    ):
        """
        Private method for volume slices bulk uploading.

        :param volume_id: Volume ID in Supervisely.
        :type volume_id: int
        :param items: Volume slices to upload
        :type items: list
        :param progress_cb: Function for tracking download progress.
        :type progress_cb: tqdm or callable, optional
        :return: List of responses
        :rtype: list
        """

        results = []
        if len(items) == 0:
            return results

        for batch in batched(items):
            response = self._api.post(
                "volumes.slices.bulk.add",
                {ApiField.VOLUME_ID: volume_id, ApiField.VOLUME_SLICES: batch},
            )
            if progress_cb is not None:
                progress_cb(len(batch))
            results.extend(response.json())
        return results

    def upload_nrrd_serie_path(
        self, dataset_id: int, name: str, path: str, log_progress=True, progress_cb=None
    ) -> VolumeInfo:
        """
        Upload NRRD format volume from given path to Dataset.

        :param dataset_id: Dataset ID in Supervisely.
        :type dataset_id: int
        :param name: Volume name with extension.
        :type name: str
        :param path: Local volume path.
        :type path: str
        :param log_progress: Determine if additional technical logs are displaying.
        :type log_progress: bool, optional
        :return: Information about Volume. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`VolumeInfo`
        :Usage example:

         .. code-block:: python

            import supervisely as sly

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()


            local_path = "src/upload/nrrd/MRHead.nrrd"

            nrrd_info = api.volume.upload_nrrd_serie_path(
                dataset.id,
                "MRHead.nrrd",
                local_path,
            )
            print(f'"{nrrd_info.name}" volume uploaded to Supervisely with ID:{nrrd_info.id}')

            # Output:
            # "NRRD_1.nrrd" volume uploaded to Supervisely with ID:18562981
        """

        volume_np, volume_meta = volume.read_nrrd_serie_volume_np(path)

        progress_nrrd = None
        if log_progress is True or progress_cb is not None:
            progress_nrrd = tqdm_sly(
                desc=f"Uploading volume '{name}'",
                total=sum(volume_np.shape),
                leave=True if progress_cb is None else False,
                position=1,
            )
        res = self.upload_np(dataset_id, name, volume_np, volume_meta, progress_nrrd)
        return self.get_info_by_name(dataset_id, name)

    def _download(self, id: int, is_stream: bool = False):
        """
        Private method for volume downloading.

        :param id: Volume ID in Supervisely.
        :type id: int
        :param stream: Define, if you'd like to get the raw socket response from the server.
        :type stream: bool, optional
        :return: Response object
        :rtype: :class:`Response`
        """

        response = self._api.post("volumes.download", {ApiField.ID: id}, stream=is_stream)
        return response

    def download_path(
        self, id: int, path: str, progress_cb: Optional[Union[tqdm, Callable]] = None
    ):
        """
        Download volume with given ID to local directory.

        :param id: Volume ID in Supervisely.
        :type id: int
        :param path: Local path to save volume.
        :type path: str
        :param progress_cb: Function for tracking download progress.
        :type progress_cb: tqdm or callable, optional
        :return: Information about Volume. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`VolumeInfo`
        :Usage example:

         .. code-block:: python

            import supervisely as sly
            from tqdm import tqdm

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()

            src_dataset_id = 61229
            volume_infos = api.volume.get_list(src_dataset_id)
            volume_id = volume_infos[0].id
            volume_info = api.volume.get_info_by_id(id=volume_id)

            download_dir_name = "src/download/"
            path = os.path.join(download_dir_name, volume_info.name)
            if os.path.exists(path):
                os.remove(path)

            p = tqdm(desc="Volumes upload: ", total=volume_info.sizeb, is_size=True)
            api.volume.download_path(volume_info.id, path, progress_cb=p)

            if os.path.exists(path):
                print(f"Volume (ID {volume_info.id}) successfully downloaded.")

            # Output:
            # Volume (ID 18630603) successfully downloaded.
        """

        response = self._download(id, is_stream=True)
        ensure_base_path(path)

        with open(path, "wb") as fd:
            mb1 = 1024 * 1024
            for chunk in response.iter_content(chunk_size=mb1):
                fd.write(chunk)

                if progress_cb is not None:
                    progress_cb(len(chunk))

    def upload_nrrd_series_paths(
        self,
        dataset_id: int,
        names: List[str],
        paths: List[str],
        progress_cb: Optional[Union[tqdm, Callable]] = None,
        log_progress: bool = True,
    ):
        """
        Upload NRRD format volumes from given paths to Dataset.

        :param dataset_id: Dataset ID in Supervisely.
        :type dataset_id: int
        :param names: Volumes names with extensions.
        :type names: List[str]
        :param paths: Local volumes paths.
        :type paths: List[str]
        :param log_progress: Determine if additional technical logs are displaying.
        :type log_progress: bool
        :param progress_cb: Function for tracking download progress.
        :type progress_cb: tqdm or callable, optional
        :return: Information about Volume. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`VolumeInfo`
        :Usage example:

         .. code-block:: python

            import supervisely as sly

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()


            local_dir_name = "src/upload/nrrd/"
            all_nrrd_names = os.listdir(local_dir_name)
            names = [f"1_{name}" for name in all_nrrd_names]
            paths = [os.path.join(local_dir_name, name) for name in all_nrrd_names]

            volume_infos = api.volume.upload_nrrd_series_paths(dataset.id, names, paths)
            print(f"All volumes has been uploaded with IDs: {[x.id for x in volume_infos]}")

            # Output:
            # All volumes has been uploaded with IDs: [18630605, 18630606, 18630607]
        """

        volume_infos = []
        for name, path in zip(names, paths):
            info = self.upload_nrrd_serie_path(dataset_id, name, path, log_progress, progress_cb)
            volume_infos.append(info)
            if progress_cb is not None:
                progress_cb(1)
        return volume_infos

    def download_slice_np(
        self,
        volume_id: int,
        slice_index: int,
        plane: Literal["sagittal", "coronal", "axial"],
        window_center: float = None,
        window_width: int = None,
    ):
        """
        Download slice as NumPy from Supervisely by ID.

        :param volume_id: Volume ID in Supervisely.
        :type volume_id: int
        :param slice_index: :py:class:`Slice<supervisely.volume_annotation.slice.Slice>` index.
        :type slice_index: int
        :param plane: :py:class:`Plane<supervisely.volume_annotation.plane.Plane>` of the slice in volume.
        :type plane: str
        :param window_center: Window center.
        :type window_center: float
        :param window_width: Window width.
        :type window_width: int
        :return: Information about Volume. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`VolumeInfo`
        :Usage example:

         .. code-block:: python

            import supervisely as sly

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()


            slice_index = 60

            image_np = api.volume.download_slice_np(
                volume_id=volume_id,
                slice_index=slice_index,
                plane=sly.Plane.SAGITTAL,
            )

            print(f"Image downloaded as NumPy array. Image shape: {image_np.shape}")

            # Output:
            # Image downloaded as NumPy array. Image shape: (256, 256, 3)
        """

        normal = Plane.get_normal(plane)
        meta = self.get_info_by_id(volume_id).meta

        if window_center is None:
            if "windowCenter" in meta:
                window_center = meta["windowCenter"]
            else:
                window_center = meta["intensity"]["min"] + meta["windowWidth"] / 2

        if window_width is None:
            if "windowWidth" in meta:
                window_width = meta["windowWidth"]
            else:
                window_width = meta["intensity"]["max"] - meta["intensity"]["min"]

        data = {
            "volumeId": volume_id,
            "sliceIndex": slice_index,
            "normal": normal,
            "windowCenter": window_center,
            "windowWidth": window_width,
        }
        image_bytes = self._api.post(
            method="volumes.slices.images.download", data=data, stream=True
        ).content

        return read_bytes(image_bytes)

    def get_free_names(self, dataset_id: int, names: List[str]) -> List[str]:
        """
        Returns list of free names for given dataset.

        :param dataset_id: Dataset ID in Supervisely.
        :type dataset_id: int
        :param names: List of names to check.
        :type names: List[str]
        :return: List of free names.
        :rtype: List[str]
        """

        volumes_in_dataset = self.get_list(dataset_id)
        used_names = {volume_info.name for volume_info in volumes_in_dataset}
        new_names = [
            generate_free_name(used_names, name, with_ext=True, extend_used_names=True)
            for name in names
        ]
        return new_names

    def raise_name_intersections_if_exist(
        self, dataset_id: int, names: List[str], message: str = None
    ):
        """
        Raises error if volumes with given names already exist in dataset.
        Default error message:
        "Volumes with the following names already exist in dataset [ID={dataset_id}]: {name_intersections}.
        Please, rename volumes and try again or set change_name_if_conflict=True to rename automatically on upload."
        :param dataset_id: Dataset ID in Supervisely.
        :type dataset_id: int
        :param names: List of names to check.
        :type names: List[str]
        :param message: Error message.
        :type message: str, optional
        :return: None
        :rtype: None
        """
        volumes_in_dataset = self.get_list(dataset_id)
        used_names = {volume_info.name for volume_info in volumes_in_dataset}
        name_intersections = used_names.intersection(set(names))
        if message is None:
            message = f"Volumes with the following names already exist in dataset [ID={dataset_id}]: {name_intersections}. Please, rename volumes and try again or set change_name_if_conflict=True to rename automatically on upload."
        if len(name_intersections) > 0:
            raise ValueError(f"{message}")

    def upload_dir(
        self,
        dataset_id: int,
        dir_path: str,
        progress_cb: Optional[Union[tqdm, Callable]] = None,
        log_progress: bool = False,
        change_name_if_conflict: bool = True,
    ) -> List[VolumeInfo]:
        """
        Upload all volumes from given directory to Dataset recursively.

        :param dataset_id: Dataset ID in Supervisely.
        :type dataset_id: int
        :param dir_path: Local directory path.
        :type dir_path: str
        :param progress_cb: Function for tracking download progress.
        :type progress_cb: tqdm or callable, optional
        :param log_progress: Determine if additional technical logs are displaying.
        :type log_progress: bool
        :param change_name_if_conflict: Determine if names are changing if conflict.
        :type change_name_if_conflict: bool, optional
        :return: List with information about Volumes. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`List[VolumeInfo]`
        :Usage example:

             .. code-block:: python

                import supervisely as sly
                from tqdm import tqdm

                os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
                os.environ['API_TOKEN'] = 'Your Supervisely API Token'

                api = sly.Api.from_env()

                dataset_id = 61958
                dir_path = "src/upload/volumes/"
                volume_infos = api.volume.upload_dir(dataset_id, dir_path)
                print(f"All volumes has been uploaded with IDs: {[x.id for x in volume_infos]}")

                # Output:
                # All volumes has been uploaded with IDs: [18630605, 18630606, 18630607]
        """
        names = []
        paths = []

        if os.path.isdir(dir_path) is False:
            raise ValueError(f"Path {dir_path} is not a directory or does not exist")

        dcm_volumes = inspect_dicom_series(dir_path, logging=log_progress)
        for serie, files in dcm_volumes.items():
            name = f"{serie}.nrrd"
            names.append(name)
            paths.append(files)
        nrrd_volumes = inspect_nrrd_series(dir_path, logging=log_progress)
        for volume_path in nrrd_volumes:
            name = get_file_name_with_ext(volume_path)
            names.append(name)
            paths.append(volume_path)

        if change_name_if_conflict:
            names = self.get_free_names(dataset_id, names)
        else:
            self.raise_name_intersections_if_exist(dataset_id, names)

        volume_infos = []
        for name, path in zip(names, paths):
            if isinstance(path, tuple):
                volume_info = self.upload_dicom_serie_paths(
                    dataset_id=dataset_id,
                    name=name,
                    paths=path,
                    log_progress=log_progress,
                )
            else:
                volume_info = self.upload_nrrd_serie_path(
                    dataset_id=dataset_id,
                    name=name,
                    path=path,
                    log_progress=log_progress,
                )
            volume_infos.append(volume_info)
            if progress_cb is not None:
                progress_cb(1)
        return volume_infos

    def upload_dirs(
        self,
        dataset_id: int,
        dir_paths: List[str],
        progress_cb: Optional[Union[tqdm, Callable]] = None,
        log_progress: bool = False,
        change_name_if_conflict: bool = True,
    ) -> List[VolumeInfo]:
        """
        Upload all volumes from given directories to Dataset recursively.

        :param dataset_id: Dataset ID in Supervisely.
        :type dataset_id: int
        :param dir_paths: List of local directory paths.
        :type dir_paths: List[str]
        :param progress_cb: Function for tracking download progress.
        :type progress_cb: tqdm or callable, optional
        :param log_progress: Determine if additional technical logs are displaying.
        :type log_progress: bool
        :param change_name_if_conflict: Determine if names are changing if conflict.
        :type change_name_if_conflict: bool, optional
        :return: List with information about Volumes. See :class:`info_sequence<info_sequence>`
        :rtype: :class:`List[VolumeInfo]`
        :Usage example:

             .. code-block:: python

                import supervisely as sly
                from tqdm import tqdm

                os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
                os.environ['API_TOKEN'] = 'Your Supervisely API Token'

                api = sly.Api.from_env()

                dataset_id = 61958
                dir_paths = ["src/upload/volumes1/", "src/upload/volumes2/"]
                volume_infos = api.volume.upload_dirs(dataset_id, dir_paths)
                print(f"All volumes has been uploaded with IDs: {[x.id for x in volume_infos]}")

                # Output:
                # All volumes has been uploaded with IDs: [18630605, 18630606, 18630607]
        """
        volume_infos = []
        if not isinstance(dir_paths, list):
            raise ValueError(f"dir_paths must be a list of strings, but got {type(dir_paths)}")

        for dir_path in dir_paths:
            volume_infos.extend(
                self.upload_dir(
                    dataset_id, dir_path, progress_cb, log_progress, change_name_if_conflict
                )
            )
        return volume_infos

    async def _download_async(
        self,
        id: int,
        is_stream: bool = False,
        range_start: Optional[int] = None,
        range_end: Optional[int] = None,
        headers: Optional[dict] = None,
        chunk_size: int = 1024 * 1024,
    ) -> AsyncGenerator:
        """
        Download Volume with given ID asynchronously.
        If is_stream is True, returns stream of bytes, otherwise returns response object.
        For streaming, returns tuple of chunk and hash.

        :param id: Volume ID in Supervisely.
        :type id: int
        :param is_stream: If True, returns stream of bytes, otherwise returns response object.
        :type is_stream: bool, optional
        :param range_start: Start byte of range for partial download.
        :type range_start: int, optional
        :param range_end: End byte of range for partial download.
        :type range_end: int, optional
        :param headers: Headers for request.
        :type headers: dict, optional
        :param chunk_size: Size of chunk for downloading. Default is 1MB.
        :type chunk_size: int, optional
        :return: Stream of bytes or response object.
        :rtype: AsyncGenerator
        """
        api_method_name = "volumes.download"

        json_body = {ApiField.ID: id}

        if is_stream:
            async for chunk, hhash in self._api.stream_async(
                api_method_name,
                "POST",
                json_body,
                headers=headers,
                range_start=range_start,
                range_end=range_end,
                chunk_size=chunk_size,
            ):
                yield chunk, hhash
        else:
            response = await self._api.post_async(api_method_name, json_body, headers=headers)
            yield response

    async def download_path_async(
        self,
        id: int,
        path: str,
        semaphore: Optional[asyncio.Semaphore] = None,
        range_start: Optional[int] = None,
        range_end: Optional[int] = None,
        headers: Optional[dict] = None,
        chunk_size: int = 1024 * 1024,
        check_hash: bool = True,
        progress_cb: Optional[Union[tqdm, Callable]] = None,
        progress_cb_type: Literal["number", "size"] = "number",
    ) -> None:
        """
        Downloads Volume with given ID to local path.

        :param id: Volume ID in Supervisely.
        :type id: int
        :param path: Local save path for Volume.
        :type path: str
        :param semaphore: Semaphore for limiting the number of simultaneous downloads.
        :type semaphore: :class:`asyncio.Semaphore`, optional
        :param range_start: Start byte of range for partial download.
        :type range_start: int, optional
        :param range_end: End byte of range for partial download.
        :type range_end: int, optional
        :param headers: Headers for request.
        :type headers: dict, optional
        :param chunk_size: Size of chunk for downloading. Default is 1MB.
        :type chunk_size: int, optional
        :param check_hash: If True, checks hash of downloaded file.
                        Check is not supported for partial downloads.
                        When range is set, hash check is disabled.
        :type check_hash: bool, optional
        :param progress_cb: Function for tracking download progress.
        :type progress_cb: tqdm or callable, optional
        :param progress_cb_type: Type of progress callback. Can be "number" or "size". Default is "number".
        :type progress_cb_type: str, optional
        :return: None
        :rtype: :class:`NoneType`
        :Usage example:

         .. code-block:: python

            import supervisely as sly
            import asyncio

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()

            volume_info = api.volume.get_info_by_id(770918)
            save_path = os.path.join("/path/to/save/", volume_info.name)

            semaphore = asyncio.Semaphore(100)
            loop = sly.utils.get_or_create_event_loop()
            loop.run_until_complete(
                        api.volume.download_path_async(volume_info.id, save_path, semaphore)
                )
        """

        if range_start is not None or range_end is not None:
            check_hash = False  # Hash check is not supported for partial downloads
            headers = headers or {}
            headers["Range"] = f"bytes={range_start or ''}-{range_end or ''}"
            logger.debug(f"Image ID: {id}. Setting Range header: {headers['Range']}")

        writing_method = "ab" if range_start not in [0, None] else "wb"

        ensure_base_path(path)
        hash_to_check = None
        if semaphore is None:
            semaphore = self._api.get_default_semaphore()
        async with semaphore:
            async with aiofiles.open(path, writing_method) as fd:
                async for chunk, hhash in self._download_async(
                    id,
                    is_stream=True,
                    headers=headers,
                    range_start=range_start,
                    range_end=range_end,
                    chunk_size=chunk_size,
                ):
                    await fd.write(chunk)
                    hash_to_check = hhash
                    if progress_cb is not None and progress_cb_type == "size":
                        progress_cb(len(chunk))
            if check_hash:
                if hash_to_check is not None:
                    downloaded_file_hash = await get_file_hash_async(path)
                    if hash_to_check != downloaded_file_hash:
                        raise RuntimeError(
                            f"Downloaded hash of volume with ID:{id} does not match the expected hash: {downloaded_file_hash} != {hash_to_check}"
                        )
            if progress_cb is not None and progress_cb_type == "number":
                progress_cb(1)

    async def download_paths_async(
        self,
        ids: List[int],
        paths: List[str],
        semaphore: Optional[asyncio.Semaphore] = None,
        headers: Optional[dict] = None,
        chunk_size: int = 1024 * 1024,
        check_hash: bool = True,
        progress_cb: Optional[Union[tqdm, Callable]] = None,
        progress_cb_type: Literal["number", "size"] = "number",
    ) -> None:
        """
        Download Volumes with given IDs and saves them to given local paths asynchronously.

        :param ids: List of Volume IDs in Supervisely.
        :type ids: :class:`List[int]`
        :param paths: Local save paths for Volumes.
        :type paths: :class:`List[str]`
        :param semaphore: Semaphore for limiting the number of simultaneous downloads.
        :type semaphore: :class:`asyncio.Semaphore`, optional
        :param headers: Headers for request.
        :type headers: dict, optional
        :param chunk_size: Size of chunk for downloading. Default is 1MB.
        :type chunk_size: int, optional
        :param check_hash: If True, checks hash of downloaded file.
        :type check_hash: bool, optional
        :param progress_cb: Function for tracking download progress.
        :type progress_cb: tqdm or callable, optional
        :param progress_cb_type: Type of progress callback. Can be "number" or "size". Default is "number".
        :type progress_cb_type: str, optional
        :raises: :class:`ValueError` if len(ids) != len(paths)
        :return: None
        :rtype: :class:`NoneType`

        :Usage example:

         .. code-block:: python

            import supervisely as sly
            import asyncio

            os.environ['SERVER_ADDRESS'] = 'https://app.supervisely.com'
            os.environ['API_TOKEN'] = 'Your Supervisely API Token'
            api = sly.Api.from_env()

            ids = [770914, 770915]
            paths = ["/path/to/save/volume1.nrrd", "/path/to/save/volume2.nrrd"]
            loop = sly.utils.get_or_create_event_loop()
            loop.run_until_complete(api.volume.download_paths_async(ids, paths))
        """
        if len(ids) == 0:
            return
        if len(ids) != len(paths):
            raise ValueError(f'Can not match "ids" and "paths" lists, {len(ids)} != {len(paths)}')
        if semaphore is None:
            semaphore = self._api.get_default_semaphore()
        tasks = []
        for img_id, img_path in zip(ids, paths):
            task = self.download_path_async(
                img_id,
                img_path,
                semaphore,
                headers=headers,
                chunk_size=chunk_size,
                check_hash=check_hash,
                progress_cb=progress_cb,
                progress_cb_type=progress_cb_type,
            )
            tasks.append(task)
        await asyncio.gather(*tasks)

"""
Copy pillar data from a bucket in Amazon S3

The S3 pillar can be configured in the master config file with the following
options

.. code-block:: yaml

    ext_pillar:
      - s3:
          bucket: my.fancy.pillar.bucket
          keyid: KASKFJWAKJASJKDAJKSD
          key: ksladfDLKDALSFKSD93q032sdDasdfasdflsadkf
          multiple_env: False
          environment: base
          prefix: somewhere/overthere
          verify_ssl: True
          service_url: s3.amazonaws.com
          kms_keyid: 01234567-89ab-cdef-0123-4567890abcde
          s3_cache_expire: 30
          s3_sync_on_update: True
          path_style: False
          https_enable: True

The ``bucket`` parameter specifies the target S3 bucket. It is required.

The ``keyid`` parameter specifies the key id to use when access the S3 bucket.
If it is not provided, an attempt to fetch it from EC2 instance meta-data will
be made.

The ``key`` parameter specifies the key to use when access the S3 bucket. If it
is not provided, an attempt to fetch it from EC2 instance meta-data will be made.

The ``multiple_env`` defaults to False. It specifies whether the pillar should
interpret top level folders as pillar environments (see mode section below).

The ``environment`` defaults to 'base'. It specifies which environment the
bucket represents when in single environments mode (see mode section below). It
is ignored if multiple_env is True.

The ``prefix`` defaults to ''. It specifies a key prefix to use when searching
for data in the bucket for the pillar. It works when multiple_env is True or False.
Essentially it tells ext_pillar to look for your pillar data in a 'subdirectory'
of your S3 bucket

The ``verify_ssl`` parameter defaults to True. It specifies whether to check for
valid S3 SSL certificates. *NOTE* If you use bucket names with periods, this
must be set to False else an invalid certificate error will be thrown (issue
#12200).

The ``service_url`` parameter defaults to 's3.amazonaws.com'. It specifies the
base url to use for accessing S3.

The ``kms_keyid`` parameter is optional. It specifies the ID of the Key
Management Service (KMS) master key that was used to encrypt the object.

The ``s3_cache_expire`` parameter defaults to 30s. It specifies expiration
time of S3 metadata cache file.

The ``s3_sync_on_update`` parameter defaults to True. It specifies if cache
is synced on update rather than jit.

The ``path_style`` parameter defaults to False. It specifies whether to use
path style requests or dns style requests

The ``https_enable`` parameter defaults to True. It specifies whether to use
https protocol or http protocol

This pillar can operate in two modes, single environment per bucket or multiple
environments per bucket.

Single environment mode must have this bucket structure:

.. code-block:: text

    s3://<bucket name>/<prefix>/<files>

Multiple environment mode must have this bucket structure:

.. code-block:: text

    s3://<bucket name>/<prefix>/<environment>/<files>

If you wish to define your pillar data entirely within S3 it's recommended
that you use the `prefix=` parameter and specify one entry in ext_pillar
for each environment rather than specifying multiple_env. This is due
to issue #22471 (https://github.com/saltstack/salt/issues/22471)
"""

import logging
import os
import pickle
import time
import urllib.parse
from copy import deepcopy

import salt.utils.files
import salt.utils.hashutils
from salt.pillar import Pillar

log = logging.getLogger(__name__)


class S3Credentials:
    def __init__(
        self,
        key,
        keyid,
        bucket,
        service_url,
        verify_ssl=True,
        kms_keyid=None,
        location=None,
        path_style=False,
        https_enable=True,
    ):
        self.key = key
        self.keyid = keyid
        self.kms_keyid = kms_keyid
        self.bucket = bucket
        self.service_url = service_url
        self.verify_ssl = verify_ssl
        self.location = location
        self.path_style = path_style
        self.https_enable = https_enable


def ext_pillar(
    minion_id,
    pillar,  # pylint: disable=W0613
    bucket,
    key=None,
    keyid=None,
    verify_ssl=True,
    location=None,
    multiple_env=False,
    environment="base",
    prefix="",
    service_url=None,
    kms_keyid=None,
    s3_cache_expire=30,  # cache for 30 seconds
    s3_sync_on_update=True,  # sync cache on update rather than jit
    path_style=False,
    https_enable=True,
):
    """
    Execute a command and read the output as YAML
    """

    s3_creds = S3Credentials(
        key,
        keyid,
        bucket,
        service_url,
        verify_ssl,
        kms_keyid,
        location,
        path_style,
        https_enable,
    )

    # normpath is needed to remove appended '/' if root is empty string.
    pillar_dir = os.path.normpath(os.path.join(_get_cache_dir(), environment, bucket))
    if prefix:
        pillar_dir = os.path.normpath(os.path.join(pillar_dir, prefix))

    if __opts__["pillar_roots"].get(environment, []) == [pillar_dir]:
        return {}

    metadata = _init(
        s3_creds, bucket, multiple_env, environment, prefix, s3_cache_expire
    )

    if s3_sync_on_update:
        # sync the buckets to the local cache
        log.info("Syncing local pillar cache from S3...")
        for saltenv, env_meta in metadata.items():
            for bucket, files in _find_files(env_meta).items():
                for file_path in files:
                    cached_file_path = _get_cached_file_name(bucket, saltenv, file_path)
                    log.info("%s - %s : %s", bucket, saltenv, file_path)
                    # load the file from S3 if not in the cache or too old
                    _get_file_from_s3(
                        s3_creds, metadata, saltenv, bucket, file_path, cached_file_path
                    )

        log.info("Sync local pillar cache from S3 completed.")

    opts = deepcopy(__opts__)
    opts["pillar_roots"][environment] = (
        [os.path.join(pillar_dir, environment)] if multiple_env else [pillar_dir]
    )

    # Avoid recursively re-adding this same pillar
    opts["ext_pillar"] = [x for x in opts["ext_pillar"] if "s3" not in x]

    pil = Pillar(opts, __grains__, minion_id, environment)

    compiled_pillar = pil.compile_pillar(ext=False)

    return compiled_pillar


def _init(creds, bucket, multiple_env, environment, prefix, s3_cache_expire):
    """
    Connect to S3 and download the metadata for each file in all buckets
    specified and cache the data to disk.
    """

    cache_file = _get_buckets_cache_filename(bucket, prefix)
    exp = time.time() - s3_cache_expire

    # check if cache_file exists and its mtime
    if os.path.isfile(cache_file):
        cache_file_mtime = os.path.getmtime(cache_file)
    else:
        # file does not exists then set mtime to 0 (aka epoch)
        cache_file_mtime = 0

    expired = cache_file_mtime <= exp

    log.debug(
        "S3 bucket cache file %s is %sexpired, mtime_diff=%ss, expiration=%ss",
        cache_file,
        "" if expired else "not ",
        cache_file_mtime - exp,
        s3_cache_expire,
    )

    if expired:
        pillars = _refresh_buckets_cache_file(
            creds, cache_file, multiple_env, environment, prefix
        )
    else:
        pillars = _read_buckets_cache_file(cache_file)

    log.debug("S3 bucket retrieved pillars %s", pillars)
    return pillars


def _get_cache_dir():
    """
    Get pillar cache directory. Initialize it if it does not exist.
    """

    cache_dir = os.path.join(__opts__["cachedir"], "pillar_s3fs")

    if not os.path.isdir(cache_dir):
        log.debug("Initializing S3 Pillar Cache")
        os.makedirs(cache_dir)

    return cache_dir


def _get_cached_file_name(bucket, saltenv, path):
    """
    Return the cached file name for a bucket path file
    """

    file_path = os.path.join(_get_cache_dir(), saltenv, bucket, path)

    # make sure bucket and saltenv directories exist
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    return file_path


def _get_buckets_cache_filename(bucket, prefix):
    """
    Return the filename of the cache for bucket contents.
    Create the path if it does not exist.
    """

    cache_dir = _get_cache_dir()
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    return os.path.join(cache_dir, f"{bucket}-{prefix}-files.cache")


def _refresh_buckets_cache_file(creds, cache_file, multiple_env, environment, prefix):
    """
    Retrieve the content of all buckets and cache the metadata to the buckets
    cache file
    """

    # helper s3 query function
    def __get_s3_meta(continuation_token=None):
        # We want to use ListObjectsV2 so we get the NextContinuationToken
        params = {"prefix": prefix, "list-type": 2}

        if continuation_token:
            params["continuation-token"] = continuation_token

        return __utils__["s3.query"](
            key=creds.key,
            keyid=creds.keyid,
            kms_keyid=creds.kms_keyid,
            bucket=creds.bucket,
            service_url=creds.service_url,
            verify_ssl=creds.verify_ssl,
            location=creds.location,
            return_bin=False,
            params=params,
            path_style=creds.path_style,
            https_enable=creds.https_enable,
        )

    # grab only the files/dirs in the bucket
    def __get_pillar_files_from_s3_meta(s3_meta):
        return [k for k in s3_meta if "Key" in k]

    # pull out the environment dirs (e.g. the root dirs)
    def __get_pillar_environments(files):
        environments = [(os.path.dirname(k["Key"]).split("/", 1))[0] for k in files]
        return set(environments)

    def __get_continuation_token(s3_meta):
        return next(
            (
                item.get("NextContinuationToken")
                for item in s3_meta
                if item.get("NextContinuationToken")
            ),
            None,
        )

    log.debug("Refreshing S3 buckets pillar cache file")

    metadata = {}
    bucket = creds.bucket

    if not multiple_env:
        # Single environment per bucket
        log.debug("Single environment per bucket mode")

        bucket_files = {}
        s3_meta = __get_s3_meta()

        # s3 query returned something
        if s3_meta:
            bucket_files[bucket] = __get_pillar_files_from_s3_meta(s3_meta)

            # Check if we have a NextContinuationToken and loop until we don't
            while True:
                continuation_token = __get_continuation_token(s3_meta)
                if not continuation_token:
                    break
                s3_meta = __get_s3_meta(continuation_token)
                bucket_files[bucket] += __get_pillar_files_from_s3_meta(s3_meta)

            metadata[environment] = bucket_files

    else:
        # Multiple environments per buckets
        log.debug("Multiple environment per bucket mode")
        s3_meta = __get_s3_meta()

        # s3 query returned data
        if s3_meta:
            files = __get_pillar_files_from_s3_meta(s3_meta)

            # Check if we have a NextContinuationToken and loop until we don't
            while True:
                continuation_token = __get_continuation_token(s3_meta)
                if not continuation_token:
                    break
                s3_meta = __get_s3_meta(continuation_token)
                files += __get_pillar_files_from_s3_meta(s3_meta)

            environments = __get_pillar_environments(files)

            # pull out the files for the environment
            for saltenv in environments:
                # grab only files/dirs that match this saltenv.
                env_files = [k for k in files if k["Key"].startswith(saltenv)]

                if saltenv not in metadata:
                    metadata[saltenv] = {}

                if bucket not in metadata[saltenv]:
                    metadata[saltenv][bucket] = []

                metadata[saltenv][bucket] += env_files

    # write the metadata to disk
    if os.path.isfile(cache_file):
        os.remove(cache_file)

    log.debug("Writing S3 buckets pillar cache file")

    with salt.utils.files.fopen(cache_file, "wb") as fp_:
        pickle.dump(metadata, fp_)

    return metadata


def _read_buckets_cache_file(cache_file):
    """
    Return the contents of the buckets cache file
    """

    log.debug("Reading buckets cache file")

    with salt.utils.files.fopen(cache_file, "rb") as fp_:
        data = pickle.load(fp_)

    return data


def _find_files(metadata):
    """
    Looks for all the files in the S3 bucket cache metadata
    """

    ret = {}

    for bucket, data in metadata.items():
        if bucket not in ret:
            ret[bucket] = []

        # grab the paths from the metadata
        filePaths = [k["Key"] for k in data]
        # filter out the dirs
        ret[bucket] += [k for k in filePaths if not k.endswith("/")]

    return ret


def _find_file_meta(metadata, bucket, saltenv, path):
    """
    Looks for a file's metadata in the S3 bucket cache file
    """

    env_meta = metadata[saltenv] if saltenv in metadata else {}
    bucket_meta = env_meta[bucket] if bucket in env_meta else {}
    files_meta = list(list(filter((lambda k: "Key" in k), bucket_meta)))

    for item_meta in files_meta:
        if "Key" in item_meta and item_meta["Key"] == path:
            return item_meta


def _get_file_from_s3(creds, metadata, saltenv, bucket, path, cached_file_path):
    """
    Checks the local cache for the file, if it's old or missing go grab the
    file from S3 and update the cache
    """

    # check the local cache...
    if os.path.isfile(cached_file_path):
        file_meta = _find_file_meta(metadata, bucket, saltenv, path)
        file_md5 = (
            "".join(list(filter(str.isalnum, file_meta["ETag"]))) if file_meta else None
        )

        cached_md5 = salt.utils.hashutils.get_hash(cached_file_path, "md5")

        # hashes match we have a cache hit
        log.debug(
            "Cached file: path=%s, md5=%s, etag=%s",
            cached_file_path,
            cached_md5,
            file_md5,
        )
        if cached_md5 == file_md5:
            return

    # ... or get the file from S3
    __utils__["s3.query"](
        key=creds.key,
        keyid=creds.keyid,
        kms_keyid=creds.kms_keyid,
        bucket=bucket,
        service_url=creds.service_url,
        path=urllib.parse.quote(path),
        local_file=cached_file_path,
        verify_ssl=creds.verify_ssl,
        location=creds.location,
        path_style=creds.path_style,
        https_enable=creds.https_enable,
    )

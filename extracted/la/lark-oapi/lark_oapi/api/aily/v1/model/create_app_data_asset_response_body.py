# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .data_asset import DataAsset


class CreateAppDataAssetResponseBody(object):
    _types = {
        "data_asset": DataAsset,
    }

    def __init__(self, d=None):
        self.data_asset: Optional[DataAsset] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAppDataAssetResponseBodyBuilder":
        return CreateAppDataAssetResponseBodyBuilder()


class CreateAppDataAssetResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_app_data_asset_response_body = CreateAppDataAssetResponseBody()

    def data_asset(self, data_asset: DataAsset) -> "CreateAppDataAssetResponseBodyBuilder":
        self._create_app_data_asset_response_body.data_asset = data_asset
        return self

    def build(self) -> "CreateAppDataAssetResponseBody":
        return self._create_app_data_asset_response_body

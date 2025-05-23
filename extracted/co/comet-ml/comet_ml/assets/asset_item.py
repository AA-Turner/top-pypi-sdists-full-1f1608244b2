# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at https://www.comet.com
#  Copyright (C) 2015-2021 Comet ML INC
#  This source code is licensed under the MIT license.
# *******************************************************


class AssetItem:
    def __init__(self, file_path: str, file_name: str, type: str) -> None:
        self.file_path = file_path
        self.file_name = file_name
        self.type = type


def unserialize_items(serialized_items):
    unserialized_items = []

    for item in serialized_items:
        unserialized_items.append(
            AssetItem(
                file_path=item["file_path"],
                file_name=item["file_name"],
                type=item["type"],
            )
        )

    return unserialized_items

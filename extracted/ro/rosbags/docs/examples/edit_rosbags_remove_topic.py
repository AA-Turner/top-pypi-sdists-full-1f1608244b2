"""Example: Remove topic."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rosbags.rosbag2 import Reader, Writer
from rosbags.typesys.stores import Stores, get_typestore

if TYPE_CHECKING:
    from pathlib import Path

    from rosbags.interfaces import ConnectionExtRosbag2


def remove_topic(src: Path, dst: Path, topic: str) -> None:
    """Remove topic from rosbag2.

    Args:
        src: Source path.
        dst: Destination path.
        topic: Name of topic to remove.

    """
    typestore = get_typestore(Stores.ROS2_FOXY)
    with Reader(src) as reader, Writer(dst) as writer:
        conn_map = {}
        for conn in reader.connections:
            if conn.topic == topic:
                continue
            ext = cast('ConnectionExtRosbag2', conn.ext)
            conn_map[conn.id] = writer.add_connection(
                conn.topic,
                conn.msgtype,
                typestore=typestore,
                serialization_format=ext.serialization_format,
                offered_qos_profiles=ext.offered_qos_profiles,
            )

        rconns = [reader.connections[x] for x in conn_map]
        for conn, timestamp, data in reader.messages(connections=rconns):
            writer.write(conn_map[conn.id], timestamp, data)

from __future__ import annotations

from typing import TYPE_CHECKING

from dissect.util.ts import uuid1timestamp

from dissect.shellitem.lnk import Lnk, c_lnk

if TYPE_CHECKING:
    from pathlib import Path


def test_xp_custom_destination_remote_lnk_file(xp_modified_remote_lnk_file: Path) -> None:
    # The first 16 bytes contain the LNK GUID a to simulate a Jumplist CustomDestination file
    fh = xp_modified_remote_lnk_file.open("rb")
    fh.seek(16)

    lnk_file = Lnk(fh)

    assert lnk_file.link_header.header_size == 0x4C
    assert str(lnk_file.clsid) == "00021401-0000-0000-c000-000000000046"


def test_xp_remote_lnk_file(xp_remote_lnk_file: Path) -> None:
    fh = xp_remote_lnk_file.open("rb")
    lnk_file = Lnk(fh)

    assert lnk_file.link_header.header_size == 0x4C
    assert str(lnk_file.clsid) == "00021401-0000-0000-c000-000000000046"

    flags = lnk_file.flags

    assert flags & c_lnk.LINK_FLAGS.has_link_target_idlist
    idlist = lnk_file.target_idlist.idlist
    assert len(idlist.itemid_list) == 9
    assert idlist.terminalid == b"\x00\x00"
    assert all(entry.itemid_size == len(entry.dumps()) for entry in idlist.itemid_list)

    assert flags & c_lnk.LINK_FLAGS.has_link_info
    link_info = lnk_file.linkinfo.link_info
    link_info_flags = link_info.link_info_flags
    assert link_info_flags & c_lnk.LINK_INFO_FLAGS.volumeid_and_local_basepath == 0
    assert link_info_flags & c_lnk.LINK_INFO_FLAGS.common_network_relative_link_and_pathsuffix

    common_network_relative_link = lnk_file.linkinfo.common_network_relative_link
    assert (
        common_network_relative_link.common_network_relative_link_flags
        & c_lnk.COMMON_NETWORK_RELATIVE_LINK_FLAGS.valid_device
        == 0
    )
    assert (
        common_network_relative_link.common_network_relative_link_flags
        & c_lnk.COMMON_NETWORK_RELATIVE_LINK_FLAGS.valid_net_type
    )
    assert common_network_relative_link.net_name_offset == 0x14
    assert common_network_relative_link.device_name_offset == 0x0
    assert common_network_relative_link.device_name.device_name == b""
    assert common_network_relative_link.net_provider_type == 0x20000
    assert common_network_relative_link.net_name == b"\\\\ALS-FICHIERS3\\QUALIT\xc9"
    assert link_info.common_path_suffix == b"Archives\\M\xe9thodologie WAS\\Norme de d\xe9veloppement JAVA.doc"

    assert flags & c_lnk.LINK_FLAGS.has_working_dir
    assert len(lnk_file.stringdata.string_data) == 1
    working_dir = lnk_file.stringdata.string_data["working_dir"]
    assert working_dir.character_count == 0x62
    assert working_dir.string == "\\\\als-fichiers3\\Qualité\\Archives\\Méthodologie WAS"
    assert len(working_dir.string) == working_dir.character_count / 2  # extra 0x00 bytes are decoded away.

    tracker_props = lnk_file.extradata.extradata["TRACKER_PROPS"]
    assert tracker_props.length == 0x58
    assert tracker_props.version == 0
    assert tracker_props.machine_id == b"als-fichiers3\x00\x00\x00"
    assert str(tracker_props.file_droid) == "ea461b34-9877-11da-80bd-000f1ff7c0dc"
    assert str(tracker_props.file_droid_birth) == "ea461b34-9877-11da-80bd-000f1ff7c0dc"
    assert uuid1timestamp(tracker_props.file_droid.time).ctime() == "Wed Feb  8 07:52:55 2006"


def test_xp_remote_lnk_dir(xp_remote_lnk_dir: Path) -> None:
    fh = xp_remote_lnk_dir.open("rb")
    lnk_file = Lnk(fh)

    assert lnk_file.link_header.header_size == 0x4C
    assert str(lnk_file.clsid) == "00021401-0000-0000-c000-000000000046"

    flags = lnk_file.flags

    assert flags & c_lnk.LINK_FLAGS.has_link_target_idlist
    idlist = lnk_file.target_idlist.idlist
    assert len(idlist.itemid_list) == 7
    assert idlist.terminalid == b"\x00\x00"
    assert all(entry.itemid_size == len(entry.dumps()) for entry in idlist.itemid_list)

    assert flags & c_lnk.LINK_FLAGS.has_link_info
    link_info = lnk_file.linkinfo.link_info
    link_info_flags = link_info.link_info_flags
    assert link_info_flags & c_lnk.LINK_INFO_FLAGS.volumeid_and_local_basepath == 0
    assert link_info_flags & c_lnk.LINK_INFO_FLAGS.common_network_relative_link_and_pathsuffix

    common_network_relative_link = lnk_file.linkinfo.common_network_relative_link
    assert (
        common_network_relative_link.common_network_relative_link_flags
        & c_lnk.COMMON_NETWORK_RELATIVE_LINK_FLAGS.valid_device
        == 0
    )
    assert (
        common_network_relative_link.common_network_relative_link_flags
        & c_lnk.COMMON_NETWORK_RELATIVE_LINK_FLAGS.valid_net_type
    )

    assert common_network_relative_link.net_name_offset == 0x14
    assert common_network_relative_link.device_name_offset == 0x0
    assert common_network_relative_link.device_name.device_name == b""
    assert common_network_relative_link.net_provider_type == 0x20000
    assert common_network_relative_link.net_name == b"\\\\ALS-FICHIERS3\\QUALIT\xc9"
    assert link_info.common_path_suffix == b"GMAldheris"

    tracker_props = lnk_file.extradata.extradata["TRACKER_PROPS"]
    assert tracker_props.length == 0x58
    assert tracker_props.version == 0
    assert tracker_props.machine_id == b"als-fichiers3\x00\x00\x00"
    assert str(tracker_props.file_droid) == "8ab7e0c5-75c8-11de-b8c9-000f1ff7c0dd"
    assert str(tracker_props.file_droid_birth) == "8ab7e0c5-75c8-11de-b8c9-000f1ff7c0dd"
    assert uuid1timestamp(tracker_props.file_droid.time).ctime() == "Tue Jul 21 07:31:44 2009"


def test_win7_local_lnk_dir(win7_local_lnk_dir: Path) -> None:
    fh = win7_local_lnk_dir.open("rb")
    lnk_file = Lnk(fh)

    assert lnk_file.link_header.header_size == 0x4C
    assert str(lnk_file.clsid) == "00021401-0000-0000-c000-000000000046"

    flags = lnk_file.flags

    assert flags & c_lnk.LINK_FLAGS.has_link_target_idlist
    idlist = lnk_file.target_idlist.idlist
    assert len(idlist.itemid_list) == 4
    assert idlist.terminalid == b"\x00\x00"
    assert all(entry.itemid_size == len(entry.dumps()) for entry in idlist.itemid_list)

    assert flags & c_lnk.LINK_FLAGS.has_link_info
    link_info = lnk_file.linkinfo.link_info
    link_info_flags = link_info.link_info_flags
    assert link_info_flags & c_lnk.LINK_INFO_FLAGS.volumeid_and_local_basepath
    assert link_info_flags & c_lnk.LINK_INFO_FLAGS.common_network_relative_link_and_pathsuffix
    assert link_info.local_base_path == b"C:\\Users\\"

    volumeid = lnk_file.linkinfo.volumeid
    assert volumeid.drive_type == 0x3
    assert volumeid.drive_serial_number == 0x502E1A8A
    assert volumeid.volume_label_offset == 0x10
    assert volumeid.data == b"SSD-WIN7\x00"

    common_network_relative_link = lnk_file.linkinfo.common_network_relative_link
    assert (
        common_network_relative_link.common_network_relative_link_flags
        & c_lnk.COMMON_NETWORK_RELATIVE_LINK_FLAGS.valid_device
        == 0
    )
    assert (
        common_network_relative_link.common_network_relative_link_flags
        & c_lnk.COMMON_NETWORK_RELATIVE_LINK_FLAGS.valid_net_type
    )

    assert common_network_relative_link.net_name_offset == 0x14
    assert common_network_relative_link.device_name_offset == 0x0
    assert common_network_relative_link.device_name.device_name == b""
    assert common_network_relative_link.net_provider_type == 0x20000
    assert common_network_relative_link.net_name == b"\\\\NETBOOK\\Users"

    assert flags & c_lnk.LINK_FLAGS.has_relative_path
    assert lnk_file.stringdata.relative_path.character_count == 0x26
    assert lnk_file.stringdata.relative_path.string == "..\\..\\Administrator"

    tracker_props = lnk_file.extradata.extradata["TRACKER_PROPS"]
    assert tracker_props.length == 0x58
    assert tracker_props.version == 0
    assert tracker_props.machine_id == b"netbook\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    assert str(tracker_props.file_droid) == "136502ff-8c66-11df-b6eb-001377d34a59"
    assert str(tracker_props.file_droid_birth) == "136502ff-8c66-11df-b6eb-001377d34a59"
    assert uuid1timestamp(tracker_props.file_droid.time).ctime() == "Sat Jul 10 20:59:48 2010"

    property_store_props = lnk_file.extradata.extradata["PROPERTY_STORE_PROPS"]
    assert property_store_props.storage_size == 0xAC
    assert property_store_props.version == 0x53505331
    assert str(property_store_props.format_id) == "b725f130-47ef-101a-a5f1-02608c9eebac"


def test_common_path_suffix(win81_downloads_lnk_dir: Path) -> None:
    fh = win81_downloads_lnk_dir.open("rb")
    downloads = Lnk(fh)

    link_info = downloads.linkinfo.link_info
    link_info_flags = link_info.link_info_flags
    # edge-case were common_network_relative_link_and_pathsuffix indicates no common_path_suffix
    # but when reality says otherwise.
    assert link_info_flags & c_lnk.LINK_INFO_FLAGS.common_network_relative_link_and_pathsuffix == 0
    assert link_info.common_path_suffix == b""
    assert link_info.common_path_suffix.decode() == ""


def test_vista_and_above_idlist_lnk_props(vista_idlist_lnk_file: Path) -> None:
    fh = vista_idlist_lnk_file.open("rb")
    lnk_file = Lnk(fh)
    vista_props = lnk_file.extradata.extradata["VISTA_AND_ABOVE_IDLIST_PROPS"]

    assert vista_props.size == 0x62  # 98
    assert vista_props.idlist.itemid_list[0].itemid_size == 0x60  # 96
    assert len(vista_props.idlist.itemid_list[0].data) == 0x5E  # 94

import os

from dvc_data.hashfile.hash import file_md5
from dvc_data.hashfile.hash_info import HashInfo
from dvc_data.hashfile.state import State


def test_state(tmp_dir, dvc):
    tmp_dir.gen("foo", "foo content")
    path = tmp_dir / "foo"
    hash_info = HashInfo("md5", file_md5(path, dvc.fs))

    state = State(dvc.root_dir, dvc.tmp_dir, dvc.dvcignore)

    state.save(str(path), dvc.fs, hash_info)
    assert state.get(str(path), dvc.fs)[1] == hash_info

    path.unlink()
    path.write_text("1")

    assert state.get(str(path), dvc.fs) == (None, None)

    hash_info = HashInfo("md5", file_md5(path, dvc.fs))
    state.save(str(path), dvc.fs, hash_info)

    assert state.get(str(path), dvc.fs)[1] == hash_info


def test_state_overflow(tmp_dir, dvc):
    # NOTE: trying to add more entries than state can handle,
    # to see if it will clean up and vacuum successfully
    dvc.config["state"]["row_limit"] = 10

    path = tmp_dir / "dir"
    path.mkdir()
    for i in range(20):
        (path / str(i)).write_text(str(i))

    dvc.add("dir")


def mock_get_inode(inode):
    def get_inode_mocked(_):
        return inode

    return get_inode_mocked


def test_remove_links(tmp_dir, dvc):
    tmp_dir.dvc_gen({"foo": "foo_content", "bar": "bar_content"})

    assert len(dvc.state.links) == 2

    dvc.state.remove_links(["foo", "bar"], dvc.fs)

    assert len(dvc.state.links) == 0


def test_get_unused_links(tmp_dir, dvc):
    tmp_dir.dvc_gen({"foo": "foo_content", "bar": "bar_content"})

    links = [os.path.join(dvc.root_dir, link) for link in ["foo", "bar"]]
    assert set(dvc.state.get_unused_links([], dvc.fs)) == {"foo", "bar"}
    assert set(dvc.state.get_unused_links(links[:1], dvc.fs)) == {"bar"}
    assert set(dvc.state.get_unused_links(links, dvc.fs)) == set()
    assert set(
        dvc.state.get_unused_links(
            ([*links[:1], os.path.join(dvc.root_dir, "not-existing-file")]),
            dvc.fs,
        )
    ) == {"bar"}

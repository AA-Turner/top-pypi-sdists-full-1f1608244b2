from inspect_ai._cli.log import view_type_resource


def test_view_type_resource():
    ts_types = view_type_resource("log.d.ts")
    assert isinstance(ts_types, str)
    assert "automatically generated by" in ts_types

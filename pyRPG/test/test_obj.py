import pytest
from pyRPG import Obj


def test_item_creation():
    s_desc = "Short desc"
    s_name = "Short name"
    short = Obj(short_name=s_name, short_desc=s_desc)
    assert short.short_desc == s_desc
    assert short.long_desc == s_desc, "Long description should equal short description if no long description is provided."
    assert short.short_name == s_name
    assert short.long_name == s_name, "Long name should equal short name if no long name is provided."

    l_desc = "Long desc"
    l_name = "Long name"
    long = Obj(short_name=s_name, short_desc=s_desc, long_name=l_name, long_desc=l_desc)
    assert long.short_desc == s_desc
    assert long.long_desc == l_desc
    assert long.short_name == s_name
    assert long.long_name == l_name


def test_item_modification():
    s_desc = "E"
    s_name = "F"
    l_desc = "G"
    l_name = "H"
    # Set some initial values
    foo = Obj(short_name="A", short_desc="B", long_name="C", long_desc="D")
    # Then change them!
    foo.short_desc = s_desc
    foo.long_desc = l_desc
    foo.short_name = s_name
    foo.long_name = l_name

    assert foo.short_desc == s_desc
    assert foo.long_desc == l_desc
    assert foo.short_name == s_name
    assert foo.long_name == l_name


def test_item_aliases():
    foo = Obj(short_name="A", short_desc="B", long_name="C", long_desc="D")
    # Confirm that with no added aliases, `get_aliases` should just return the short_name then the long_name
    assert sorted(foo.get_aliases()) == ["A", "C"]

    foo.add_alias("Z")
    foo.add_alias("Y")
    assert sorted(foo.get_aliases()) == ["A", "C", "Y", "Z"]

    foo.remove_alias("Y")
    assert sorted(foo.get_aliases()) == ["A", "C", "Z"]


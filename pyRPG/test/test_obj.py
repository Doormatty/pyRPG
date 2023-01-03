import pytest
from pyRPG.obj import Obj


def test_item_creation():
    s_desc = "Short desc"
    l_desc = "Long desc"
    name = "Short name"
    short = Obj(name=name, short_desc=s_desc)
    assert short.short_desc == s_desc
    assert short.long_desc == s_desc, "Long description should equal short description if no long description is provided."
    assert short.name == name

    long = Obj(name=name, short_desc=s_desc, long_desc=l_desc)
    assert long.short_desc == s_desc
    assert long.long_desc == l_desc
    assert long.name == name


def test_item_modification():
    name = "D"
    s_desc = "E"
    l_desc = "F"
    # Set some initial values
    foo = Obj(name="A", short_desc="B", long_desc="C")
    # Then change them!
    foo.short_desc = s_desc
    foo.long_desc = l_desc
    foo.name = name

    assert foo.short_desc == s_desc
    assert foo.long_desc == l_desc
    assert foo.name == name


def test_item_aliases():
    foo = Obj(name="A", short_desc="B", long_desc="D")
    # Confirm that with no added aliases, `get_aliases` should just return the name
    assert sorted(foo.get_aliases()) == ["A"]

    foo.add_alias("Z")
    foo.add_alias("Y")
    assert sorted(foo.get_aliases()) == ["A", "Y", "Z"]

    foo.remove_alias("Y")
    assert sorted(foo.get_aliases()) == ["A", "Z"]

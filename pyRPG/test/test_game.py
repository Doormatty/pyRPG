import pytest
from pyRPG.player import Player
from pyRPG.room import Room
from pyRPG.obj import Obj
from pyRPG.world import World


@pytest.fixture
def basic_world():
    world = World(name='The World')
    room_one = Room(short_desc="A small white room.", long_desc="It's a small room - what more do you want from me?")
    world.add_room(room_one)
    world.start_location = room_one
    item = Obj(name="thing", short_desc="A thing", long_desc="a strange looking thing.")
    room_one.add_item(item)
    player = Player(name="Bob", location=world.start_location)
    world.add_player(player)
    return world

@pytest.fixture
def two_room_world():
    world = World(name='The World')
    room_one = Room(short_desc="A small white room.", long_desc="It's a small room - what more do you want from me?")
    room_two = Room(short_desc="A large red room.", long_desc="It's a large red room.  Your footsteps echo in the air.")
    world.add_room(room_one)
    world.add_room(room_two)
    world.start_location = room_one
    portal = Obj(name="portal", short_desc="A shimmering portal", flags="DOOR")
    item = Obj(name="thing", short_desc="A thing", long_desc="a strange looking thing.")
    room_one.add_item(item)
    room_one.add_item(portal)
    room_two.add_item(portal)
    player = Player(name="Bob", location=world.start_location)
    world.add_player(player)
    return world


def test_looking(basic_world):
    player = basic_world.players[0]
    item = basic_world.rooms[0].items[0]
    assert player.parse("look") == f"""{basic_world.rooms[0].long_desc}\n\n{basic_world.rooms[0].items[0].name}\nYou see no obvious exits..."""
    assert player.parse(f"look {item.name}") == item.long_desc
    assert player.parse(f"look at {item.name}") == item.long_desc


def test_moving(two_room_world):
    player = two_room_world.players[0]
    item = two_room_world.rooms[0].items[0]
    itemstr = "\n".join([x.name for x in two_room_world.rooms[0].items])
    assert player.parse("look") == f"""{two_room_world.rooms[0].long_desc}\n\n{itemstr}\nYou see no obvious exits..."""
    assert player.parse(f"look {item.name}") == item.long_desc
    assert player.parse(f"look at {item.name}") == item.long_desc
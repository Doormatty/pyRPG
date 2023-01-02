import pytest
from pyRPG import Player, Room, Obj, World

@pytest.fixture
def basic_world():
    world = World(name='The World')
    room = Room(short_desc="A small room.", long_desc="It's a small room - what more do you want from me?")
    item = Obj(short_name="thing", short_desc="A thing", long_desc="a strange looking thing.")
    room.add_item(item)
    world.add_room(room)
    world.start_location = room
    player = Player(name="Bob", location=world.start_location)
    world.add_player(player)
    return world

def test_looking(basic_world):
    player = basic_world.players[0]
    assert player.parse("look") == f"""{basic_world.rooms[0].long_desc}\n\n{basic_world.rooms[0].items[0].short_name}\nYou see no obvious exits..."""
    assert player.parse("look thing") == "a strange looking thing."
    assert player.parse("look at thing")=="a strange looking thing."



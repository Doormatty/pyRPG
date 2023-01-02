from player import Player
from room import Room
from obj import Obj


def game_init():
    room = Room(short_desc="A small room.", long_desc="It's a small room - what more do you want from me?")
    room.add_item(Obj(short_name="thing", short_desc="A thing", long_desc="a strange looking thing."))
    player = Player(name="Bob", location=room)
    print(player.parse("look"))
    #print(player.parse("look at thing"))


if __name__ == '__main__':
    game_init()

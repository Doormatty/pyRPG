from pyRPG.player import Player
from pyRPG.room import Room
from typing import Union


class World:

    def __init__(self, name):
        self.name = name
        self.players = []
        self.rooms = []
        self.start_location = None

    def add_player(self, player: Player) -> None:
        if player not in self.players:
            self.players.append(player)
            player.location = self.start_location

    def remove_player(self, player: Player) -> None:
        if player in self.players:
            self.players.remove(player)

    def add_room(self, room: Union[Room | list[Room]]) -> None:
        if isinstance(room, Room):
            room = [room]
        for rm in room:
            if rm not in self.rooms:
                self.rooms.append(rm)

    def remove_room(self, room: Room) -> None:
        if room in self.rooms:
            self.rooms.remove(room)

    def list_all_rooms(self) -> list[...]:
        for room in self.rooms:
            print(f"ID: {room.id} Short description: {room.short_desc}")

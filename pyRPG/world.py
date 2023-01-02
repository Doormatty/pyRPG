from pyRPG import Player, Room

class World:

    def __init__(self, name):
        self.name = name
        self.players=[]
        self.rooms=[]
        start_location=None

    def add_player(self, player: Player):
        if player not in self.players:
            self.players.append(player)

    def remove_player(self, player: Player):
        if player in self.players:
            self.players.remove(player)

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def remove_room(self, room: Room):
        if room in self.rooms:
            self.rooms.remove(room)

    def list_all_rooms(self):
        for room in self.rooms:
            print(f"ID: {room.id} Short description: {room.short_desc}")
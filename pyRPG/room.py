from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyRPG.obj import Obj
    from pyRPG.mob import Mob
from itertools import chain, count

try:
    from rich import print
except ImportError:
    pass


class Room:
    id_iter = count()

    def __init__(self, short_desc, long_desc=None):
        self.id = next(self.id_iter)
        self.exits = []
        self.mobs = []
        self.items = []
        self.players = []
        self.long_desc = long_desc if long_desc is not None else short_desc
        self.short_desc = short_desc

    def look(self):
        # Look at the room
        retval = f'{self.long_desc}\n\n'
        # Look at the items
        for item in self.get_items_and_mobs():
            retval += f'{item.name}\n'

        # Look at the exits
        if self.exits:
            retval += f'You see the following exits: [{[x for x in self.exits]}]'
        else:
            retval += f'You see no obvious exits...'
        return retval

    def get_items_and_mobs(self):
        for obj in chain.from_iterable((self.items, self.mobs)):
            yield obj

    def broadcast(self, msg):
        for player in self.players:
            player.send_msg_to(msg)

    def _on_exit(self):
        """Call the _on_exit method on each mob and item in the room"""
        for item in self.get_items_and_mobs():
            # if it has an "_on_exit" method
            if getattr(item, "_on_exit", None) is not None:
                item._on_exit()

    def _on_enter(self):
        """Call the _on_enter method on each mob and item in the room"""
        for item in self.get_items_and_mobs():
            # if it has an "_on_enter" method
            if getattr(item, "_on_enter", None) is not None:
                item._on_enter()

    def add_item(self, item: Obj):
        self.items.append(item)
        item.rooms.append(self)

    def remove_item(self, item: Obj):
        self.items.remove(item)
        item.rooms.remove(self)

    def add_mob(self, mob: Mob):
        self.mobs.append(mob)
        mob.room = self

    def remove_mob(self, mob: Mob):
        self.mobs.remove(mob)
        mob.room = None

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyRPG.obj import Obj
    from pyRPG.player import Player


class Parser:

    def __init__(self):
        pass

    @staticmethod
    def parse(player: Player, token_str: str):
        if token_str:
            token_list = token_str.strip().split(' ')
        else:
            return None

        verb = token_list.pop(0).upper()
        if verb in ("LOOK", "L"):
            # LOOK|L   (Look at the player's current room)
            if len(token_list) == 0:
                return {"obj": player.location,
                        "verb": "LOOK"}
            # LOOK|L AT <ITEM>
            elif len(token_list) > 1 and token_list[0].upper() == "AT":
                token_list.pop(0)
            # At this point, token_list should only contain the name of the item
            item = "".join(token_list)
            # Scan over all items in inventory and room, checking for any item that has a descriptor that matches
            obj = Parser.obj_matcher(player, item)
            if obj is None:
                return {"error": f"Could not find anything called '{item}' to look at."}
            else:
                return {"obj": obj,
                        "verb": verb.upper()}
        else:
            return {"error": f"I don't know how to '{token_str}'"}

    @staticmethod
    def obj_matcher(player: Player, name: str) -> Obj:
        # Scan over all items in inventory and room, checking for any item that has a descriptor that matches
        for obj in player.location.get_items_and_mobs():
            for alias in obj.get_aliases():
                if name.lower() == alias.lower():
                    return obj

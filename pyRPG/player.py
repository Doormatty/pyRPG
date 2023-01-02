from pyRPG import Room, Obj


class Player:

    def __init__(self, name, location=None):
        self.name: str = name
        self.location: Room = location
        self.inventory: list[Obj] = []

    def send_msg_to(self, msg: str):
        print(msg)

    def obj_matcher(self, name: str) -> Obj:
        # Scan over all items in inventory and room, checking for any item that has a descriptor that matches
        for obj in self.location.get_items_and_mobs():
            for alias in obj.get_aliases():
                if name.lower() == alias.lower():
                    return obj

    def parse(self, token_str: str):
        if token_str:
            token_list = token_str.strip().split(' ')
        else:
            return None

        verb = token_list.pop(0).upper()
        if verb in ("LOOK", "L"):
            # LOOK|L   (Look at the player's current room)
            if len(token_list) == 0:
                return self.location.look()
            # LOOK|L AT <ITEM>
            elif len(token_list) > 1 and token_list[0].upper() == "AT":
                token_list.pop(0)
            # At this point, token_list should only contain the name of the item
            item = "".join(token_list)
            # Scan over all items in inventory and room, checking for any item that has a descriptor that matches
            obj = self.obj_matcher(item)
            if obj is None:
                return f"Could not find anything called '{item}' to look at."
            else:
                return obj.long_desc
        else:
            return f"I don't know how to '{token_str}'"

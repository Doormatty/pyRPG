from typing import Union
from pyRPG.player import Player

try:
    from rich import print
except ImportError:
    pass


class Obj:
    flag_types = ("OPENABLE", "CONTAINER", "EXIT", "HIDDENEXIT", "ITEM", "WEAPON", "ARMOR")

    def __init__(self, name: str, short_desc: str, aliases: list[str] = None, long_desc: str = None, flags: Union[list, str] = None):
        # Set the name and descriptions
        self.name: str = name
        self._short_desc: str = short_desc
        self._long_desc: str = long_desc

        self.flags: set[str] = set()

        if flags:
            if isinstance(flags, str):
                self.flags.add(flags)
            else:
                for flag in flags:
                    self.flags.add(flag)

        self.attributes = dict()
        self.verbs = dict()
        self.actions = dict()

        self.rooms = list()

        # Set aliases if the item has any
        self.aliases = [x for x in aliases] if aliases else []

    @property
    def short_desc(self) -> str:
        """The description returned when looking at a room that contains the object"""
        return self._short_desc

    @short_desc.setter
    def short_desc(self, value: str) -> None:
        self._short_desc = value

    @property
    def long_desc(self) -> str:
        """The description returned when looking at the item directly.  If not set, returns the short_desc"""
        if self._long_desc:
            return self._long_desc
        else:
            return self._short_desc

    @long_desc.setter
    def long_desc(self, value: str) -> None:
        self._long_desc = value

    def add_alias(self, alias: str) -> None:
        """Adds a new alias to the item's list of aliases"""
        self.aliases.append(alias)

    def remove_alias(self, alias: str) -> None:
        """Removes an existing alias from an item"""
        self.aliases.remove(alias)

    def get_aliases(self) -> list[str]:
        """Returns a list of the item's aliases AND the item's actual name"""
        if self.aliases:
            # If we have aliases, include them
            retval = self.aliases
        else:
            retval = []
        # Add the actual name to the list of aliases
        if self.name not in retval:
            retval.append(self.name)
        return retval

    def set_flag(self, flag: str) -> None:
        if flag.upper() in self.flag_types:
            self.flags.add(flag.upper())
        else:
            Exception(f"No such flag type as {flag.upper()}")

    def unset_flag(self, flag: str) -> None:
        if flag.upper() in self.flag_types:
            self.flags.remove(flag.upper())
        else:
            Exception(f"No such flag type as {flag.upper()}")

    def verb(self, player: Player, verb: str):
        # Handle builtin verbs
        if verb.upper() == "LOOK":
            return self.long_desc

        # Now check to see if it matches any custom verbs added to the object
        if verb.upper() not in self.verbs.keys():
            return f"I don't know how to {verb} {self.name}."
        else:
            result = self.verbs[verb.upper()]

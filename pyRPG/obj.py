try:
    from rich import print
except ImportError:
    pass


class Obj:
    flag_types = ("DOOR", "ITEM", "WEAPON", "ARMOR")

    def __init__(self, short_name: str, short_desc: str, aliases: list[str] = None, long_name: str = None, long_desc: str = None):
        # Set the long and short names and descriptions
        self._short_name: str = short_name
        self._short_desc: str = short_desc

        self._long_name: str = long_name
        self._long_desc: str = long_desc

        self.flags: set[str] = set()

        self.verbs = {"open": {'self': 'you open the door, and walk through',
                               'room': '{}'}
                      }

        # Set aliases if the item has any
        if aliases:
            self.aliases = [x for x in aliases]
        else:
            self.aliases = []

    @property
    def short_name(self):
        """The name returned when looking at a room that contains the object"""
        return self._short_name

    @short_name.setter
    def short_name(self, value: str):
        self._short_name = value

    @property
    def long_name(self):
        """The name returned when looking at the object directly.  If not set, returns the short_name"""
        if self._long_name:
            return self._long_name
        else:
            return self._short_name

    @long_name.setter
    def long_name(self, value: str):
        self._long_name = value

    @property
    def short_desc(self):
        """The description returned when looking at a room that contains the object"""
        return self._short_desc

    @short_desc.setter
    def short_desc(self, value: str):
        self._short_desc = value

    @property
    def long_desc(self):
        """The description returned when looking at the item directly.  If not set, returns the short_desc"""
        if self._long_desc:
            return self._long_desc
        else:
            return self._short_desc

    @long_desc.setter
    def long_desc(self, value: str):
        self._long_desc = value

    def add_alias(self, alias: str):
        """Adds a new alias to the item's alias list"""
        self.aliases.append(alias)

    def remove_alias(self, alias: str):
        """Removes an existing alias from an item"""
        self.aliases.remove(alias)

    def get_aliases(self) -> list[str]:
        """Returns a list of the item's aliases AND actual names"""
        if self.aliases:
            # If we have aliases, include them
            retval = self.aliases
        else:
            retval = []
        # Add the long and short name to the list of aliases
        if self.short_name not in retval:
            retval.append(self.short_name)
        if self.long_name not in retval:
            retval.append(self.long_name)
        return retval

    def set_flag(self, flag):
        if flag.upper() in self.flag_types:
            self.flags += flag.upper()
        else:
            Exception(f"No such flag type as {flag.upper()}")

    def unset_flag(self, flag):
        if flag.upper() in self.flag_types:
            self.flags -= flag.upper()
        else:
            Exception(f"No such flag type as {flag.upper()}")

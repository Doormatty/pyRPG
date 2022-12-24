try:
    from rich import print
except ImportError:
    pass


class Item:

    def __init__(self, short_name, short_desc, aliases=None, long_name=None, long_desc=None):
        # Set the long and short names and descriptions
        self._short_name = short_name
        self._short_desc = short_desc

        self._long_name = long_name
        self._long_desc = long_desc

        # Set aliases if the item has any
        self.aliases = (x for x in aliases)
    @property
    def short_name(self):
        """this name is returned when looking at a room that contains the object"""
        return self._short_name

    @property
    def long_name(self):
        """this name is returned when looking at the object directly.  If not set, returns the short_name"""
        if self._long_name:
            return self._long_name
        else:
            return self._short_name

    @property
    def short_desc(self):
        """this description is returned when looking at a room that contains the object"""
        return self._short_desc

    @property
    def long_desc(self):
        """this description is returned when looking at the item directly.  If not set, returns the short_desc"""
        if self._long_desc:
            return self._long_desc
        else:
            return self._short_desc

    def _get_aliases(self):






try:
    from rich import print
except ImportError:
    pass


class Room:

    def __init__(self):
        self.exits = []
        self.mobs = []
        self.items = dict() # Tuple of aliases pointing to items
        self.long_desc= ''
        self.short_desc = ''

    def look(self):
        # Look at the room
        retval = f'{self.long_desc}\n\n'
        # Look at the items
        for item in self.items:
            retval += f'{item.long_name}\n'

        # # Look at the mobs
        # for mob in self.mobs:
        #     retval += f'{}\n'

        # Look at the exits
        retval += f'\n You see the following exits: [{[x for x in self.exits]}]'

    def _on_exit(self):
        # Call the _on_exit method for each mob and item in the room
        pass

    def _on_enter(self):
        # Display the short_description
        # Call the _on_enter method for each mob and item in the room
        pass

    def add_exit(self, direction, room, short_desc, long_desc=None):
        pass

    def add_item(self, item):
        self.items[()]

    def add_mob(self, mob):
        self.mobs.append(mob)

class Mob:
    possible_flags = ('LISTENING',  # If set, allows the mob to react to things said in the same room as it, or to it directly
                      'WATCHING',  # If set, allows the mob to react to things done in the same room as it, or to it directly
                      'FIGHTABLE')  # If set, allows you to fight the mob

    def __init__(self, short_desc=None, long_desc=None, flags=None):
        self.loot_table = dict()
        self.long_desc = ''
        self.short_desc = ''
        self.flags = set()
        self.setflags(flags)

        self.room = None

    def setflags(self, flags_to_set):
        for flag in flags_to_set:
            if flag.upper() in self.possible_flags:
                self.flags.add(flag)

    def look(self):
        # Look at the mob
        return self.long_desc

    def _on_exit(self, thing):
        # Called whenever something leaves a room
        pass

    def _on_enter(self, thing):
        # Called whenever something enters a room
        pass

    def _on_speak(self, thing, speech):
        # Called whenever something talks in a room containing this mob
        pass

    def _on_speak_to(self, thing, speech):
        # Called whenever something talks directly to this mob
        pass

    def _on_action(self, thing, action):
        # Called whenever something performs an action in a room containing this mob
        pass

    def _on_death(self, thing):
        # Called whenever the mob dies at something's hands
        pass

    def _on_recieve_item(self, thing, item):
        # Called whenever the mob is given a thing by something
        pass

    def add_loot(self, item, rarity):
        # Adds an item to the loot table
        self.loot_table[rarity] = item

    def roll_for_loot(self, num_rolls):
        # Roll against the loot table num_rolls times
        pass

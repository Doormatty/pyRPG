class GM:

    def __init__(self):
        self.world = []
        self.start_room = None
        self.current_room = self.start_room
        self.run_game()

    def run_game(self):
        while True:
            # Get Input
            # Parse Input
            pass

    def get_input(self):
        pass

    def fight(self, mob):
        # Causes a fight between the player and the mob in question
        pass

    def enter_room(self):
        pass

    def exit_room(self):
        pass

    def parser(self, tokens):
        if tokens:
            tokens = tokens.strip().split(' ')
        else:
            return None

        if tokens[0].upper() in ("LOOK", "L"):
            if len(tokens) == 1:
                # LOOK
                return self.current_room.look()
            elif len(tokens) >= 3 and tokens[1].upper() == "AT":
                # LOOK AT <ITEM>
                item = "".join(tokens[2:])
            else:
                # LOOK <ITEM>
                item = "".join(tokens[1:])
            if item:
                # Scan over all items in inventory and room, checking for any item that has a descriptor that matches
                pass


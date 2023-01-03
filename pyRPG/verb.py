class Verb:

    def __init__(self):
        self.speak = {"self": "", "room": "", "world": ""}
        self.do = {"self": None, "room": None, "world": None}

    def set_speak(self, kind, text):
        if kind.lower() in self.speak.keys():
            self.speak[kind.lower()]=text

    def set_do(self, kind, func):
        if kind.lower() in self.do.keys():
            self.do[kind.lower()]=func

    
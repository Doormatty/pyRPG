from __future__ import annotations
from typing import TYPE_CHECKING, Union
from pyRPG.parser import Parser

if TYPE_CHECKING:
    from pyRPG.obj import Obj

from pyRPG.room import Room


class Player:

    def __init__(self, name, location=None):
        self.name: str = name
        self.location: Room = location
        self.inventory: list[Obj] = []

    def send_msg_to(self, msg: str):
        print(msg)

    def parse(self, text):
        result = Parser.parse(player=self, token_str=text)
        if result.get("error",None) is not None:
            return result["error"]
        obj: Union[Obj, Room] = result["obj"]
        verb = result["verb"]
        if isinstance(obj, Room) and verb.upper() == "LOOK":
            return obj.look()
        return obj.verb(self,verb)


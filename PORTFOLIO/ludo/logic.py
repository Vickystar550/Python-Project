from itertools import cycle
from typing import NamedTuple


# class Player(NamedTuple):
#     color: str
#     dice: list
#
#
# DEFAULT_PLAYERS = (Player(color='green', dice=[1, 2, 3, 4, 5, 6]), Player(color='red', dice=[1, 2, 3, 4, 5, 6]),
#                    Player(color='yellow', dice=[1, 2, 3, 4, 5, 6]), Player(color='blue', dice=[1, 2, 3, 4, 5, 6]))

class Player:
    def __init__(self, color):
        self.color = color
        self.dice = [1, 2, 3, 4, 5, 6]


class Logic:
    def __init__(self, players: list):
        self.players = players

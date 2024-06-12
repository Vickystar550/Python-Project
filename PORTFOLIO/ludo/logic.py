from itertools import cycle
from typing import NamedTuple


class Player(NamedTuple):
    color: str


DEFAULT_PLAYERS = (Player(color='green'), Player(color='red'), Player(color='yellow'), Player(color='blue'))


class Logic:
    def __init__(self):
        pass

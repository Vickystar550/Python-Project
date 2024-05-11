import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle


class Player(NamedTuple):
    label: str
    color: str


class Move(NamedTuple):
    row: int
    col: int
    label: str = ''


BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    (Player(label='X', color='blue'),
     Player(label='O', color='green'))
)


class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self.players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self.players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self.setup_board()

    def setup_board(self):
        """set up a virtual board"""
        # get the current / possible moves
        self._current_moves = [[Move(row, col) for col in range(self.board_size)] for row in range(self.board_size)]
        print('current moves', self._current_moves)
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        rows = [[(move.row, move.col) for move in row] for row in self._current_moves]
        print('rows', rows)
        columns = [list(col) for col in zip(*rows)]
        print('columns', columns)
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        print('first diagonal', first_diagonal)
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        print('second diagonal', second_diagonal)
        print(rows + columns + [first_diagonal, second_diagonal])
        return rows + columns + [first_diagonal, second_diagonal]


game = TicTacToeGame()
print(game._current_moves)

from typing import NamedTuple
from itertools import cycle
import random


class Player(NamedTuple):
    """define a player by color"""
    color: str


class Pieces:
    """represent the chess game piece"""
    def __init__(self, **kwargs):
        self.row: int = kwargs.get('row')
        self.col: int = kwargs.get('col')
        self.name: str = kwargs.get('name')
        self.class_name = kwargs.get('class_name')
        self.color: str = kwargs.get('color')


class Moves:
    """describe each cell as an object which is also a possible move"""
    def __init__(self, **kwargs):
        self.row: int = kwargs.get('row')
        self.col: int = kwargs.get('col')
        self.player: Player = kwargs.get('player')
        self.piece: Pieces = kwargs.get('piece')


BOARD_SIZE = 8
DEFAULT_PLAYERS = (
    (Player(color='white'), Player(color='black'))
)


class GameLogic:
    """models the chess logic"""
    def __init__(self):
        self.players = cycle(DEFAULT_PLAYERS)
        self.board_size = BOARD_SIZE
        self.current_player = next(self.players)
        self.virtual_moves = {}  # hold all unoccupied moves objects
        self.pieces = {}  # holds all the pieces
        self.current_piece = None

        self.virtual_board()
        self.occupied_moves = {}  # holds all the moves that are being occupied
        self.initialize_piece_and_moves()   # initialize the virtual board with pieces

    def virtual_board(self):
        """set a virtual board make of all cells or moves object"""
        self.virtual_moves = {(row, col): Moves(row=row, col=col, piece=None, player=None) for col in
                              range(self.board_size) for row in range(self.board_size)}

    def get_piece(self, row, col):
        """return a piece object given the coordinates"""
        return self.pieces.get((row, col))

    def initialize_piece_and_moves(self):
        """initialize all pieces and moves at start"""
        for coordinates, move in self.virtual_moves.items():
            row, col = coordinates

            # white and black pawn
            if row == 1:
                self.pieces[coordinates] = Pieces(row=row, col=col, name='BPawn', class_name='Pawn', color='black')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces.get(coordinates)

            elif row == 6:
                self.pieces[coordinates] = Pieces(row=row, col=col, name='WPawn', class_name='Pawn', color='white')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

            # white and black rook
            elif row == 0 and (col == 0 or col == 7):
                self.pieces[coordinates] = Pieces(row=row, col=col, name='BRook', class_name='Rook', color='black')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

            elif row == 7 and (col == 0 or col == 7):
                self.pieces[coordinates] = Pieces(row=row, col=col, name='WRook', class_name='Rook', color='white')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

            # black knight left
            elif row == 0 and col == 1:
                self.pieces[coordinates] = Pieces(row=row, col=col, name='BKnightLeft',
                                                  class_name='Knight', color='black')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

                # black knight right
            elif row == 0 and col == 6:
                self.pieces[coordinates] = Pieces(row=row, col=col, name='BKnightRight',
                                                  class_name='Knight',  color='black')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

            # white knight left
            elif row == 7 and col == 1:
                self.pieces[coordinates] = Pieces(row=row, col=col, name='WKnightLeft',
                                                  class_name='Knight',  color='white')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

                # white knight right
            elif row == 7 and col == 6:
                self.pieces[coordinates] = Pieces(row=row, col=col, name='WKnightRight',
                                                  class_name='Knight', color='white')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

            # bishop
            elif row == 0 and (col == 2 or col == 5):
                self.pieces[coordinates] = Pieces(row=row, col=col, name='BBishop', class_name='Bishop', color='black')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

            elif row == 7 and (col == 2 or col == 5):
                self.pieces[coordinates] = Pieces(row=row, col=col, name='WBishop', class_name='Bishop', color='white')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

            # queen
            elif row == 0 and col == 3:
                self.pieces[coordinates] = Pieces(row=row, col=col, name='BQueen', class_name='Queen', color='black')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

            elif row == 7 and col == 3:
                self.pieces[coordinates] = Pieces(row=row, col=col, name='WQueen', class_name='Queen', color='white')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

            # king
            elif row == 0 and col == 4:
                self.pieces[coordinates] = Pieces(row=row, col=col, name='BKing', class_name='King', color='black')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

            elif row == 7 and col == 4:
                self.pieces[coordinates] = Pieces(row=row, col=col, name='WKing', class_name='King', color='white')
                self.occupied_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates])
                move.current_piece = self.pieces[coordinates]

    def is_valid_move(self, move: Moves, piece):
        """check if each piece move is valid"""

    def update_moves(self, row, col, **kwargs):
        """change the attribute of a move object when a move has been made from it or to it"""
        move_to_update: Moves = self.virtual_moves.get((row, col))
        move_to_update.piece = kwargs.get('piece')
        move_to_update.player = kwargs.get('player')

    def toggle_player(self):
        self.current_player = next(self.players)


class Pawn(Pieces):
    """defines the pawn class, their properties and moves"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Pawn'
        self.initial_skip = (1, 2)
        self.possible_cells = {'white': [], 'black': []}

    def create_possible_cells(self):
        if self.color == 'white':
            self.possible_cells = []
        else:
            self.possible_cells = []

    def move(self):
        pass


logic = GameLogic()

from typing import NamedTuple
from itertools import cycle
from pieces import Pieces, Pawn, Rook, Knight, Bishop, Queen, King
from typing import Union


class Player(NamedTuple):
    """define a player by color"""
    color: str


class Moves:
    """describe each cell as an object which is also a possible move"""

    def __init__(self, **kwargs):
        self.row: int = kwargs.get('row')  # move row
        self.col: int = kwargs.get('col')  # move column
        self.player: Player = kwargs.get('player')  # move current player
        self.piece: Pieces = kwargs.get('piece')  # move current associated Piece


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

        self.moving_piece: Union[Pieces, Pawn, Rook, Knight, Bishop, Queen, King] = None
        self.piece_to_be_remove: Union[Pieces, Pawn, Rook, Knight, Bishop, Queen, King] = None

        self.new_piece = {}

        self.move_from = None
        self.move_to = None

        self.virtual_board()
        self.initialize_piece_and_moves()  # initialize the virtual board with pieces

    def virtual_board(self):
        """set a virtual board make of all cells or moves object"""
        self.virtual_moves = {(row, col): Moves(row=row, col=col, piece=None, player=None) for col in
                              range(self.board_size) for row in range(self.board_size)}

    def get_piece(self, row, col):
        """return a piece object given the coordinates"""
        return self.pieces.get((row, col))

    def create_piece(self, row: int, col: int, which: str, color: str):
        """given a coordinate, create a new chess piece of choice at the location for pawn promotion"""
        new_piece: Union[Rook, Knight, Bishop, Queen] = None

        new_piece_name = f'{color.upper()[:1]}{which.title()}'

        if which.lower() == 'rook':
            new_piece = Rook(row=row, col=col, name=new_piece_name, color=color.lower(), type_='inverted')

        elif which.lower() == 'bishop':
            new_piece = Bishop(row=row, col=col, name=new_piece_name, color=color.lower(), type_='inverted')

        elif which.lower() == 'knight':
            if (row, col) in [(0, 0), (0, 1), (0, 2), (0, 3)] or (row, col) in [(7, 0), (7, 1), (7, 2), (7, 3)]:
                new_piece_name = new_piece_name + 'Left'

            elif (row, col) in [(0, 4), (0, 5), (0, 6), (0, 7)] or (row, col) in [(7, 4), (7, 5), (7, 6), (7, 7)]:
                new_piece_name = new_piece_name + 'Right'

            new_piece = Knight(row=row, col=col, name=new_piece_name, color=color.lower(), type_='inverted')

        elif which.lower() == 'queen':
            new_piece = Queen(row=row, col=col, name=new_piece_name, color=color.lower(), type_='inverted')

        # adding the new piece to store:
        self.new_piece[(row, col)] = new_piece
        self.pieces[(row, col)] = new_piece

        # return new_piece object
        return new_piece

    def initialize_piece_and_moves(self):
        """initialize all pieces and moves at start"""
        for coordinates in self.virtual_moves.keys():
            row, col = coordinates

            # white and black pawn
            if row == 1:
                self.pieces[coordinates] = Pawn(row=row, col=col, name='BPawn', color='black', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            elif row == 6:
                self.pieces[coordinates] = Pawn(row=row, col=col, name='WPawn', color='white', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            # white and black rook
            elif row == 0 and (col == 0 or col == 7):
                self.pieces[coordinates] = Rook(row=row, col=col, name='BRook',
                                                class_name='Rook', color='black', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            elif row == 7 and (col == 0 or col == 7):
                self.pieces[coordinates] = Rook(row=row, col=col, name='WRook',
                                                class_name='Rook', color='white', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            # black knight left
            elif row == 0 and col == 1:
                self.pieces[coordinates] = Knight(row=row, col=col, name='BKnightLeft', class_name='Knight',
                                                  color='black', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

                # black knight right
            elif row == 0 and col == 6:
                self.pieces[coordinates] = Knight(row=row, col=col, name='BKnightRight', class_name='Knight',
                                                  color='black', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            # white knight left
            elif row == 7 and col == 1:
                self.pieces[coordinates] = Knight(row=row, col=col, name='WKnightLeft', class_name='Knight',
                                                  color='white', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

                # white knight right
            elif row == 7 and col == 6:
                self.pieces[coordinates] = Knight(row=row, col=col, name='WKnightRight', class_name='Knight',
                                                  color='white', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            # bishop
            elif row == 0 and (col == 2 or col == 5):
                self.pieces[coordinates] = Bishop(row=row, col=col, name='BBishop',
                                                  class_name='Bishop', color='black', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            elif row == 7 and (col == 2 or col == 5):
                self.pieces[coordinates] = Bishop(row=row, col=col, name='WBishop',
                                                  class_name='Bishop', color='white', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            # queen
            elif row == 0 and col == 3:
                self.pieces[coordinates] = Queen(row=row, col=col, name='BQueen',
                                                 class_name='Queen', color='black', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            elif row == 7 and col == 3:
                self.pieces[coordinates] = Queen(row=row, col=col, name='WQueen',
                                                 class_name='Queen', color='white', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            # king
            elif row == 0 and col == 4:
                self.pieces[coordinates] = King(row=row, col=col, name='BKing',
                                                class_name='King', color='black', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

            elif row == 7 and col == 4:
                self.pieces[coordinates] = King(row=row, col=col, name='WKing',
                                                class_name='King', color='white', type_='normal')
                self.virtual_moves[coordinates] = Moves(row=row, col=col, piece=self.pieces[coordinates], player=None)

    def update_moves(self, row, col, **kwargs):
        """change the attribute of a move object when a move has been made from it or to it"""
        move_to_update: Moves = self.virtual_moves.get((row, col))
        move_to_update.piece = kwargs.get('piece')
        move_to_update.player = kwargs.get('player')

    def toggle_player(self):
        """toggle the next player"""
        self.current_player = next(self.players)

    def validate_move(self):
        """check is a piece move is valid by returning validating string"""
        # 1. Pawn ---------------------
        if self.moving_piece.class_name == 'Pawn':
            result = self.select_piece(root=self.moving_piece, move_to=self.move_to)
            return result

        # 2. Other Pieces --------------
        elif self.moving_piece.class_name in ['Rook', 'Knight', 'Bishop', 'Queen', 'King']:
            result = self.select_piece(root=self.moving_piece, move_to=self.move_to,
                                       virtual_board=self.virtual_moves)
            return result

    def select_piece(self, root, **kwargs):
        """a universal function to select a particular piece"""
        piece: Union[Pieces, Pawn, Rook, Knight, Bishop, King] = root

        piece.move_from = piece.row, piece.col
        piece.move_to = kwargs.get('move_to')
        piece.piece_to_capture = self.piece_to_be_remove
        piece.virtual_board = kwargs.get('virtual_board')

        return piece.can_move()

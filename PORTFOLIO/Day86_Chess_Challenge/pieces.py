# PARENT CLASS FOR ALL PIECES.

class Pieces:
    """Represent the chess game piece"""

    def __init__(self, **kwargs):
        self.row: int = kwargs.get('row')  # defines where the piece is currently at
        self.col: int = kwargs.get('col')  # defines where the piece is currently at
        self.name: str = kwargs.get('name')  # the piece actual name
        self.class_name = kwargs.get('class_name')  # the piece class or family name
        self.color: str = kwargs.get('color')  # the piece associated color


# SUBCLASSES FOR EACH PIECE.

# ------------------------------------------------ 1. PAWN ----------------------------------------------
class Pawn(Pieces):
    """Defines the pawn class, their properties and moves.
        Inherit from the Pieces class"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_name = 'Pawn'
        self.white_starting_positions = {(6, c) for c in range(8)}
        self.black_starting_positions = {(1, c) for c in range(8)}

        self.move_from: tuple = None
        self.move_to: tuple = None

        self.piece_to_capture = None

        self.associated_forward_moves = []
        self.associated_prohibited_cells = []

        self.black_promotion_cells = []
        self.white_promotion_cells = []

        # initiate functions
        self.get_prohibited_cells()
        self.forward_moves()

    def get_capture_cell(self):
        """return a list of pawn possible capture cells based on it current location"""
        r, c = self.move_from
        if self.color == 'black':
            return [(r + 1, c - 1), (r + 1, c + 1)]
        else:
            return [(r - 1, c - 1), (r - 1, c + 1)]

    def get_prohibited_cells(self):
        """get the cell a pawn object is not permitted to move to while going forward
        that is backward cells"""
        if self.color == 'white':
            self.associated_prohibited_cells = {(r, c) for c in range(8) for r in range(self.row + 1, 8)}
        else:  # for black piece
            self.associated_prohibited_cells = {(r, col) for col in range(8) for r in range(self.row - 1, -1, -1)}

    def get_promotion_cells(self):
        """get the promotion cells for a pawn piece based on its current location"""
        if self.color == 'white':
            return [(0, c) for c in (self.col - 1, self.col, self.col + 1)]
        else:  # for black
            return [(7, c) for c in (self.col - 1, self.col, self.col + 1)]

    def forward_moves(self):
        """create potential forward cells which the pawn maybe permitted to move to"""
        # create a list of possible cell while moving forward
        if self.color == 'white':
            if (self.row, self.col) in self.white_starting_positions:
                self.associated_forward_moves = {(r, self.col) for r in range(self.row - 1, self.row - 3, -1)}
            else:
                self.associated_forward_moves = {(r, self.col) for r in
                                                 range(self.row - 1, self.row - 2, -1)}

        # for black:
        else:
            if (self.row, self.col) in self.black_starting_positions:
                self.associated_forward_moves = {(r, self.col) for r in range(self.row + 1, self.row + 3)}
            else:
                self.associated_forward_moves = {(r, self.col) for r in
                                                 range(self.row + 1, self.row + 2)}

        # remove items of forward_cells that are prohibited cells
        self.associated_forward_moves = [item for item in self.associated_forward_moves
                                         if item not in self.associated_prohibited_cells]

    def can_move(self):
        """check if the given coordinate is right to move this piece to"""
        self.get_prohibited_cells()
        self.forward_moves()

        # get capturing cells
        capture_cells = self.get_capture_cell()
        # get promoting cells
        promoting_cells = self.get_promotion_cells()

        # ------------------------------------------------
        if self.move_to in set(promoting_cells) and self.move_to in set(capture_cells):
            if self.piece_to_capture is None:
                return 'not capturing'  # cannot capture an empty cell
            else:
                return 'capture and promote'

        # ------------------------------------------------
        elif self.move_to in set(promoting_cells):
            if self.piece_to_capture is None:  # promote this piece
                return 'promote'
            else:
                return 'blocked'

        # --------------------------------------------------
        elif self.move_to in set(self.associated_forward_moves):
            if self.piece_to_capture is None:
                return 'forward'
            else:
                return 'blocked'  # can't move forward again because path is blocked

        # ---------------------------------------------------
        elif self.move_to in set(capture_cells):
            if self.piece_to_capture is None:
                return 'not capturing'  # cannot capture an empty cell
            else:
                return 'capturing'

        # ----------------------------------------------------
        elif self.move_to in set(self.associated_prohibited_cells):  # for known prohibited cells
            return 'prohibited'

        # ------------------------------------------
        else:  # for unknown prohibited cells
            return 'unknown'


# ----------------------------------------- 2. ROOK -------------------------------------------------------

class Rook(Pieces):
    """Defines the rook class, their properties and moves.
            Inherit from the Pieces class"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_name = 'Rook'
        self.move_from: tuple = None
        self.move_to: tuple = None
        self.piece_to_capture = None
        self.virtual_board = {}
        self.allow_skip = None

        # for castling purpose:
        self.has_move_before = False
        self.castling_range = None
        self.can_castle = False

        self.permitted_moves = {}
        self.get_permitted_moves()

    def get_permitted_moves(self):
        """Get the potential permissible cells that a rook can move to. Determine based on its current location"""
        horizontal_moves = {(self.row, c) for c in range(8)}
        vertical_moves = {(r, self.col) for r in range(8)}

        self.permitted_moves = horizontal_moves.union(vertical_moves)

    def can_move(self):
        """check if the given coordinate is right to move this piece to"""
        self.get_permitted_moves()
        self.skipping()
        self.castling()

        if self.move_to in self.castling_range and self.can_castle:
            self.can_castle = False  # off castling for this piece
            self.has_move_before = True   # change has_move_before
            return 'castle'

        elif self.move_to in self.permitted_moves:
            # check for skipping
            if self.allow_skip:
                self.has_move_before = True  # change has_move_before
                if self.piece_to_capture:   # check for capturing:
                    return 'capturing'
                else:
                    return 'forward'
            else:
                return 'prohibited'

        else:
            return 'prohibited'

    def skipping(self):
        """checks if the rook skips any piece on its way while moving horizontally or vertically"""
        horizontal_moves = [(self.row, c) for c in range(8)]
        vertical_moves = [(r, self.col) for r in range(8)]

        # horizontal skipping ------------------------------------------
        if self.move_from in horizontal_moves and self.move_to in horizontal_moves:
            from_index = horizontal_moves.index(self.move_from)
            to_index = horizontal_moves.index(self.move_to)

            if from_index < to_index:
                h1_ranges = horizontal_moves[from_index + 1: to_index]

                if not h1_ranges:
                    self.allow_skip = True
                else:
                    for e in h1_ranges:
                        result = self.virtual_board.get(e)
                        if result.piece is None:
                            self.allow_skip = True
                            continue
                        else:
                            self.allow_skip = False
                            break

            else:
                h2_ranges = horizontal_moves[from_index - 1: to_index: -1]

                if not h2_ranges:
                    self.allow_skip = True
                else:
                    for e in h2_ranges:
                        result = self.virtual_board.get(e)
                        if result.piece is None:
                            self.allow_skip = True
                            continue
                        else:
                            self.allow_skip = False
                            break

        # vertical skipping ----------------------------------
        elif self.move_from in vertical_moves and self.move_to in vertical_moves:
            from_index = vertical_moves.index(self.move_from)
            to_index = vertical_moves.index(self.move_to)

            if from_index < to_index:
                v1_ranges = vertical_moves[from_index + 1: to_index]

                print('vertical cells between from & to', v1_ranges)

                if not v1_ranges:
                    print('empty range')
                    self.allow_skip = True
                    return self.allow_skip
                else:
                    for e in v1_ranges:
                        result = self.virtual_board.get(e)
                        if result.piece is None:
                            self.allow_skip = True
                            continue
                        else:
                            self.allow_skip = False
                            break

            else:
                v2_ranges = vertical_moves[from_index - 1: to_index: -1]

                print('vertical cells between from & to', v2_ranges)

                if not v2_ranges:
                    print('empty range')
                    self.allow_skip = True
                    return self.allow_skip
                else:
                    for e in v2_ranges:
                        result = self.virtual_board.get(e)
                        if result.piece is None:
                            self.allow_skip = True
                            continue
                        else:
                            self.allow_skip = False
                            break

    def castling(self):
        """checks if castling is possible for each player"""
        if self.color == 'white':
            self.castling_range = [(7, 4), (7, 5), (7, 6), (7, 7)]
        else:
            self.castling_range = [(0, 4), (0, 5), (0, 6), (0, 7)]

        if not self.has_move_before:
            try:
                is_king0 = self.virtual_board.get(self.castling_range[0]).piece.class_name
                is_king2 = self.virtual_board.get(self.castling_range[2]).piece.class_name
            except AttributeError:
                is_king0 = self.virtual_board.get(self.castling_range[0]).piece
                is_king2 = self.virtual_board.get(self.castling_range[2]).piece

                king_in_range = is_king0 or is_king2
            else:
                king_in_range = is_king0 == 'King' or is_king2 == 'King'

            is_rook = self.virtual_board.get(self.castling_range[-1]).piece.class_name

            if king_in_range and is_rook == 'Rook':
                for coordinate in self.castling_range[1:-1]:
                    occupying_piece = self.virtual_board.get(coordinate).piece

                    if occupying_piece is None:
                        self.can_castle = True
                        continue
                    else:
                        if occupying_piece.class_name == 'King':
                            self.can_castle = True
                            continue
                        else:
                            self.can_castle = False
                            break


# ----------------------------------------- 3. KNIGHT -------------------------------------------------------

class Knight(Pieces):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_name = 'Knight'

        self.move_from: tuple = None
        self.move_to: tuple = None

        self.piece_to_capture = None
        self.virtual_board = {}

        self.permitted_moves = {}
        self.get_permitted_moves()

    def get_permitted_moves(self):
        pass

    def can_move(self):
        return 'other pieces'

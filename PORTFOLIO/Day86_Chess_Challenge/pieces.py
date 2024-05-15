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
        r, c = self.move_from
        """return a list of pawn possible capture cells based on it current location"""
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
        if self.color == 'white':
            return [(0, c) for c in (self.col - 1, self.col, self.col + 1)]
        else:  # for black
            return [(7, c) for c in (self.col - 1, self.col, self.col + 1)]

    def forward_moves(self):
        # create a list of possible cell while moving forward
        if self.color == 'white':
            if self.move_from is None or self.move_from in self.white_starting_positions:
                self.associated_forward_moves = {(r, self.col) for r in range(self.row - 1, self.row - 3, -1)}
            else:
                self.associated_forward_moves = {(r, self.col) for r in range(self.move_from[0] - 1, self.move_from[0] - 2, -1)}

        # for black:
        else:
            if self.move_from is None or self.move_from in self.black_starting_positions:
                self.associated_forward_moves = {(r, self.col) for r in range(self.row + 1, self.row + 3)}
            else:
                self.associated_forward_moves = {(r, self.col) for r in range(self.move_from[0] + 1, self.move_from[0] + 2)}

        # remove items of forward_cells that are prohibited cells
        self.associated_forward_moves = [item for item in self.associated_forward_moves
                                         if item not in self.associated_prohibited_cells]

    def can_move(self):
        """check if the given coordinate is right to move the piece to"""
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

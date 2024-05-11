class Pieces:
    """Represent the chess game piece"""

    def __init__(self, **kwargs):
        self.row: int = kwargs.get('row')  # defines where the piece is currently at
        self.col: int = kwargs.get('col')  # defines where the piece is currently at
        self.name: str = kwargs.get('name')  # the piece actual name
        self.class_name = kwargs.get('class_name')  # the piece class or family name
        self.color: str = kwargs.get('color')  # the piece associated color


class Pawn(Pieces):
    """Defines the pawn class, their properties and moves.
        Inherit from the Pieces class"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_name = 'Pawn'

        self.black_promotion_cells = [(7, c) for c in range(8)]
        self.black_normal_cells = [(r, c) for c in range(8) for r in range(2, 7)]

        self.white_promotion_cells = [(0, c) for c in range(8)]
        self.white_normal_cells = [(r, c) for c in range(8) for r in range(5, 0, -1)]

        self.potential_cells = {}
        self.skip = False
        self.initial_skip = self.initial_permissible_skip_cells()

    def get_capture_cell(self):
        """return a list of pawn possible capture cells based on it current location"""
        if self.color == 'black':
            return [(self.row + 1, self.col - 1), (self.row + 1, self.col + 1)]
        else:
            return [(self.row - 1, self.col - 1), (self.row - 1, self.col + 1)]

    def get_prohibited_cells(self):
        """get the cell a pawn object is not permitted to move to while going forward
        that is backward cells"""
        if self.color == 'white':
            return [(r, c) for c in range(8) for r in range(self.row + 1, 8)]
        else:
            return [(r, col) for col in range(8) for r in range(self.row - 1, -1, -1)]

    def initial_permissible_skip_cells(self):
        """define the initial cell a pawn can move to"""
        if (self.row == 1 or self.row == 6) and self.skip is False:
            if self.color == 'white':
                return [(self.row - skip, self.col) for skip in range(1, 3)]
            else:
                return [(self.row + skip, self.col) for skip in range(1, 3)]

    def forward_moves(self):
        # create a list of possible cell while moving forward
        if self.color == 'white':
            return [(r, self.col) for r in range(self.row - 1, -1, -1)]
        else:
            return [(r, self.col) for r in range(self.row + 1, 8)]

    def can_move(self, row_to, col_to):
        """check if the given coordinate is right to move the piece to"""
        if (row_to, col_to) in self.forward_moves() or (row_to, col_to) in self.get_capture_cell():
            return True
        elif (row_to, col_to) in self.get_prohibited_cells():
            return False

    def can_promote(self, row_to, col_to):
        """given the coordinate, check if this piece can be promoted"""
        if (row_to, col_to) in self.white_promotion_cells or (row_to, col_to) in self.black_promotion_cells:
            return True

    def can_capture(self, row_to, col_to):
        """given the coordinate, check if this piece can capture"""
        if (row_to, col_to) in self.get_capture_cell():
            return True


pawn = Pawn(row=6, col=5)
pawn.can_move(row_to=5, col_to=5)

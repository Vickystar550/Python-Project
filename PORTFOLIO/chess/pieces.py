# PARENT CLASS FOR ALL PIECES.

class Pieces:
    """Represent the chess game piece"""

    def __init__(self, **kwargs):
        self.row: int = kwargs.get('row')  # defines where the piece is currently at
        self.col: int = kwargs.get('col')  # defines where the piece is currently at
        self.name: str = kwargs.get('name')  # the piece actual name
        self.class_name = kwargs.get('class_name')  # the piece class or family name
        self.color: str = kwargs.get('color')  # the piece associated color
        self.type_: str = kwargs.get('type_')


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
        elif self.move_to in set(promoting_cells):  # overhead promoting cells
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
            return 'prohibited'


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
        self.has_move_before = 0  # 0 is for no moves
        self.castling_range = None
        self.can_castle = False

        self.permitted_moves = {}
        self.get_permitted_moves()

    def get_permitted_moves(self):
        """Get the potential permissible cells that a rook can move to. Determine based on its current location"""
        self.horizontal_moves = [(self.row, c) for c in range(8)]
        self.vertical_moves = [(r, self.col) for r in range(8)]

        self.permitted_moves = set(self.horizontal_moves).union(set(self.vertical_moves))

    def skipping(self, **kwargs):
        """checks if the rook skips any piece on its way while moving horizontally or vertically"""
        # print(kwargs)

        # combo1 skipping check
        for combo in kwargs.values():
            if self.move_from in combo and self.move_to in combo:
                from_index = combo.index(self.move_from)
                to_index = combo.index(self.move_to)

                if from_index < to_index:
                    e1_ranges = combo[from_index + 1: to_index]

                    if not e1_ranges:
                        self.allow_skip = True
                    else:
                        for e in e1_ranges:
                            result = self.virtual_board.get(e)
                            if result.piece is None:
                                self.allow_skip = True
                                continue
                            else:
                                self.allow_skip = False
                                break
                else:
                    e2_ranges = combo[from_index - 1: to_index: -1]

                    if not e2_ranges:
                        self.allow_skip = True
                    else:
                        for e in e2_ranges:
                            result = self.virtual_board.get(e)
                            if result.piece is None:
                                self.allow_skip = True
                                continue
                            else:
                                self.allow_skip = False
                                break
                break  # stop checking for skip
            else:
                continue

    def castling(self):
        """checks if castling is possible for each player"""
        if self.color == 'white':
            self.castling_range = [(7, 5), (7, 6)]
            self.rook_initial_position = (7, 7)
            self.king_initial_position = (7, 4)
            self.king_castled_coordinate = (7, 6)
        else:
            self.castling_range = [(0, 5), (0, 6)]
            self.rook_initial_position = (0, 7)
            self.king_initial_position = (0, 4)
            self.king_castled_coordinate = (0, 6)

        try:
            self.virtual_board.get(self.king_initial_position).piece.class_name == 'King'
        except AttributeError:
            # check if the king is at its castled position
            try:
                self.virtual_board.get(self.king_castled_coordinate).piece.class_name == 'King'
            except AttributeError:
                king_has_move_before = 2  # more than one
            else:
                king_has_move_before: int = self.virtual_board.get(self.king_castled_coordinate).piece.has_move_before
        else:
            king_has_move_before: int = self.virtual_board.get(self.king_initial_position).piece.has_move_before

        cond = ''
        if self.has_move_before == 1:
            if king_has_move_before == 1:
                cond = 'good'
            elif king_has_move_before >= 1:
                cond = 'bad'
            elif king_has_move_before <= 1:
                cond = 'good'

        elif self.has_move_before >= 1:
            cond = 'bad'

        elif self.has_move_before <= 0:
            if king_has_move_before == 1:
                cond = 'good'
            elif king_has_move_before >= 1:
                cond = 'bad'
            elif king_has_move_before <= 1:
                cond = 'good'

        # print('cond is:', cond)
        # print('------------------------------------------------')

        if cond == 'good':
            for coordinate in self.castling_range:
                occupying_piece = self.virtual_board.get(coordinate).piece

                if occupying_piece is None:
                    self.can_castle = True
                    continue
                else:
                    if occupying_piece.class_name == 'King' and coordinate == self.castling_range[1]:
                        self.can_castle = True
                        continue
                    else:
                        self.can_castle = False
                        break
        else:
            self.can_castle = False

    def can_move(self):
        """check if the given coordinate is right to move this piece to"""
        self.get_permitted_moves()
        self.skipping(combo1=self.horizontal_moves, combo2=self.vertical_moves)
        self.castling()

        if self.move_to in self.castling_range and self.can_castle is True:
            self.can_castle = False  # off castling for this piece
            self.has_move_before = 1  # 1 is for castling move only
            return 'castle'

        elif self.move_to in self.permitted_moves and self.allow_skip:
            self.has_move_before = 2  # 2 is for any other moves aside from castling
            if self.piece_to_capture:  # check for capturing:
                return 'capturing'
            else:
                return 'forward'

        else:
            return 'prohibited'


# ----------------------------------------- 3. KNIGHT -------------------------------------------------------

class Knight(Pieces):
    """Defines the knight class, their properties and moves.
            Inherit from the Pieces class"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_name = 'Knight'

        self.move_from: tuple = None
        self.move_to: tuple = None

        self.piece_to_capture = None
        self.virtual_board = {}

        self.potential_moves: set = None
        self.get_potential_moves()

    def get_potential_moves(self):
        """get the possible combinations of coordinates a knight can move to from its current coordinate"""
        r, c = self.row, self.col

        # for each location, there are eight possible combinations which the piece can move to
        first_combinations = {(r - 1, c - 2), (r - 1, c + 2), (r + 1, c - 2), (r + 1, c + 2)}
        second_combinations = {(r - 2, c - 1), (r - 2, c + 1), (r + 2, c - 1), (r + 2, c + 1)}

        combinations_union = first_combinations.union(second_combinations)

        # get all coordinates that make up the chess board
        all_coordinates = set(self.virtual_board.keys())

        # The intersection of all coordinates in chess board & the union of all the possible moves the knight is
        # allowed.
        # This intersection removes coordinates not in the chess board, like (1, 8), (2, 9) etc.
        self.potential_moves = combinations_union.intersection(all_coordinates)

    def can_move(self):
        """check if the given coordinate is right to move this piece to"""
        self.get_potential_moves()

        if self.move_to in self.potential_moves:
            if self.piece_to_capture:
                return 'capturing'
            else:
                return 'forward'
        else:
            return 'prohibited'


# ----------------------------------------- 4. BISHOP -------------------------------------------------------

class Bishop(Pieces):
    """Defines the bishop class, their properties and moves.
            Inherit from the Pieces class"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_name = 'Bishop'

        self.move_from: tuple = None
        self.move_to: tuple = None
        self.allow_skip = None

        self.piece_to_capture = None
        self.virtual_board = {}

        self.potential_moves: set = None
        self.get_potential_moves()

    def get_potential_moves(self):
        """get the possible combinations of coordinates (diagonals) a bishop can move to from its current coordinate"""

        self.elevating_diagonal = []  # that is, going towards the top right corner of the chess board
        for key in self.virtual_board.keys():
            if key[0] + key[1] == self.row + self.col:
                self.elevating_diagonal.append(key)

        self.decelerating_diagonal = []  # that is, going towards the bottom right corner of the chess board
        for key in self.virtual_board.keys():
            if key[0] - key[1] == self.row - self.col:
                self.decelerating_diagonal.append(key)

        # make a union of the two lists of all the possible combinations of diagonal coordinates
        self.potential_moves = set(self.elevating_diagonal).union(set(self.decelerating_diagonal))

    def skipping(self, **kwargs):
        """checks if the bishop skips any piece on its way while moving horizontally or vertically"""
        # print(kwargs)

        # skipping check
        for combo in kwargs.values():
            if self.move_from in combo and self.move_to in combo:
                from_index = combo.index(self.move_from)
                to_index = combo.index(self.move_to)

                if from_index < to_index:
                    e1_ranges = combo[from_index + 1: to_index]

                    if not e1_ranges:
                        self.allow_skip = True
                    else:
                        for e in e1_ranges:
                            result = self.virtual_board.get(e)
                            if result.piece is None:
                                self.allow_skip = True
                                continue
                            else:
                                self.allow_skip = False
                                break
                else:
                    e2_ranges = combo[from_index - 1: to_index: -1]

                    if not e2_ranges:
                        self.allow_skip = True
                    else:
                        for e in e2_ranges:
                            result = self.virtual_board.get(e)
                            if result.piece is None:
                                self.allow_skip = True
                                continue
                            else:
                                self.allow_skip = False
                                break
                break  # stop checking for skip
            else:
                continue

    def can_move(self):
        """check if the given coordinate is right to move this piece to"""
        self.get_potential_moves()
        self.skipping(combo1=self.elevating_diagonal, combo2=self.decelerating_diagonal)

        if self.move_to in self.potential_moves and self.allow_skip:
            if self.piece_to_capture:
                return 'capturing'
            else:
                return 'forward'
        else:
            return 'prohibited'


# ----------------------------------------- 5. THE QUEEN -------------------------------------------------------

class Queen(Pieces):
    """Defines the Queen class, their properties and moves.
            Inherit from the Pieces class"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_name = 'Queen'

        self.move_from: tuple = None
        self.move_to: tuple = None
        self.allow_skip = None

        self.piece_to_capture = None
        self.virtual_board = {}

        self.potential_moves: set = None
        self.get_potential_moves()

    def get_potential_moves(self):
        """Get the potential permissible cells that a queen can move to. Determine based on its current location"""

        # The queen combines the moves functionalities of both the rook and the bishop together

        # 1. Like a Rook: --------------------------------------------------
        self.horizontal_moves = [(self.row, c) for c in range(8)]
        self.vertical_moves = [(r, self.col) for r in range(8)]

        rook_like_union = set(self.horizontal_moves).union(set(self.vertical_moves))

        # 2. Like a Bishop: -------------------------------------------------
        self.elevating_diagonal = []  # that is, going towards the top right corner of the chess board
        for key in self.virtual_board.keys():
            if key[0] + key[1] == self.row + self.col:
                self.elevating_diagonal.append(key)

        self.decelerating_diagonal = []  # that is, going towards the bottom right corner of the chess board
        for key in self.virtual_board.keys():
            if key[0] - key[1] == self.row - self.col:
                self.decelerating_diagonal.append(key)

        bishop_like_union = set(self.elevating_diagonal).union(set(self.decelerating_diagonal))

        # make a union of all the possible combinations for a queen
        self.potential_moves = rook_like_union.union(bishop_like_union)

    def skipping(self, **kwargs):
        """checks if the queen skips any piece on its way while moving horizontally or
        vertically or diagonally"""
        # print(kwargs)

        # combo1 skipping check
        for combo in kwargs.values():
            if self.move_from in combo and self.move_to in combo:
                from_index = combo.index(self.move_from)
                to_index = combo.index(self.move_to)

                if from_index < to_index:
                    e1_ranges = combo[from_index + 1: to_index]

                    if not e1_ranges:
                        self.allow_skip = True
                    else:
                        for e in e1_ranges:
                            result = self.virtual_board.get(e)
                            if result.piece is None:
                                self.allow_skip = True
                                continue
                            else:
                                self.allow_skip = False
                                break
                else:
                    e2_ranges = combo[from_index - 1: to_index: -1]

                    if not e2_ranges:
                        self.allow_skip = True
                    else:
                        for e in e2_ranges:
                            result = self.virtual_board.get(e)
                            if result.piece is None:
                                self.allow_skip = True
                                continue
                            else:
                                self.allow_skip = False
                                break
                break  # stop checking for skip
            else:
                continue

    def can_move(self):
        """check if the given coordinate is right to move this piece to"""
        self.get_potential_moves()
        self.skipping(combo1=self.horizontal_moves, combo2=self.vertical_moves,
                      combo3=self.elevating_diagonal, combo4=self.decelerating_diagonal)

        if self.move_to in self.potential_moves and self.allow_skip:
            if self.piece_to_capture:
                return 'capturing'
            else:
                return 'forward'
        else:
            return 'prohibited'


# ----------------------------------------- 5. THE KING -------------------------------------------------------

class King(Pieces):
    """Defines the Queen class, their properties and moves.
            Inherit from the Pieces class"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.class_name = 'King'

        self.move_from: tuple = None
        self.move_to: tuple = None
        self.allow_skip = None

        # for castling purpose:
        self.has_move_before = 0  # 0 is for no moves
        self.castling_range = None
        self.can_castle = False

        self.piece_to_capture = None
        self.virtual_board = {}

        self.potential_moves: set = None
        self.get_potential_moves()

    def get_potential_moves(self):
        """Get the potential permissible cells that a queen can move to. Determine based on its current location"""
        r, c = self.row, self.col
        diagonal1 = [(r - 1, c - 1), (r + 1, c + 1)]
        diagonal2 = [(r + 1, c - 1), (r - 1, c + 1)]
        row_value = [(r, c - 1), (r, c + 1)]
        col_value = [(r - 1, c), (r + 1, c)]

        all_moves = set(diagonal1 + diagonal2 + row_value + col_value)
        all_coordinates = set(self.virtual_board.keys())

        self.potential_moves = all_moves.intersection(all_coordinates)

    def castling(self):
        """checks if castling is possible for each player"""
        if self.color == 'white':
            self.castling_range = [(7, 5), (7, 6)]
            self.king_initial_position = (7, 4)
            self.rook_initial_position = (7, 7)
            self.rook_castled_coordinate = (7, 5)
        else:
            self.castling_range = [(0, 5), (0, 6)]
            self.king_initial_position = (0, 4)
            self.rook_initial_position = (0, 7)
            self.rook_castled_coordinate = (0, 5)

        try:
            self.virtual_board.get(self.rook_initial_position).piece.class_name == 'Rook'
        except AttributeError:
            # check if rook is at its castled position
            try:
                self.virtual_board.get(self.rook_castled_coordinate).piece.class_name == 'Rook'
            except AttributeError:
                rook_has_move_before = 2  # more than one
            else:
                rook_has_move_before: int = self.virtual_board.get(self.rook_castled_coordinate).piece.has_move_before
        else:
            rook_has_move_before: int = self.virtual_board.get(self.rook_initial_position).piece.has_move_before

        cond = ''
        if self.has_move_before == 1:
            if rook_has_move_before == 1:
                cond = 'good'
            elif rook_has_move_before >= 1:
                cond = 'bad'
            elif rook_has_move_before <= 0:
                cond = 'good'

        elif self.has_move_before >= 1:
            cond = 'bad'

        elif self.has_move_before <= 0:
            if rook_has_move_before == 1:
                cond = 'good'
            elif rook_has_move_before >= 1:
                cond = 'bad'
            elif rook_has_move_before <= 0:
                cond = 'good'

        # print('cond is:', cond)
        # print('------------------------------------------------')

        if cond == 'good':
            for coordinate in self.castling_range:
                occupying_piece = self.virtual_board.get(coordinate).piece

                if occupying_piece is None:
                    self.can_castle = True
                    continue
                else:
                    if occupying_piece.class_name == 'Rook' and coordinate == self.castling_range[0]:
                        self.can_castle = True
                        continue
                    else:
                        self.can_castle = False
                        break
        else:
            self.can_castle = False

    def can_move(self):
        self.get_potential_moves()
        self.castling()

        if self.move_to in self.castling_range:
            if self.can_castle:
                self.can_castle = False  # off castling for this piece
                self.has_move_before = 1  # 1 is for castling move only
                return 'castle'
            else:
                if self.move_to in self.castling_range and self.move_to in self.potential_moves:
                    self.has_move_before = 2
                    return 'forward'
                # checking reverse castling for either white or black
                elif (self.move_to in self.castling_range and (self.move_to not in self.potential_moves)
                      and self.move_from in [(7, 7), (0, 7)]):
                    return 'prohibited'
                else:
                    return 'not castling'

        elif self.move_to in self.potential_moves:
            self.has_move_before = 2  # 2 is for any other moves aside from castling
            if self.piece_to_capture:
                return 'capturing'
            else:
                return 'forward'

        else:
            return 'prohibited'

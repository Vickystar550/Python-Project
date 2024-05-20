import tkinter as tk
from game_logic import Pieces
from dialog import DisplayDialog
import math
from datetime import datetime
import subprocess
import sys
import os


class Cell(tk.Button):
    """Models each cell of the chess board.
        Similar to the Move class of GameLogic. It is a tkinter button"""

    def __init__(self, row, col, piece, _type, **kwargs):
        super().__init__(**kwargs)

        # added attributes
        self.row: int = row
        self.col: int = col
        self.current_piece: Pieces = piece  # the current piece associated with that particular cell
        self.type: str = _type  # represent the type of cell by color


class GameBoard(tk.Tk):
    """Models the chess game board"""

    def __init__(self, game_logic):
        super().__init__()
        self.copyright_year = datetime.now().year
        self.title(f'CHESS © {self.copyright_year} Victor Nice')
        self.checkmate: bool = False
        self.game_logic = game_logic
        self.config(pady=5, padx=50, bg='black')
        self.minsize(width=2000, height=500)
        self.protocol("WM_DELETE_WINDOW", self.closing)
        self._cells = {}  # holds each cell and their various coordinates
        self._sub_menu = []  # holds each sub menu
        self.clicked_time = 0  # determine how much time to click before moving a piece from current place to required
        self.clicked_cell = None
        self.clicked_piece = None
        self.previous_piece = None

        self.white_successful_castles = 0
        self.black_successful_castles = 0

        self.white_capture = []
        self.black_capture = []

        # this cell holds each player piece:
        self.occupied_black_pieces = {}
        self.occupied_white_pieces = {}

        self.move_from = None
        self.move_to = None
        self.timer_id = ''
        self.toggle_id = None

        # -------------- loading upright chess icons ------------------
        # loading pawns images
        self.pawn_filled = tk.PhotoImage(file='assets/icons/pawn_filled.png')
        self.pawn_unfilled = tk.PhotoImage(file='assets/icons/pawn_unfilled.png')

        # loading rook images
        self.rook_filled = tk.PhotoImage(file='assets/icons/rook_filled.png')
        self.rook_unfilled = tk.PhotoImage(file='assets/icons/rook_unfilled.png')

        # loading knight left images
        self.knight_filled_left = tk.PhotoImage(file='assets/icons/knight_filled_left.png')
        self.knight_unfilled_left = tk.PhotoImage(file='assets/icons/knight_unfilled_left.png')

        # loading knight right images
        self.knight_filled_right = tk.PhotoImage(file='assets/icons/knight_filled_right.png')
        self.knight_unfilled_right = tk.PhotoImage(file='assets/icons/knight_unfilled_right.png')

        # loading bishop images
        self.bishop_filled = tk.PhotoImage(file='assets/icons/bishop_filled.png')
        self.bishop_unfilled = tk.PhotoImage(file='assets/icons/bishop_unfilled.png')

        # loading queen images
        self.queen_filled = tk.PhotoImage(file='assets/icons/queen_filled.png')
        self.queen_unfilled = tk.PhotoImage(file='assets/icons/queen_unfilled.png')

        # loading king images
        self.king_filled = tk.PhotoImage(file='assets/icons/king_filled.png')
        self.king_unfilled = tk.PhotoImage(file='assets/icons/king_unfilled.png')

        # -------------- loading inverted chess icons (required for pawn promotion) ------------------
        # loading inverted rook images
        self.inverted_rook_filled = tk.PhotoImage(file='assets/inverted_icons/rook_filled.png')
        self.inverted_rook_unfilled = tk.PhotoImage(file='assets/inverted_icons/rook_unfilled.png')

        # loading inverted knight left images
        self.inverted_knight_filled_left = tk.PhotoImage(file='assets/inverted_icons/knight_filled_left.png')
        self.inverted_knight_unfilled_left = tk.PhotoImage(file='assets/inverted_icons/knight_unfilled_left.png')

        # loading knight right images
        self.inverted_knight_filled_right = tk.PhotoImage(file='assets/inverted_icons/knight_filled_right.png')
        self.inverted_knight_unfilled_right = tk.PhotoImage(file='assets/inverted_icons/knight_unfilled_right.png')

        # loading bishop images
        self.inverted_bishop_filled = tk.PhotoImage(file='assets/inverted_icons/bishop_filled.png')
        self.inverted_bishop_unfilled = tk.PhotoImage(file='assets/inverted_icons/bishop_unfilled.png')

        # loading queen images
        self.inverted_queen_filled = tk.PhotoImage(file='assets/inverted_icons/queen_filled.png')
        self.inverted_queen_unfilled = tk.PhotoImage(file='assets/inverted_icons/queen_unfilled.png')

        self.pawn_promoted_image = None
        self.pawn_promoted_piece = None

        # -------------------------loading defeated king images ---------------------------------------------
        self.defeated_king_filled_left = tk.PhotoImage(file='assets/defeat_king_icons/defeat_king_filled_left.png')
        self.defeated_king_filled_right = tk.PhotoImage(file='assets/defeat_king_icons/defeat_king_filled_right.png')

        self.defeated_king_unfilled_left = tk.PhotoImage(file='assets/defeat_king_icons/defeat_king_unfilled_left.png')
        self.defeated_king_unfilled_right = tk.PhotoImage(file='assets/defeat_king_icons/defeat_king_unfilled_right.png')
        # ---------------------------------------------------------------------------------

        self.create_menu()
        self.create_panel()
        self.create_board()

        try:
            self.message = DisplayDialog(parent=self, title='Starter', purpose='starter').result.lower()
        except AttributeError:
            quit()
        else:
            if self.message == 'white':
                self.animated_display_label.config(text=f'{self.game_logic.current_player.color.title()}\'s turn',
                                                   fg='white', bg='#2d2d2d')
            elif self.message == 'black':
                self.game_logic.toggle_player()
                self.animated_display_label.config(text=f'{self.game_logic.current_player.color.title()}\'s turn',
                                                   fg='white', bg='#2d2d2d')

        # start timer
        self.timer()

    def is_valid(self, row):
        pass

    def create_menu(self):
        """create the game window menu and menu items"""
        menu_bar = tk.Menu(master=self, font=('San Serif', 10, 'normal'), bg='#2d2d2d', fg='white')
        self.config(menu=menu_bar, height=5)

        # file menu:
        file_menu = tk.Menu(master=menu_bar)
        self._sub_menu.append(file_menu)
        file_menu.add_command(label='Restart', command=self.restart)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=quit)
        menu_bar.add_cascade(label='File', menu=file_menu)

        # edit menu:
        edit_menu = tk.Menu(master=menu_bar)
        self._sub_menu.append(edit_menu)
        edit_menu.add_separator()
        # edit_menu.add_command()
        menu_bar.add_cascade(label='Edit', menu=edit_menu)

        # configure all sub menu:
        for sub_menu in self._sub_menu:
            sub_menu.config(tearoff=0, font=('San San Serif', 15, 'normal'), bg='#2d2d2d', fg='white')

    def create_panel(self):
        """create the game window panel"""
        panel_frame = tk.Frame(master=self)
        panel_frame.pack()
        panel_frame.config(pady=5, padx=5, highlightbackground='grey',
                           highlightthickness=5, bg='black')

        inner_panel_frame = tk.Frame(master=panel_frame)
        inner_panel_frame.grid(row=0, column=0)

        self.white_label = tk.Label(master=inner_panel_frame, text='White:', font=('San Serif', 15, 'normal'))
        self.white_label.config(fg='white', justify='left', width=35)
        self.white_label.grid(row=0, column=0)

        self.black_label = tk.Label(master=inner_panel_frame, text='Black:', font=('San Serif', 15, 'normal'))
        self.black_label.config(fg='white', justify='left', width=35)
        self.black_label.grid(row=0, column=1)

        self.animated_display_label = tk.Label(master=inner_panel_frame,
                                               text=f'Your are welcome. Please enjoy your stay',
                                               font=('San Serif', 15, 'normal'))

        self.animated_display_label.config(bg='#2d2d2d', fg='sea green', justify='center')
        self.animated_display_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='ew')
        self.animated_display_label.columnconfigure(0, weight=1, minsize=65)

    def create_board(self):
        """create the chess board"""
        # make an outer tkinter frame managed by pack geometry manager, parent is self
        outer_frame = tk.Frame(master=self)
        outer_frame.pack()
        outer_frame.config(padx=20, pady=10, bg='#CC5500', highlightthickness=0)

        # make an inner frame whose parent is the outer_frame, but it is managed by the grid system
        inner_frame = tk.Frame(master=outer_frame)
        inner_frame.grid(row=0, column=0)

        # create the cells which are tkinter buttons
        for row in range(self.game_logic.board_size):
            self.rowconfigure(row, weight=1, minsize=100)
            self.columnconfigure(row, weight=1, minsize=100)

            for col in range(self.game_logic.board_size):

                # set cell color to alternate between even and odd cells
                if (row + col) % 2 == 0:
                    cell_color = '#808080'
                    cell_type = 'white'
                else:
                    cell_color = '#2d2d2d'
                    cell_type = 'black'

                cell = Cell(row=row, col=col, piece=None, _type=cell_type, master=inner_frame, width=5, height=3,
                            font=('Courier', 20, 'normal'), bg=cell_color, activebackground=cell_color)
                cell.grid(row=row, column=col, sticky='nsew')

                # store each cell
                self._cells[cell] = (row, col)

                # bind every button to the play method
                cell.bind("<ButtonPress-1>", self.play)

        # initialize cells with chess images after creating
        self.initialize_cells()
        self.distinguish_cells()

    def initialize_cells(self):
        """initialize the first-two and last-two rows with button filled with images"""
        for cell, coordinates in self._cells.items():
            row, col = coordinates

            # NOTE: cell height and width are now in pixels

            # for pawns
            if coordinates[0] == 1:
                cell.config(image=self.pawn_filled, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            elif coordinates[0] == 6:
                cell.config(image=self.pawn_unfilled, width=110, height=110,
                            highlightthickness=0, borderwidth=0, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            # for castle
            elif coordinates in [(0, 0), (0, 7), ]:
                cell.config(image=self.rook_filled, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            elif coordinates in [(7, 0), (7, 7)]:
                cell.config(image=self.rook_unfilled, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            # for knight left
            elif coordinates == (0, 1):
                cell.config(image=self.knight_filled_left, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            elif coordinates == (7, 1):
                cell.config(image=self.knight_unfilled_left, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            # for knight right
            elif coordinates == (0, 6):
                cell.config(image=self.knight_filled_right, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            elif coordinates == (7, 6):
                cell.config(image=self.knight_unfilled_right, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            # for bishop
            elif coordinates in [(0, 2), (0, 5)]:
                cell.config(image=self.bishop_filled, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            elif coordinates in [(7, 2), (7, 5)]:
                cell.config(image=self.bishop_unfilled, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            # for queen
            elif coordinates == (0, 3):
                cell.config(image=self.queen_filled, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            elif coordinates == (7, 3):
                cell.config(image=self.queen_unfilled, highlightthickness=0, borderwidth=0,
                            width=110, height=110, relief='flat')
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            # for king
            elif coordinates == (0, 4):
                cell.config(image=self.king_filled, highlightthickness=0, borderwidth=0,
                            width=110, height=100, )
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

            elif coordinates == (7, 4):
                cell.config(image=self.king_unfilled, highlightthickness=0, borderwidth=0,
                            width=110, height=100, )
                cell.current_piece = self.game_logic.get_piece(row=row, col=col)

    def distinguish_cells(self):
        """differentiate cells into white and black based on the color of the piece it holds currently"""
        for cell, coordinate in self._cells.items():
            try:
                piece_color = cell.current_piece.color
            except AttributeError:
                continue
            else:
                if piece_color == 'white':
                    self.occupied_white_pieces[cell] = coordinate
                else:
                    self.occupied_black_pieces[cell] = coordinate

    def configure_cell(self, **kwargs):
        """configure or reset a specific cell"""
        # location of the cell to configure
        row = kwargs.get('row')
        col = kwargs.get('col')

        # attribute to reset
        piece: Pieces = kwargs.get('piece')
        image: tk.PhotoImage = kwargs.get('image')

        # get the specific cell
        cell_to_config = [cell for cell, coordinate in self._cells.items() if coordinate == (row, col)][0]

        if cell_to_config.type == 'white':
            cell_color = '#808080'
        else:
            cell_color = '#2d2d2d'

        # add a piece to it
        cell_to_config.current_piece = piece

        if image:
            cell_to_config.config(image=image, width=110, height=110, highlightthickness=0, borderwidth=0)
        else:
            cell_to_config.config(image='', width=5, height=3, font=('Courier', 20, 'normal'), bg=cell_color,
                                  activebackground=cell_color)

        # return the configured cell
        return cell_to_config

    def name_cell(self, row, col):
        """name cell"""
        alpha_index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        num_index = [1, 2, 3, 4, 5, 6, 7, 8]

        named_dict = {(num_index.index(num), alpha_index.index(alpha)): f"{alpha}{num}" for num in num_index for alpha
                      in alpha_index}

        return named_dict.get((row, col))

    def play(self, event):
        """Handle a player's move"""

        # get the current clicked cell object
        self.clicked_cell = event.widget

        # get the current clicked piece from the clicked cell
        self.clicked_piece = self.clicked_cell.current_piece

        # get the clicked cell coordinates:
        row, col = self._cells[self.clicked_cell]

        self.current_player_color = self.game_logic.current_player.color

        # get permissible cells for either black or white player
        if self.current_player_color == 'white':
            self.permissible_starting_cells = self.occupied_white_pieces
        else:
            self.permissible_starting_cells = self.occupied_black_pieces

        # ------------- PASTING -----------
        if self.clicked_time == 1:
            self.paste(row=row, col=col)
        # ------------- COPYING -----------
        elif self.clicked_time == 0:
            self.copy(row=row, col=col)

    def toggle(self, state: str):
        if state == 'pasting':
            """toggles the next player 2 seconds after the last player played """
            self.game_logic.toggle_player()
            self.timer()
            self.after_cancel(self.toggle_id)
            self.animated_display_label.config(text=f'{self.game_logic.current_player.color.title()}\'s turn',
                                               fg='white', bg='#2d2d2d')
            self.clicked_time = 0
        elif state == 'delay':
            self.game_logic.toggle_player()
            self.timer()
            self.animated_display_label.config(text=f'{self.game_logic.current_player.color.title()}\'s turn',
                                               fg='white', bg='#2d2d2d')
            self.clicked_time = 0
        elif state == 'penalize':
            self.game_logic.toggle_player()
            self.timer()
            self.after_cancel(self.penalize_id)
            self.animated_display_label.config(text=f'{self.game_logic.current_player.color.title()}\'s turn',
                                               fg='white', bg='#2d2d2d')
        elif state == 'warnings':
            self.after_cancel(self.error_id)
            self.animated_display_label.config(text=f'{self.game_logic.current_player.color.title()}\'s turn',
                                               fg='white', bg='#2d2d2d')
        elif state == 'validation':
            self.after_cancel(self.message_id)
            self.animated_display_label.config(text=self.validation_report, fg='white', bg='#2d2d2d')

        elif state == 'checkmate':
            try:
                dlg = DisplayDialog(parent=self, title='Exit', purpose='checkmate').result.lower()
            except AttributeError:
                self.destroy()
            else:
                if dlg == 'yes':
                    self.restart()
                else:
                    self.destroy()

    def select_image(self, name, **kwargs):
        """return an image given the piece name"""
        type_: str = kwargs.get('type')

        if type_ == 'inverted':  # get inverted icons required for pawn promotions
            # inverted rook
            if name == 'WRook':
                return self.inverted_rook_unfilled
            elif name == 'BRook':
                return self.inverted_rook_filled

            # inverted white knight
            if name == 'WKnightLeft':
                return self.inverted_knight_unfilled_left
            elif name == 'WKnightRight':
                return self.inverted_knight_unfilled_right

            # inverted black knight
            if name == 'BKnightLeft':
                return self.inverted_knight_filled_left
            elif name == 'BKnightRight':
                return self.inverted_knight_filled_right

            # inverted bishop
            if name == 'WBishop':
                return self.inverted_bishop_unfilled
            elif name == 'BBishop':
                return self.inverted_bishop_filled

            # inverted queen
            if name == 'WQueen':
                return self.inverted_queen_unfilled
            elif name == 'BQueen':
                return self.inverted_queen_filled

        elif type_ == 'normal':  # when a type_ is 'normal', or not given
            # pawn
            if name == 'WPawn':
                return self.pawn_unfilled
            elif name == 'BPawn':
                return self.pawn_filled

            # rook
            if name == 'WRook':
                return self.rook_unfilled
            elif name == 'BRook':
                return self.rook_filled

            # white knight
            if name == 'WKnightLeft':
                return self.knight_unfilled_left
            elif name == 'WKnightRight':
                return self.knight_unfilled_right

            # black knight
            if name == 'BKnightLeft':
                return self.knight_filled_left
            elif name == 'BKnightRight':
                return self.knight_filled_right

            # bishop
            if name == 'WBishop':
                return self.bishop_unfilled
            elif name == 'BBishop':
                return self.bishop_filled

            # queen
            if name == 'WQueen':
                return self.queen_unfilled
            elif name == 'BQueen':
                return self.queen_filled

            # king
            if name == 'WKing':
                return self.king_unfilled
            elif name == 'BKing':
                return self.king_filled

    def timer(self, sec=60):
        """ Act like a stopwatch.
        Also display the timing mechanism on the canvas"""
        try:
            minutes = math.floor(sec / 60)
            actual_sec = math.floor(sec % 60)

            if actual_sec < 10:
                actual_sec = f'0{actual_sec}'

            if minutes < 10:
                minutes = f'0{minutes}'

            if self.game_logic.current_player.color == 'white':
                self.black_label.config(text='Black:', fg='white')
                self.white_label.config(text=f'White: {minutes}:{actual_sec}', fg='green')
            else:
                self.white_label.config(text='White:', fg='white')
                self.black_label.config(text=f'Black: {minutes}:{actual_sec}', fg='green')

            if sec >= 0:
                # keep the timing
                self.timer_id = self.after(1000, self.timer, sec - 1)

            if sec <= 0:
                self.after_cancel(self.timer_id)
                self.toggle(state='delay')

        except tk.TclError:
            # Handle the error if the window is closed
            pass

    def copy(self, row, col):
        self.move_from = row, col

        # ------------- change the current clicked piece location to this clicked location-------
        try:
            self.clicked_piece.row, self.clicked_piece.col = row, col
        except AttributeError:  # if no piece exists
            pass

        # send the current piece back to game logic
        self.game_logic.move_from = self.move_from
        self.game_logic.moving_piece = self.clicked_piece

        # -----------------------------------------------
        if self.clicked_piece is None:
            # you cannot copy a cell with no piece
            self.clicked_time = 0

        # -----------------------------------------------
        elif self.clicked_cell not in self.permissible_starting_cells.keys():
            self.animated_display_label.config(text=f'TRESPASSING: Ensure to move your own piece!',
                                               fg='black', bg='crimson')
            self.error_id = self.after(3000, self.toggle, 'warnings')
            self.clicked_time = 0

        # ----------------------------------------------
        else:
            # set the clicked cell as a previous clicked cell to be used when pasting
            self.previous_piece = self.clicked_piece

            # remove the copied item from permissible_starting_cells
            self.permissible_starting_cells.pop(self.clicked_cell)

            cell_name = self.name_cell(row=row, col=col)

            copied_report = (f'{self.clicked_piece.color.title()} {self.clicked_piece.class_name} '
                             f'moves from {cell_name}')

            self.animated_display_label.config(text=f'{copied_report}', fg='white', bg='#2d2d2d')

            # get the piece name and its associated image
            self.previous_piece_image = self.select_image(name=self.clicked_piece.name, type=self.clicked_piece.type_)

            # reset this cell to the default properties
            self.configure_cell(row=row, col=col, piece=None)

            # increment clicked time to enable pasting
            self.clicked_time += 1

    def paste(self, row, col):
        self.move_to = row, col
        self.cell_name = self.name_cell(row=row, col=col)

        self.game_logic.move_to = self.move_to
        self.game_logic.piece_to_be_remove = self.clicked_piece

        self.validating_string = self.game_logic.validate_move()

        if self.validating_string in ['forward', 'capturing', 'promote', 'capture and promote', 'castle']:
            # ---------------------- double pasting ------------------------
            if self.previous_piece is None:
                # self.previous_piece can only be None after pasting was successful
                # that is the player tries to double paste
                self.clicked_time = 0

            # ------------------------ self capture -----------------------
            elif self.clicked_cell in self.permissible_starting_cells.keys():
                self.return_piece_back(reason='Self Capture')
                self.clicked_time = 0

            # --------------------------- normal case ------------------------
            else:
                # case 1: ---------- when validating string is either forward, promote, or castle ------------------
                if self.clicked_piece is None:

                    if self.validating_string == 'promote':
                        paste_report = (f'Congratulations Mr. {self.previous_piece.color.title()} '
                                        f'{self.previous_piece.class_name.upper()}. Please get yourself PROMOTED!')
                        self.animated_display_label.config(text=paste_report, fg='black', bg='sea green')

                        # call pawn promotion
                        self.pawn_promotion()

                        self.validation_report = (f'{self.cell_name} now occupied by '
                                                  f'{self.previous_piece.color.title()} '
                                                  f'{self.previous_piece.class_name.upper()}')
                        self.message_id = self.after(2000, self.toggle, 'validation')

                    # --------------------------------------------------------------------------------
                    elif self.validating_string == 'castle':
                        if self.previous_piece.color == 'white':
                            self.white_successful_castles += 1
                        else:
                            self.black_successful_castles += 1

                        if self.previous_piece.color == 'white' and self.white_successful_castles >= 2 \
                                or (self.previous_piece.color == 'black' and self.black_successful_castles >= 2):

                            full_castled_report = (f'{self.previous_piece.color.title()} player '
                                                   f'has fully castled his KING and ROOK')
                            self.animated_display_label.config(text=full_castled_report, fg='black', bg='sea green')
                        else:
                            half_castled_report = (f'{self.previous_piece.color.title()} '
                                                   f'{self.previous_piece.class_name.upper()} '
                                                   f'probably castled to {self.cell_name}')
                            self.animated_display_label.config(text=half_castled_report, fg='black', bg='#CC5500')
                        # -------------------------------------------------------------------------------
                    else:
                        paste_report = (f'{self.cell_name} now occupied by '
                                        f'{self.previous_piece.color.title()} {self.previous_piece.class_name.upper()}')
                        self.animated_display_label.config(text=paste_report, fg='white', bg='#2d2d2d')

                # case 2: ------ when validating string is either capturing, or 'promote and capture' -----------
                else:
                    # check for checkmate!
                    if self.clicked_piece.class_name == 'King':
                        self.checkmate = True
                        checkmate_report = (
                            f'{self.clicked_piece.color.title()} {self.clicked_piece.class_name.upper()}'
                            f' is CHECKMATE! The {self.previous_piece.color.upper()} player wins')

                        self.animated_display_label.config(text=checkmate_report, fg='black', bg='blue')
                        self.after_cancel(self.timer_id)
                        self.exit_id = self.after(3000, self.toggle, 'checkmate')
                    else:
                        #   remove an already occupied piece from its permissible cells
                        if self.clicked_piece.color == 'white':  # ---- white piece is being capture
                            self.occupied_white_pieces.pop(self.clicked_cell)
                            self.black_capture.append(self.clicked_cell.current_piece)  # Store captive by black player

                        elif self.clicked_piece.color == 'black':  # ---- black piece is being capture
                            self.occupied_black_pieces.pop(self.clicked_cell)
                            self.white_capture.append(self.clicked_cell.current_piece)  # Store captive by white player

                        # check is the captor is a pawn & the validating string is 'capture and promote'
                        if self.validating_string == 'capture and promote':
                            paste_report = (
                                f'{self.clicked_piece.color.title()} {self.clicked_piece.class_name.upper()} '
                                f'at {self.cell_name} was captured by {self.previous_piece.color.title()}'
                                f' {self.previous_piece.class_name.upper()}. You deserves a PROMOTION!')

                            self.animated_display_label.config(text=paste_report, fg='black', bg='sea green')

                            # call pawn promotion
                            self.pawn_promotion()

                            self.validation_report = (f'{self.cell_name} now occupied by '
                                                      f'{self.previous_piece.color.title()} '
                                                      f'{self.previous_piece.class_name.upper()}')
                            self.message_id = self.after(2000, self.toggle, 'validation')

                        else:
                            paste_report = (
                                f'{self.clicked_piece.color.title()} {self.clicked_piece.class_name.upper()} '
                                f'at {self.cell_name} was captured by {self.previous_piece.color.title()}'
                                f' {self.previous_piece.class_name.upper()}')

                            self.animated_display_label.config(text=paste_report, fg='white', bg='#2d2d2d')

                    # ------------------------------------------

                # change the current cell at this position to inherit from the previous clicked cell
                if self.checkmate:
                    image = self.get_defeated_king_image()
                    new_cell = self.configure_cell(row=row, col=col, image=image,
                                                   piece=self.previous_piece)
                else:
                    if self.validating_string in ['promote', 'capture and promote']:
                        new_cell = self.configure_cell(row=row, col=col, image=self.pawn_promoted_image,
                                                       piece=self.pawn_promoted_piece)
                    else:
                        new_cell = self.configure_cell(row=row, col=col, image=self.previous_piece_image,
                                                       piece=self.previous_piece)

                # add new_cell to the permissible_cells
                self.permissible_starting_cells[new_cell] = self.move_to

                #  ----update the Move object at previous position to loss this piece
                self.game_logic.update_moves(row=self.move_from[0], col=self.move_from[1], piece=None,
                                             player=self.game_logic.current_player)

                # -----update the Move object at this position to have this piece
                if self.validating_string in ['promote', 'capture and promote']:
                    self.game_logic.update_moves(row=row, col=col, piece=self.pawn_promoted_piece,
                                                 player=self.game_logic.current_player)
                else:
                    self.game_logic.update_moves(row=row, col=col, piece=self.previous_piece,
                                                 player=self.game_logic.current_player)

                # to avoid double pasting, reset some inherited variables:
                self.previous_piece_image = None
                self.previous_piece = None

                # cancel timer after pasting
                self.after_cancel(self.timer_id)

                # toggle player after pasting, but only after 3 seconds
                if self.checkmate:
                    self.after_cancel(self.timer_id)
                else:
                    self.toggle_id = self.after(3000, self.toggle, 'pasting')

        # ----------------------- when validating string fall here -----------
        elif self.validating_string in ['blocked', 'prohibited', 'not capturing', 'not castling']:
            self.return_piece_back(reason='BP-NC')
            self.clicked_time = 0

    def return_piece_back(self, reason: str):
        """This function returns the current moving piece to its previous position where it came from"""
        if reason == 'Self Capture':
            self.animated_display_label.config(text='Self capture not permitted! Move to a cell not occupy by your '
                                                    'piece', fg='black', bg='crimson')

        elif reason == 'BP-NC':
            if self.previous_piece is None:
                pass
            else:
                if self.validating_string == 'blocked':
                    self.animated_display_label.config(text=f'This {self.previous_piece.color.title()}'
                                                            f' {self.previous_piece.class_name.upper()} cannot continue'
                                                            f'  forward again!', fg='black', bg='crimson')

                elif self.validating_string == 'not capturing':
                    self.animated_display_label.config(text=f'This {self.previous_piece.color.title()} '
                                                            f'{self.previous_piece.class_name.upper()} cannot capture'
                                                            f' any empty cell!', fg='black', bg='crimson')

                elif self.validating_string == 'not castling':
                    self.animated_display_label.config(text=f'{self.previous_piece.color.title()} '
                                                            f'{self.previous_piece.class_name.upper()} can\'t castled '
                                                            f'anymore! Nor is allowed to skip over a piece.',
                                                       fg='black', bg='crimson')

                elif self.validating_string in ['prohibited']:
                    self.animated_display_label.config(text=f'{self.previous_piece.color.title()} '
                                                            f'{self.previous_piece.class_name.upper()} not permitted'
                                                            f' to move here!', fg='black', bg='crimson')

        # -------------------------------------------
        # return pasting piece to it previous position
        returned_row, returned_column = self.move_from

        returned_cell = self.configure_cell(row=returned_row, col=returned_column,
                                            image=self.previous_piece_image, piece=self.previous_piece)

        # add returned cell back to the permissible_cells
        self.permissible_starting_cells[returned_cell] = self.move_from

        # return the Move object at this position
        self.game_logic.update_moves(row=returned_row, col=returned_column, piece=self.previous_piece,
                                     player=self.game_logic.current_player)

        # to avoid double pasting, reset some inherited variables:
        self.previous_piece_image = None
        self.previous_piece = None

        if reason == 'Self Capture':  # penalize this action(self-capturing)
            self.after_cancel(self.timer_id)
            self.penalize_id = self.after(3000, self.toggle, 'penalize')
        elif reason == 'BPU-NC':
            self.error_id = self.after(3000, self.toggle, 'warnings')

    def get_promotion_image(self, option: str):
        """get a promotion image for the promoted pawn piece"""

        if self.previous_piece.color == 'white':
            if option == 'rook':
                self.pawn_promoted_image = self.select_image(name='WRook', type='inverted')

            elif option == 'bishop':
                self.pawn_promoted_image = self.select_image(name='WBishop', type='inverted')

            elif option == 'queen':
                self.pawn_promoted_image = self.select_image(name='WQueen', type='inverted')

            elif option == 'knight':
                # when white pawn is promoted, that means it must be in black first row
                if self.move_to in [(0, 0), (0, 1), (0, 2), (0, 3)]:
                    self.pawn_promoted_image = self.select_image(name='WKnightLeft', type='inverted')
                elif self.move_to in [(0, 4), (0, 5), (0, 6), (0, 7)]:
                    self.pawn_promoted_image = self.select_image(name='WKnightRight', type='inverted')
        else:  # for black
            if option == 'rook':
                self.pawn_promoted_image = self.select_image(name='BRook', type='inverted')

            elif option == 'bishop':
                self.pawn_promoted_image = self.select_image(name='BBishop', type='inverted')

            elif option == 'queen':
                self.pawn_promoted_image = self.select_image(name='BQueen', type='inverted')

            elif option == 'knight':
                # when black pawn is promoted, that means it must be in white first row
                if self.move_to in [(7, 0), (7, 1), (7, 2), (7, 3)]:
                    self.pawn_promoted_image = self.select_image(name='BKnightLeft', type='inverted')
                elif self.move_to in [(7, 4), (7, 5), (7, 6), (7, 7)]:
                    self.pawn_promoted_image = self.select_image(name='BKnightRight', type='inverted')

    def get_defeated_king_image(self):
        """get the defeated king image"""
        r, c = self.move_to
        if self.clicked_piece.color == 'white':
            if 0 <= c <= 3:
                return self.defeated_king_unfilled_left
            elif 4 <= c <= 7:
                return self.defeated_king_unfilled_right
        else:
            if 0 <= c <= 3:
                return self.defeated_king_filled_left
            elif 4 <= c <= 7:
                return self.defeated_king_filled_right

    def pawn_promotion(self):
        r, c = self.move_to

        dlg = DisplayDialog(parent=self, title='Pawn Promotion', purpose='promotion')
        # self.wait_window(dlg)   # Wait for the dialog to close
        option = dlg.result.lower()

        self.get_promotion_image(option=option)
        self.pawn_promoted_piece = self.game_logic.create_piece(row=r, col=c, which=option,
                                                                color=self.previous_piece.color)

    def restart(self):
        self.destroy()

        # Determine the current Python interpreter
        python = sys.executable

        # Determine the path to the main script
        script_path = os.path.join(os.path.dirname(__file__), 'main.py')

        # Use subprocess to restart the script
        subprocess.run([python, script_path])

        # Optional: exit the current script
        sys.exit()

    def closing(self):
        """closing function for force closed"""
        try:
            dlg = DisplayDialog(parent=self, title='Exit', purpose='exit').result.lower()
        except tk.TclError:
            pass
        else:
            if dlg == 'yes':
                self.destroy()
            else:
                self.restart()

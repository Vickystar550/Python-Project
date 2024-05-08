import tkinter as tk
from tkinter import messagebox
from game_logic import Pieces
import math


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
        self.title('Chess')
        # self.geometry('1000x700')
        self.game_logic = game_logic
        self.config(pady=5, padx=50, bg='#2d2d2d')
        self.minsize(width=2000, height=500)
        self._cells = {}  # holds each cell their various coordinates
        self._sub_menu = []  # holds each sub menu
        self.clicked_time = 0  # determine how much time to click before moving a piece from current place to required
        self.clicked_cell = None
        self.previous_piece = None

        # this cell holds each player piece:
        self.occupied_black_pieces = {}
        self.occupied_white_pieces = {}

        self.move_from = None
        self.move_to = None
        self.timer_id = ''

        # loading pawns images
        self.pawn_filled = tk.PhotoImage(file='./CHESS ICONS/pawn_filled.png')
        self.pawn_unfilled = tk.PhotoImage(file='./CHESS ICONS/pawn_unfilled.png')

        # loading rook images
        self.rook_filled = tk.PhotoImage(file='./CHESS ICONS/rook_filled.png')
        self.rook_unfilled = tk.PhotoImage(file='./CHESS ICONS/rook_unfilled.png')

        # loading knight left images
        self.knight_filled_left = tk.PhotoImage(file='./CHESS ICONS/knight_filled_left.png')
        self.knight_unfilled_left = tk.PhotoImage(file='./CHESS ICONS/knight_unfilled_left.png')

        # loading knight right images
        self.knight_filled_right = tk.PhotoImage(file='./CHESS ICONS/knight_filled_right.png')
        self.knight_unfilled_right = tk.PhotoImage(file='./CHESS ICONS/knight_unfilled_right.png')

        # loading bishop images
        self.bishop_filled = tk.PhotoImage(file='./CHESS ICONS/bishop_filled.png')
        self.bishop_unfilled = tk.PhotoImage(file='./CHESS ICONS/bishop_unfilled.png')

        # loading queen images
        self.queen_filled = tk.PhotoImage(file='./CHESS ICONS/queen_filled.png')
        self.queen_unfilled = tk.PhotoImage(file='./CHESS ICONS/queen_unfilled.png')

        # loading king images
        self.king_filled = tk.PhotoImage(file='./CHESS ICONS/king_filled.png')
        self.king_unfilled = tk.PhotoImage(file='./CHESS ICONS/king_unfilled.png')

        self.create_menu()
        self.create_panel()
        self.create_board()

        self.message = messagebox.askquestion(title="Who's First?", message="Should the WHITE player begin?",
                                              icon='question')
        if self.message == 'no':
            self.game_logic.toggle_player()
            self.animated_display_label.config(text=f'{self.game_logic.current_player.color.title()} turns')

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
        file_menu.add_command(
            label='Play Again',
            # command=self._game.reset_board
        )
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

        self.animated_display_label = tk.Label(master=inner_panel_frame, text=f'Welcome',
                                               font=('San Serif', 15, 'normal'))

        self.animated_display_label.config(bg='#2d2d2d', fg='white', justify='center', width=65)
        self.animated_display_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def create_board(self):
        """create the chess board"""
        # make an outer tkinter frame managed by pack geometry manager, parent is self
        outer_frame = tk.Frame(master=self)
        outer_frame.pack()
        outer_frame.config(padx=20, pady=10, bg='orange', highlightthickness=0)

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

    def get_cell_property(self, row, col):
        """get a button properties"""
        for cell, coordinate in self._cells.items():
            if (row, col) == coordinate:
                pass

    def play(self, event):
        """Handle a player's move"""

        # get the current clicked cell object
        self.clicked_cell = event.widget

        # get the current clicked piece from the clicked cell
        clicked_piece = self.clicked_cell.current_piece

        # get the clicked cell coordinates:
        row, col = self._cells[self.clicked_cell]

        current_player_color = self.game_logic.current_player.color

        # get permissible cells for either black or white player
        if current_player_color == 'white':
            permissible_starting_cells = self.occupied_white_pieces
        else:
            permissible_starting_cells = self.occupied_black_pieces

        # ############## PASTING ###################
        if self.clicked_time == 1:
            self.move_to = row, col
            cell_name = self.name_cell(row=row, col=col)

            if self.previous_piece is None:
                # self.previous_piece can only be None after pasting was successful
                # that is the player tries to double paste
                messagebox.showwarning(title='Empty Hand!', message='No piece to play')
                self.clicked_time = 0
            else:

                if clicked_piece is None:
                    paste_report = (f'{cell_name} now occupied by '
                                    f'{self.previous_piece.color.title()} {self.previous_piece.class_name}')
                else:
                    paste_report = (f'{clicked_piece.color.title()} {clicked_piece.class_name} at {cell_name} '
                                    f'captured by {self.previous_piece.color.title()} {self.previous_piece.class_name}')

                self.animated_display_label.config(text=paste_report)

                # change the current cell at this position to inherit from the previous clicked cell
                new_cell = self.configure_cell(row=row, col=col, image=self.previous_piece_image,
                                               piece=self.previous_piece)

                # add new_cell to the permissible_cells
                permissible_starting_cells[new_cell] = self.move_to

                # update the Move object at this position
                self.game_logic.update_moves(row=row, col=col, piece=self.previous_piece,
                                             player=self.game_logic.current_player)

                # to avoid double pasting, reset some inherited variables:
                self.previous_piece_image = None
                self.previous_piece = None

                # cancel timer after pasting
                self.after_cancel(self.timer_id)

                # toggle after pasting, but only after 3 seconds
                self.toggle_id = self.after(3000, self.toggle, 'pasting')

        # ############# COPYING ############
        elif self.clicked_time == 0:
            self.move_from = row, col

            if clicked_piece is None:
                # you cannot copy a cell with no piece
                messagebox.showerror(title='Invalid Selection!',
                                     message=f'Cell occupies no piece now!\n\n'
                                             f'Please click on a valid {current_player_color.title()} piece')
                self.clicked_time = 0

            elif self.clicked_cell not in permissible_starting_cells.keys():
                messagebox.showwarning(title='Trespassing!',
                                       message='Ensured to move your own piece')
                self.clicked_time = 0

            else:
                # set the clicked cell as a previous clicked cell to be used when pasting
                self.previous_piece = clicked_piece

                # remove the copied item from permissible_starting_cells
                permissible_starting_cells.pop(self.clicked_cell)

                cell_name = self.name_cell(row=row, col=col)

                copied_report = f'{clicked_piece.color.title()} {clicked_piece.class_name} moves from {cell_name}'
                self.animated_display_label.config(text=f'{copied_report}')

                # update the Move object at that position to loss its piece
                self.game_logic.update_moves(row=row, col=col, piece=None,
                                             player=self.game_logic.current_player)

                # get the piece name and its associated image
                self.previous_piece_image = self.select_image(name=clicked_piece.name)

                # reset this cell to the default properties
                self.configure_cell(row=row, col=col, piece=None)

                # increment clicked time to enable pasting
                self.clicked_time += 1

    def toggle(self, _when: str):
        if _when == 'pasting':
            """toggles the next player 2 seconds after the last player played """
            self.game_logic.toggle_player()
            self.timer()
            self.after_cancel(self.toggle_id)
            self.animated_display_label.config(text=f'{self.game_logic.current_player.color.title()} turns')
            self.clicked_time = 0
        elif _when == 'delay':
            self.game_logic.toggle_player()
            self.timer()
            self.animated_display_label.config(text=f'{self.game_logic.current_player.color.title()} turns')

    def select_image(self, name):
        """return an image given the piece name"""
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

    def mid_button_state(self):
        """disable or enable the mid-buttons until the first click is made"""
        # get mid-buttons
        for btn, coordinates in self._cells.items():
            if coordinates[0] in [2, 3, 4, 5]:
                if self.clicked_time == 0:
                    btn.config(state='disabled')
                else:
                    btn.config(state='normal')

    def timer(self, sec=60):
        """ Act like a stopwatch.
        Also display the timing mechanism on the canvas"""
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
            self.toggle(_when='delay')

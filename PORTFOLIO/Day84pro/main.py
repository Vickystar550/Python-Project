import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle


class Player(NamedTuple):
    """represent each player.
    their color and label"""
    label: str
    color: str


class Move(NamedTuple):
    """represent each moves made"""
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
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        """Get all the possible winning combinations.
         Along all rows, columns and the two diagonals"""
        # Get all the possible winning combinations along all rows.
        rows = [[(move.row, move.col) for move in row] for row in self._current_moves]

        # Get all the possible winning combinations along all columns.
        columns = [list(col) for col in zip(*rows)]

        # Get all the possible winning combinations along the first diagonal
        first_diagonal = [row[i] for i, row in enumerate(rows)]

        # Get all the possible winning combinations along the second diagonal
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]

        # Return a list of lists of all the possible winning combinations
        return rows + columns + [first_diagonal, second_diagonal]

    def is_valid_moves(self, move: Move):
        """Return True if move is valid, otherwise False"""
        # get the row and col coordinate from the current Move
        row, col = move.row, move.col

        # check if this current Move was not played before by checking to see if its corresponding
        # label is empty or preoccupied
        move_was_not_played = self._current_moves[row][col].label == ''

        # check if there is no winner
        no_winner = not self._has_winner

        # return a boolean that result from if the game has no winner and the current move hasn't been played before
        return no_winner and move_was_not_played

    def process_moves(self, move: Move):
        """Process the current move and check if it's a win"""
        row, col = move.row, move.col

        # set the _current_move attribute to move
        self._current_moves[row][col] = move

        # loop through every combination range in the list of all possible winning combinations
        for combo in self._winning_combos:
            # get all the Move(s) label for that given combo and store it as a set variable
            # -- this help in checking is all the label have unique value which is responsible for a win
            result = set(self._current_moves[n][m].label for n, m in combo)

            # check if there is a win, first len of the result must be 1 --- that is every label values were unique
            # -- and "" must not be contained in result
            is_win = (len(result) == 1) and ("" not in result)

            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        """Returns True if the game has a winner, and False otherwise"""
        return self._has_winner

    def is_tied(self):
        """Return True if the game is tied, and False otherwise"""
        no_winner = not self._has_winner

        # get the played moves
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)

    def toggle_player(self):
        """Return a toggled player."""
        self.current_player = next(self.players)

    def reset_board(self):
        """Reset the game state to play again"""
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []


class TicTacToeBoard(tk.Tk):
    def __init__(self, game: TicTacToeGame):
        super().__init__()
        self.title('Tic-Tac-Toe Game')
        # self.display = None
        self._cells = {}
        self._game = game
        self.create_menu()
        self.create_display_frame()
        self.create_display_grid()

    def create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(
            label='Play Again',
            command=self._game.reset_board
        )
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=quit)
        menu_bar.add_cascade(label='File', menu=file_menu)

    def create_display_frame(self):
        # create a display frame as the container
        display_frame = tk.Frame(master=self, )
        # position it using pack geometry manager
        display_frame.pack(fill=tk.X)
        # instantiate a display Label
        self.display = tk.Label(master=display_frame,
                                text='Ready?',
                                font=font.Font(size=30, weight='bold'))
        self.display.pack()

    def create_display_grid(self):
        display_grid = tk.Frame(master=self)
        display_grid.pack()

        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)

            for col in range(self._game.board_size):
                button = tk.Button(master=display_grid,
                                   width=5,
                                   height=3,
                                   highlightbackground='blue',
                                   text='',
                                   font=font.Font(size=36, weight='bold'),
                                   fg='black')

                self._cells[button] = (row, col)

                # connect every button with the play method
                button.bind("<ButtonPress-1>", self.play)

                button.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')

    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label,
                           fg=self._game.current_player.color)

    def _update_display(self, msg, color='black'):
        self.display['text'] = msg
        self.display['fg'] = color

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground='red')

    def play(self, event):
        """Handle a player's move"""
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)

        # check if this is a valid move
        if self._game.is_valid_moves(move=move):
            self._update_button(clicked_btn)

            # process the move
            self._game.process_moves(move=move)

            if self._game.is_tied():
                # if there is a tied
                self._update_display(msg="Tied Game!", color='red')
            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg=msg, color=color)
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg=msg)


def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game=game)
    board.mainloop()


if __name__ == '__main__':
    main()

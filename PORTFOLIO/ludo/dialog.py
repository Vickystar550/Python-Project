from tkinter import *
import math


class Dialog(Toplevel):
    """A custom Tk button dialog. Get and store user selected choice"""

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title('Game Dialog')
        self.config(pady=10, padx=10, bg='black')
        self.minsize(width=800, height=400)
        self.transient(parent)
        self.protocol('WM_DELETE_WINDOW', self.closed)
        self.result = ''
        self.purpose = ''
        self.player_num_selected = False

    def question1(self, purpose: str):
        """choose the number of players or exit the game"""
        self.purpose = purpose.lower()

        if self.purpose in ('start', 'restart'):
            if self.purpose == 'start':
                self.label1_text = 'WELCOME\nplease make a selection'
            elif self.purpose == 'restart':
                self.label1_text = 'WELCOME\nglad to have you back'

            self.label1_fg = 'white'
            self.label2_text = f'how many players are you {purpose}ing with?'
            self.options = ('two', 'three', 'four')

        elif self.purpose == 'exit':
            self.label1_fg = 'red'
            self.label1_text = 'EXIT!'
            self.label2_text = 'Are you sure you want to exit?'
            self.options = ('exit', 'stay', 'restart')

        elif self.purpose == 'no selection':
            self.label1_fg = 'red'
            self.label1_text = 'OOPS! SELECTION REQUIRED!\nplease select one option'
            self.label2_text = 'how many players are you starting with?'
            self.options = ('two', 'three', 'four')

        outer_frame = Frame(master=self)
        outer_frame.pack()
        outer_frame.config(padx=20, pady=20, bg='#CC5500', highlightthickness=0)

        inner_frame = Frame(master=outer_frame)
        inner_frame.grid(row=0, column=0)
        inner_frame.config(padx=20, pady=20, bg='#1C0E25')

        label1 = Label(inner_frame, text=self.label1_text)
        label1.grid(row=0, column=0, columnspan=len(self.options), sticky='nsew')
        label1.config(pady=50, padx=20, font=('Serif', 25, 'normal'), justify='center', bg='#1C0E25', fg=self.label1_fg)

        label2 = Label(inner_frame, text=self.label2_text)
        label2.grid(row=1, column=0, columnspan=len(self.options), sticky='nsew')
        label2.config(pady=50, padx=20, font=('Arial', 15, 'normal'), justify='center', bg='#1C0E25', fg='sea green')

        column = 0
        for choice in self.options:
            btn = Button(master=inner_frame, text=choice.upper(),
                         command=lambda x=choice: self.set_option(option_selected=x))
            btn.grid(row=2, column=column, padx=(0, 10), pady=20, sticky='ew')
            btn.config(font=('Arial', 20, 'bold'), fg='sea green', activebackground='#CC5500',
                       bg='#2d2d2d', highlightthickness=0, border=5, width=8, highlightbackground='#2d2d2d')
            column += 1

    def question2(self, players: int):
        """choose the possible players/colors combo given the number of players"""
        # for 2 or 3 players
        if players == 2 or players == 3:
            players_combo = math.comb(4, players)

            if players_combo == 6:
                self.options = {
                    '(GREEN with Red) vs. (BLUE with Yellow)': ('Green', 'Blue'),
                    '(RED with Green) vs. (YELLOW with Blue)': ('Red', 'Yellow'),
                    '(GREEN with Yellow) vs. (BLUE with Red)': ('Green', 'Blue'),
                    '(YELLOW with Green) vs. (RED with Blue)': ('Red', 'Yellow'),
                }
                self.btn_width = 35
            elif players_combo == 4:
                self.options = {
                       ('Green', 'Red', 'Blue'): ('Green', 'Red', 'Blue'),
                       ('Green', 'Red', 'Yellow'): ('Green', 'Red', 'Yellow'),
                       ('Green', 'Blue', 'Yellow'): ('Green', 'Blue', 'Yellow'),
                       ('Red', 'Blue', 'Yellow'): ('Red', 'Blue', 'Yellow')
                }
                self.btn_width = 20

            outer_frame = Frame(master=self)
            outer_frame.pack()
            outer_frame.config(padx=20, pady=20, bg='#CC5500', highlightthickness=0)

            self.inner_frame = Frame(master=outer_frame)
            self.inner_frame.grid(row=0, column=0)
            self.inner_frame.config(padx=20, pady=20, bg='#1C0E25')

            label1 = Label(self.inner_frame, text='SELECT\nplease select your preferred player combo')
            label1.grid(row=0, column=0, sticky='nsew')
            label1.config(pady=50, padx=20, font=('Serif', 25, 'normal'), justify='center', bg='#1C0E25', fg='white')

            label2 = Label(self.inner_frame, text='Available colors/players are: Green, Red, Yellow and Blue')
            label2.grid(row=1, column=0, sticky='nsew')
            label2.config(pady=50, padx=20, font=('Arial', 15, 'normal'), justify='center', bg='#1C0E25',
                          fg='sea green')

            for combo in range(4):
                btn = Button(master=self.inner_frame, text=f'{list(self.options.keys())[combo]}',
                             command=lambda x=list(self.options.values())[combo]: self.set_option(option_selected=x))

                btn.grid(row=combo + 2, column=0, padx=(0, 10), pady=20, sticky='')
                btn.config(font=('Arial', 20, 'bold'), fg='sea green', activebackground='#CC5500',
                           bg='#2d2d2d', highlightthickness=0, border=5, width=self.btn_width,
                           highlightbackground='#2d2d2d')

            label3 = Label(self.inner_frame, text='Remember to click on the center button to start')
            label3.grid(row=players_combo+2, column=0, sticky='nsew')
            label3.config(pady=50, padx=20, font=('Arial', 15, 'normal'), justify='center', bg='#1C0E25',
                          fg='sea green')

        else:
            # for number of players other than 2, 3 i.e., 1, or 4
            self.set_option(option_selected=('Green', 'Red', 'Yellow', 'Blue'))

    def set_option(self, option_selected):
        """set the result or perform an action"""
        if self.purpose == 'exit':
            if option_selected == 'exit':
                self.parent.exit()
            elif option_selected == 'restart':
                self.parent.restart()
            else:
                self.destroy()

        else:
            self.result = option_selected
            self.player_num_selected = True
            self.destroy()

    def closed(self):
        """perform actions when window close button is clicked"""
        self.result = None
        self.destroy()

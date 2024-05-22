from tkinter import *
import tkinter as tk


class DisplayDialog(Toplevel):
    """A custom Dialog. Store the selected choice"""
    def __init__(self, parent, title: str, purpose: str):
        super().__init__(parent)
        self.title(title)
        self.config(pady=10, padx=10, bg='black')
        self.minsize(width=800, height=400)
        self.transient(parent)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.purpose = purpose

        if self.purpose == 'promotion':
            self.label_text = 'Congratulation!\nPlease Select Your Promoting Piece'
            self.options = ['rook', 'knight', 'bishop', 'queen']

        elif self.purpose == 'checkmate':
            self.label_text = 'Replay Game?'
            self.options = ['no', 'yes']

        elif self.purpose == 'exit':
            self.label_text = 'Are you sure you want to exit?'
            self.options = ['no', 'yes']

        self.result: str = ''

        self.create_display()

        # Ensure the window is updated before setting grab
        self.update_idletasks()
        self.grab_set()
        self.wait_window()

    def create_display(self):
        outer_frame = tk.Frame(master=self)
        outer_frame.pack()
        outer_frame.config(padx=20, pady=20, bg='#CC5500', highlightthickness=0)

        inner_frame = tk.Frame(master=outer_frame)
        inner_frame.grid(row=0, column=0)
        inner_frame.config(pady=20, padx=20, bg='#1C0E25')

        label = Label(inner_frame, text=self.label_text)
        label.grid(row=0, column=0, columnspan=len(self.options), sticky='nsew')
        label.config(pady=50, padx=20, font=('Serif', 20, 'normal'), justify='center', bg='#1C0E25')

        column = 0
        for choice in self.options:
            btn = Button(master=inner_frame, text=choice.upper(), command=lambda x=choice: self.set_option(x))
            btn.grid(row=1, column=column, padx=(0, 10), pady=20, sticky='ew')
            btn.config(font=('Arial', 20, 'bold'), fg='sea green', activebackground='#CC5500',
                       bg='#2d2d2d', highlightthickness=0, border=5, width=5, highlightbackground='#2d2d2d')
            column += 1

    def set_option(self, option_selected):
        self.result = option_selected
        self.destroy()

    def on_closing(self):
        self.result = None
        self.destroy()

import tkinter as tk
from button import MyButton
from function import Functions
from canvas import MyCanvas


class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('My Calculator')
        self.config(pady=20, padx=20, bg='black')
        self.minsize(width=700, height=900)

        # --------- primary frame ---------------------
        self.master_frame = tk.Frame(self)
        self.master_frame.pack(fill=tk.BOTH, expand=True)
        self.master_frame.config(padx=0, pady=0, bg='#1C0E25', highlightthickness=0, height=900, width=700)

        # --------------- mini frames --------------------
        self.screen_frame = tk.Frame(master=self.master_frame)
        self.screen_frame.grid(row=0, column=0)
        self.screen_frame.config(height=300, width=600, padx=0, bg='#2d2d2d')

        self.btn_frame = tk.Frame(master=self.master_frame)
        self.btn_frame.grid(row=1, column=0)
        self.btn_frame.config(height=600, width=600, pady=20, padx=10, bg='#1C0E25')
        # -----------------------------------------------

        MyButton(master=self.btn_frame, func=Functions(screen=MyCanvas(master=self.screen_frame)))

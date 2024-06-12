import tkinter as tk
from button import MyButton
from function import Functions
from canvas import MyCanvas


class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('My Calculator')
        self.config(pady=30, padx=20, bg='black')
        self.geometry('700x1050')
        self.minsize(width=700, height=1050)

        # --------- primary frame ---------------------
        self.master_frame = tk.Frame(self)
        self.master_frame.pack(fill=tk.BOTH, expand=False)
        self.master_frame.config(padx=0, pady=0, bg='#1C0E25', highlightthickness=0, height=900, width=700)

        # --------------- mini frames --------------------
        self.screen_frame = tk.Frame(master=self.master_frame)
        self.screen_frame.grid(row=0, column=0)
        self.screen_frame.config(height=300, width=600, padx=0, bg='#2d2d2d')

        self.btn_frame = tk.Frame(master=self.master_frame)
        self.btn_frame.grid(row=1, column=0, pady=20, padx=10)
        self.btn_frame.config(height=600, width=600, bg='#1C0E25', )
        # -----------------------------------------------

        self.my_functions = Functions(master=self, screen=MyCanvas(master=self.screen_frame))
        self.my_btn = MyButton(master=self.btn_frame, func=self.my_functions)

        self.activate_clock()

        # # ----------------- event bindings ----------------
        keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'parenright', 'parenleft',
                'plus', 'minus', 'slash', 'period', 'equal', 'asterisk',
                'percent', 'exclam', 'asciicircum', 'Delete']
        for key in keys:
            self.bind(f'<KeyPress-{key}>', self.my_functions.on_key_press)

        self.bind('<BackSpace>', self.my_functions.on_key_press)
        self.bind('<Return>', self.my_functions.on_key_press)
        self.bind('<Return>', self.my_functions.on_key_press)
        self.bind('<Control-q>', self.my_functions.on_key_press)

        # self.bind('<KeyPress>', self.work)

    def activate_clock(self):
        """activate clock every 1 millisecond"""
        self.clock_id = self.after(1, func=self.clock)

    def clock(self):
        """act like a clock function"""
        self.after_cancel(self.clock_id)
        self.my_btn.datetime_label.config(text=f'{self.my_functions.get_datetime()}')
        self.activate_clock()

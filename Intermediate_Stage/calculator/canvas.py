import tkinter as tk

FONT_NAME = "Courier"
DISPLAY_FONT = 'Arial'


class MyCanvas(tk.Canvas):
    def __init__(self, master: tk.Frame):
        super().__init__(master=master)
        self.config(bg='black', width=640, height=200)
        self.canvas_text = self.create_text(320, 100, text="Welcome", fill="white", justify='center',
                                            font=(FONT_NAME, 35, "normal"))
        self.grid(row=0, column=0, columnspan=5, pady=10, padx=10)

    def display(self, input_, purpose: str):
        """display input or result on the canvas or screen"""
        self.itemconfig(self.canvas_text, text='')
        if purpose == 'error':
            self.canvas_text = self.create_text(600, 100, text=input_, fill='white', justify='left',
                                                font=('Courier', 25, 'normal'), anchor='e', width=550)
        else:
            self.canvas_text = self.create_text(600, 100, text=input_, fill='white', justify='left',
                                                font=(FONT_NAME, 35, 'normal'), anchor='e', width=550)

    def ask_for_r(self):
        self.itemconfig(self.canvas_text, text='')
        self.canvas_text = self.create_text(600, 100, text='enter another number', fill='white', justify='left',
                                            font=('Courier', 25, 'normal'), anchor='e', width=550)

    def reset(self):
        self.itemconfig(self.canvas_text, text='')


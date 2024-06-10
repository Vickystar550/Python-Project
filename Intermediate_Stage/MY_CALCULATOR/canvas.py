import tkinter as tk

FONT_NAME = "Courier"


class MyCanvas:
    def __init__(self, master):
        self.canvas = tk.Canvas(master=master)
        self.canvas.config(bg='black',  width=640, height=200)
        self.canvas_text = self.canvas.create_text(320, 100, text="Welcome Home", fill="white", justify='center',
                                                   font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=5, pady=10, padx=10)

    def display_equals_to(self, result):
        self.canvas.itemconfig(self.canvas_text, text=result)

    def reset_canvas(self):
        self.canvas.itemconfig(self.canvas_text, text="Welcome")

    def ask_another_operation(self):
        self.canvas.itemconfig(self.canvas_text, text="Run another operation")

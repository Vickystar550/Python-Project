import tkinter as tk
from datetime import datetime
import random
from PIL import Image, ImageTk


class GameBoard(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__()
        copyright_year = datetime.now().year
        self.title(f'Ludo © {copyright_year} Victor Nice')
        self.config(pady=10, padx=0, bg='black')
        self.minsize(width=2000, height=1000)

        self.dices = None
        self.btn_cell = {}

        # ---------------- arrow image ------------
        self.downward_left = tk.PhotoImage(file='assets/arrows/downward_left.png')
        self.downward_right = tk.PhotoImage(file='assets/arrows/downward_right.png')
        self.upward_left = tk.PhotoImage(file='assets/arrows/upward_left.png')
        self.upward_right = tk.PhotoImage(file='assets/arrows/upward_right.png')

        self.centre_circle = tk.PhotoImage(file='assets/arrows/centre_circle.png')

        self.red_arrow = tk.PhotoImage(file='assets/arrows/red_arrow.png')
        self.green_arrow = tk.PhotoImage(file='assets/arrows/green_arrow.png')
        self.yellow_arrow = tk.PhotoImage(file='assets/arrows/yellow_arrow.png')
        self.blue_arrow = tk.PhotoImage(file='assets/arrows/blue_arrow.png')

        # ------------ home -----------------
        self.green_home = tk.PhotoImage(file='assets/home/green_home.png')
        self.red_home = tk.PhotoImage(file='assets/home/red_home.png')
        self.yellow_home = tk.PhotoImage(file='assets/home/yellow_home.png')
        self.blue_home = tk.PhotoImage(file='assets/home/blue_home.png')

        # ---------------- players -----------------
        self.red_player = ImageTk.PhotoImage(Image.open(fp='assets/players/ronaldo.jpg').resize((380, 350)))
        self.blue_player = ImageTk.PhotoImage(Image.open(fp='assets/players/lampard.jpeg').resize((380, 350)))
        self.yellow_player = ImageTk.PhotoImage(Image.open(fp='assets/players/neymar.jpg').resize((380, 350)))
        self.green_player = ImageTk.PhotoImage(Image.open(fp='assets/players/green_player.jpg').resize((380, 350)))

        # --------------- color -----
        self.green = '#008000'
        self.red = '#880808'
        self.yellow = '#8B8000'
        self.blue = '#00008B'
        self.theme = '#4D4D4D'

        self.create_frame()

    def create_frame(self):
        master_frame = tk.Frame(self)
        master_frame.pack(fill=tk.Y, expand=True)
        master_frame.config(padx=0, pady=0, bg='black', highlightthickness=0, height=1000, width=2000)

        self.panel_frame1 = tk.Frame(master=master_frame)
        self.panel_frame1.grid(row=0, column=0, padx=10, pady=10)
        self.panel_frame1.config(height=980, width=250, bg='black')

        self.board_frame = tk.Frame(master=master_frame, highlightthickness=10, highlightbackground=self.theme)
        self.board_frame.grid(row=0, column=1, padx=10, pady=10)
        # self.board_frame.config(height=950, width=1200, bg=self.theme)
        self.board_frame.config(height=1000, width=2000, bg=self.theme, padx=5, pady=5)

        # ------------------OVER-LAY LABEL -----------
        overlay_label_green = tk.Label(self.board_frame,
                                       bg=self.theme, width=380, height=350, anchor='center',
                                       image=self.green_player)
        overlay_label_green.place(x=0, y=0)

        overlay_label_yellow = tk.Label(self.board_frame,
                                        bg=self.theme, width=380, height=350, anchor='sw',
                                        image=self.yellow_player)
        overlay_label_yellow.place(x=610, y=0)

        overlay_label_red = tk.Label(self.board_frame,
                                     bg=self.red, width=380, height=350, anchor='ne',
                                     image=self.red_player)
        overlay_label_red.place(x=0, y=595)

        overlay_label_blue = tk.Label(self.board_frame,
                                      bg=self.blue, width=380, height=350, anchor='nw',
                                      image=self.blue_player)
        overlay_label_blue.place(x=610, y=595)

        # ------------------------------
        self.panel_frame2 = tk.Frame(master=master_frame)
        self.panel_frame2.grid(row=0, column=2, padx=10, pady=10)
        self.panel_frame2.config(height=980, width=250, bg='black')

        self.create_board_label()
        self.create_board_button()

    def create_board_label(self):
        # left corner label
        self.left_top_btn = tk.Button(master=self.panel_frame1)
        self.left_top_btn.grid(row=0, column=0, pady=(0, 50), padx=(0, 5))
        self.left_top_btn.config(bg=self.green, width=10, height=5, highlightthickness=0, border=5, fg='black',
                                 text='DICE'.upper(), font=('Courier', 20, 'bold'),
                                 activebackground=self.theme, activeforeground=self.green)
        self.left_top_btn.rowconfigure(0, weight=1, minsize=20)
        self.left_top_btn.columnconfigure(0, weight=1, minsize=10)
        self.left_top_btn.bind("<ButtonPress-1>", self.roll_dices)

        self.left_box_label = tk.Label(master=self.panel_frame1)
        self.left_box_label.grid(row=1, column=0, pady=(0, 50), padx=(0, 5))
        self.left_box_label.config(bg=self.theme, width=25, height=24, border=5)
        self.left_box_label.rowconfigure(1, weight=1, minsize=10)

        self.left_bottom_btn = tk.Button(master=self.panel_frame1)
        self.left_bottom_btn.grid(row=2, column=0, pady=(0, 5), padx=(0, 5))
        self.left_bottom_btn.config(bg=self.red, width=10, height=5, highlightthickness=0, border=5, fg='black',
                                    text='DICE'.upper(), font=('Courier', 20, 'bold'),
                                    activebackground=self.theme, activeforeground=self.red)
        self.left_bottom_btn.rowconfigure(2, weight=1, minsize=10)
        self.left_bottom_btn.bind("<ButtonPress-1>", self.roll_dices)
        # -------------------------------------------------------------

        self.right_top_btn = tk.Button(master=self.panel_frame2)
        self.right_top_btn.grid(row=0, column=0, pady=(0, 50), padx=(0, 5))
        self.right_top_btn.config(bg=self.yellow, width=10, height=5, highlightthickness=0, border=5, fg='black',
                                  text='DICE'.upper(), font=('Courier', 20, 'bold'),
                                  activebackground=self.theme, activeforeground=self.yellow)
        self.right_top_btn.rowconfigure(0, weight=1, minsize=20)
        self.right_top_btn.columnconfigure(0, weight=1, minsize=10)
        self.right_top_btn.bind("<ButtonPress-1>", self.roll_dices)

        self.right_box_label = tk.Label(master=self.panel_frame2)
        self.right_box_label.grid(row=1, column=0, pady=(0, 50), padx=(0, 5))
        self.right_box_label.config(bg=self.theme, width=25, height=24, border=5)
        self.right_box_label.rowconfigure(1, weight=1, minsize=10)

        self.right_bottom_btn = tk.Button(master=self.panel_frame2)
        self.right_bottom_btn.grid(row=2, column=0, pady=(0, 5), padx=(0, 5))
        self.right_bottom_btn.config(bg=self.blue, width=10, height=5, highlightthickness=0, border=5, fg='black',
                                     text='DICE'.upper(), font=('Courier', 20, 'bold'),
                                     activebackground=self.theme, activeforeground=self.blue)
        self.right_bottom_btn.rowconfigure(2, weight=1, minsize=10)
        self.right_bottom_btn.bind("<ButtonPress-1>", self.roll_dices)

    def create_board_button(self):
        # ------------------ MOVING CELLS ----------------------------
        # horizontal
        for r in [6, 7, 8]:
            for i in range(6):
                color_ = self.get_btn_color(r=r, c=i)

                cell = tk.Button(master=self.board_frame, width=5, height=3)
                cell.config(bg=color_, highlightthickness=0, activebackground='#1E1F22')
                cell.grid(row=r, column=i)
                self.btn_cell[(r, i)] = cell

            for i in range(10, 16):
                color_ = self.get_btn_color(r=r, c=i)
                cell = tk.Button(master=self.board_frame, width=5, height=3)
                cell.config(bg=color_, highlightthickness=0, activebackground='#1E1F22')
                cell.grid(row=r, column=i)
                self.btn_cell[(r, i)] = cell

        # vertical
        for c in [6, 7, 8]:
            for i in range(6):
                color_ = self.get_btn_color(r=i, c=c)
                cell = tk.Button(master=self.board_frame, width=5, height=3)
                cell.config(bg=color_, highlightthickness=0, activebackground='#1E1F22')
                cell.grid(row=i, column=c)
                self.btn_cell[(i, c)] = cell

            for i in range(10, 16):
                color_ = self.get_btn_color(r=i, c=c)
                cell = tk.Button(master=self.board_frame, width=5, height=3)
                cell.config(bg=color_, highlightthickness=0, activebackground='#1E1F22')
                cell.grid(row=i, column=c)
                self.btn_cell[(i, c)] = cell

        # -------------- HOME or CENTRE BUTTONS --------------------------
        middle_centre_btn = tk.Button(master=self.board_frame, width=55, height=55)
        middle_centre_btn.config(bg=self.theme, highlightthickness=0, image=self.centre_circle)
        middle_centre_btn.grid(row=7, column=7)
        self.btn_cell[(7, 7)] = middle_centre_btn

        left_centre_btn = tk.Button(master=self.board_frame, width=55, height=55)
        left_centre_btn.config(bg=self.green, highlightthickness=0, image=self.green_home)
        left_centre_btn.grid(row=7, column=6)
        self.btn_cell[(7, 6)] = left_centre_btn

        right_centre_btn = tk.Button(master=self.board_frame, width=55, height=55)
        right_centre_btn.config(bg=self.blue, highlightthickness=0, image=self.blue_home)
        right_centre_btn.grid(row=7, column=8)
        self.btn_cell[(7, 8)] = right_centre_btn

        up_centre_btn = tk.Button(master=self.board_frame, width=55, height=55)
        up_centre_btn.config(bg=self.yellow, highlightthickness=0, image=self.yellow_home)
        up_centre_btn.grid(row=6, column=7)
        self.btn_cell[(6, 7)] = up_centre_btn

        down_centre_btn = tk.Button(master=self.board_frame, width=55, height=55)
        down_centre_btn.config(bg=self.red, highlightthickness=0, image=self.red_home)
        down_centre_btn.grid(row=8, column=7)
        self.btn_cell[(8, 7)] = down_centre_btn

        # -------------- CENTRE DIRECTION ARROWS --------------------
        for r in [6, 8]:
            for c in [6, 8]:
                dir_btn = tk.Button(master=self.board_frame, width=5, height=3)
                dir_btn.config(bg='#1E1F22', highlightthickness=0)
                dir_btn.grid(row=r, column=c)
                self.btn_cell[(r, c)] = dir_btn

        for key, value in self.btn_cell.items():
            # ---------- ADDING DIRECTION ARROWS -----------------
            # ----- centre arrows
            if key == (6, 6):
                value.config(image=self.upward_right, width=55, height=55, state='disabled', bg=self.green)
            elif key == (6, 8):
                value.config(image=self.downward_right, width=55, height=55, state='disabled', bg=self.yellow)
            elif key == (8, 6):
                value.config(image=self.upward_left, width=55, height=55, state='disabled', bg=self.red)
            elif key == (8, 8):
                value.config(image=self.downward_left, width=55, height=55, state='disabled', bg=self.blue)

            # ----- edge arrows
            elif key == (7, 0):
                value.config(image=self.green_arrow, width=60, height=60, activebackground=self.green)
            elif key == (7, 15):
                value.config(image=self.blue_arrow, width=60, height=60, activebackground=self.blue)
            elif key == (0, 7):
                value.config(image=self.yellow_arrow, width=60, height=60, activebackground=self.yellow)
            elif key == (15, 7):
                value.config(image=self.red_arrow, width=60, height=60, activebackground=self.red)

            # ------- SETTING ACTIVE BACKGROUND COLOR FOR MOVING CELLS
            green_range = [(6, c) for c in range(6)] + [(r, 6) for r in range(6)]
            red_range = [(8, c) for c in range(6)] + [(r, 6) for r in range(9, 16)]
            yellow_range = [(r, 8) for r in range(6)] + [(6, c) for c in range(9, 16)]
            blue_range = [(r, 8) for r in range(9, 16)] + [(8, c) for c in range(9, 16)]

            if key in green_range and key not in [(6, 0), (6, 1)]:
                value.config(activebackground=self.green)

            elif key in red_range and key not in [(14, 6), (15, 6)]:
                value.config(activebackground=self.red)

            elif key in yellow_range and key not in [(0, 8), (1, 8)]:
                value.config(activebackground=self.yellow)

            elif key in blue_range and key not in [(8, 14), (8, 15)]:
                value.config(activebackground=self.blue)

    def get_btn_color(self, r, c):
        if (r == 7 and c in range(1, 6)) or (r == 6 and c == 1):
            return self.green  # dark green
        elif (r == 7 and c in range(10, 15)) or (r == 8 and c == 14):
            return self.blue  # dark blue

        elif (c == 7 and r in range(1, 6)) or (r == 1 and c == 8):
            return self.yellow  # yellow
        elif (c == 7 and r in range(10, 15)) or (r == 14 and c == 6):
            return self.red  # blood-red

        else:
            return '#1E1F22'

    def roll_dices(self, event):
        clicked_btn = event.widget
        color = clicked_btn.cget('bg')
        self.dices = random.randint(1, 6), random.randint(1, 6)

        if color == self.green:
            self.left_box_label.config(width=10, height=15, text=f'{self.dices}', font=('Arial', 20, 'bold'),
                                       fg=color, anchor='n')
        elif color == self.red:
            self.left_box_label.config(width=10, height=15, text=f'{self.dices}', font=('Arial', 20, 'bold'),
                                       fg=color, anchor='s')
        elif color == self.yellow:
            self.right_box_label.config(width=10, height=15, text=f'{self.dices}', font=('Arial', 20, 'bold'),
                                        fg=color, anchor='n')
        elif color == self.blue:
            self.right_box_label.config(width=10, height=15, text=f'{self.dices}', font=('Arial', 20, 'bold'),
                                        fg=color, anchor='s')

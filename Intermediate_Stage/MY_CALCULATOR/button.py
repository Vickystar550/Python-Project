import tkinter
from tkinter import *

FONT_NAME = "Arial"


class MyButton:
    def __init__(self, master, func):
        self.master = master
        self.func = func

        self.label = Label(self.master, text='Wed. 26th June 2024, 22:30pm')
        self.label.config(bg='green', fg='black', width=32, font=(FONT_NAME, 20, 'bold'))
        self.label.grid(row=0, column=0, columnspan=5, pady=(0, 10))

        self.zeroth_row_buttons(row=1)
        self.first_row_buttons(row=2)
        self.second_row_buttons(row=3)
        self.third_row_buttons(row=4)
        self.fouth_row_buttons(row=5)
        self.fifth_row_buttons(row=6)

    def zeroth_row_buttons(self, row):
        one_button = Button(master=self.master, text="1",
                            command=lambda: self.func.digits_or_operators("1"))
        one_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                          activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        one_button.grid(row=row, column=0, pady=10, padx=5)

        two_button = Button(master=self.master, text="2",
                            command=lambda: self.func.digits_or_operators("2"))
        two_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                          activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        two_button.grid(row=row, column=1, pady=10, padx=5)

        three_button = Button(master=self.master, text="3",
                              command=lambda: self.func.digits_or_operators("3"))
        three_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                            activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        three_button.grid(row=row, column=2, pady=10, padx=5)

        bmi_button = Button(master=self.master, text="bmi")
        bmi_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                          activeforeground='black', fg='white', bg='#2d2d2d')
        bmi_button.grid(row=row, column=3, pady=10, padx=5)

        plus_button = Button(master=self.master, text="+",
                             command=lambda: self.func.digits_or_operators("+"))
        plus_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                           activeforeground='black', fg='white', bg='#2d2d2d')
        plus_button.grid(row=row, column=4, pady=10, padx=5)

    def first_row_buttons(self, row):
        four_button = Button(master=self.master, text="4",
                             command=lambda: self.func.digits_or_operators("4"))
        four_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                           activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        four_button.grid(row=row, column=0, pady=10, padx=5)

        five_button = Button(master=self.master, text="5",
                             command=lambda: self.func.digits_or_operators("5"))
        five_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                           activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        five_button.grid(row=row, column=1, pady=10, padx=5)

        six_button = Button(master=self.master, text="6",
                            command=lambda: self.func.digits_or_operators("6"))
        six_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                          activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        six_button.grid(row=row, column=2, pady=10, padx=5)

        leap_button = Button(master=self.master, text="leap", width=5,
                             command=self.func.leap)
        leap_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                           activeforeground='black', fg='white', bg='#2d2d2d')
        leap_button.grid(row=row, column=3, pady=10, padx=5)

        minus_button = Button(master=self.master, text="-",
                              command=lambda: self.func.digits_or_operators("-"))
        minus_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                            activeforeground='black', fg='white', bg='#2d2d2d')
        minus_button.grid(row=row, column=4, pady=10, padx=5)

    def second_row_buttons(self, row):
        seven_button = Button(master=self.master, text="7",
                              command=lambda: self.func.digits_or_operators("7"))
        seven_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                            activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        seven_button.grid(row=row, column=0, pady=10, padx=5)

        eight_button = Button(master=self.master, text="8",
                              command=lambda: self.func.digits_or_operators("8"))
        eight_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                            activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        eight_button.grid(row=row, column=1, pady=10, padx=5)

        nine_button = Button(master=self.master, text="9",
                             command=lambda: self.func.digits_or_operators("9"))
        nine_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                           activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        nine_button.grid(row=row, column=2, pady=10, padx=5)

        palindrome_button = Button(self.master, text="palin")
        palindrome_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                                 activeforeground='black', fg='white', bg='#2d2d2d')
        palindrome_button.grid(row=row, column=3, pady=10, padx=5)

        divide_button = Button(master=self.master, text="/",
                               command=lambda: self.func.digits_or_operators("/"))
        divide_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                             activeforeground='black', fg='white', bg='#2d2d2d')
        divide_button.grid(row=row, column=4, pady=10, padx=5)

    def third_row_buttons(self, row):
        zero_button = Button(master=self.master, text="0",
                             command=lambda: self.func.digits_or_operators("0"))
        zero_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                           activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        zero_button.grid(row=row, column=0, pady=10, padx=5)

        dot_button = Button(master=self.master, text=".",
                            command=lambda: self.func.digits_or_operators("."))
        dot_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                          activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        dot_button.grid(row=row, column=1, pady=10, padx=5)

        percent_button = Button(master=self.master, text="%",
                                command=self.func.percent)
        percent_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                              activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        percent_button.grid(row=row, column=2, pady=10, padx=5)

        password_button = Button(master=self.master, text="pswd",
                                 command='')
        password_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                               activeforeground='black', fg='white', bg='#2d2d2d')
        password_button.grid(row=row, column=3, pady=10, padx=5)

        multiply_button = Button(master=self.master, text="*",
                                 command=lambda: self.func.digits_or_operators("*"))
        multiply_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                               activeforeground='black', fg='white', bg='#2d2d2d')
        multiply_button.grid(row=row, column=4, pady=10, padx=5)

    def fouth_row_buttons(self, row):
        open_parenthesis_button = Button(master=self.master, text="(",
                                         command=lambda: self.func.digits_or_operators("{("))
        open_parenthesis_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                                       activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        open_parenthesis_button.grid(row=row, column=1, pady=10, padx=5)

        exponent_button = Button(master=self.master, text="^",
                                 command='')
        exponent_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                               activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        exponent_button.grid(row=row, column=0, pady=10, padx=5)

        closing_parenthesis_button = Button(master=self.master, text=")",
                                            command=lambda: self.func.digits_or_operators(")}"))
        closing_parenthesis_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                                          activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        closing_parenthesis_button.grid(row=row, column=2, pady=10, padx=5)

        mod_button = Button(master=self.master, text="mod",
                            command=self.func.mod)
        mod_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                          activeforeground='black', fg='white', bg='#2d2d2d')
        mod_button.grid(row=row, column=3, pady=10, padx=5)

        equal_button = Button(master=self.master, text="=", command=self.func.equal_to)
        equal_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                            activeforeground='black', fg='white', bg='#2d2d2d')
        equal_button.grid(row=row, column=4, pady=10, padx=5)

    def fifth_row_buttons(self, row):
        weather_button = Button(master=self.master, text="check weather",
                                command='')
        weather_button.config(font=(FONT_NAME, 20, "bold"), width=20, height=2, activebackground='blue',
                              activeforeground='black', fg='white', bg='#2d2d2d')
        weather_button.grid(row=row, column=0, columnspan=3, pady=10, padx=5)

        factorial_button = Button(master=self.master, text="!",
                                  command=self.func.factorial)
        factorial_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                                activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        factorial_button.grid(row=row, column=3, pady=10, padx=5)

        off_button = Button(master=self.master, text="CE",
                            command='')
        off_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='red',
                          activeforeground='black', fg='white', bg='#2d2d2d')
        off_button.grid(row=row, column=4, pady=10, padx=5)

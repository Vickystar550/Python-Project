import tkinter
from tkinter import *

FONT_NAME = "Arial"


class MyButton:
    def __init__(self, master: Frame, func):
        self.master = master
        self.func = func

        self.datetime_label = Label(self.master, text=f'{self.func.get_datetime()}')
        self.datetime_label.config(bg='#4d4d4d', fg='black', width=35, font=(FONT_NAME, 20, 'bold'))
        self.datetime_label.grid(row=0, column=0, columnspan=5, pady=(0, 10))

        self.first_row(row=1)
        self.second_row(row=2)
        self.third_row(row=3)
        self.fourth_row(row=4)
        self.fifth_row(row=5)
        self.sixth_row(row=6)
        self.seventh_row(row=7)

    def first_row(self, row):
        one_button = Button(master=self.master, text="1",
                            command=lambda: self.func.cache_inputs("1"))
        one_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                          activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        one_button.grid(row=row, column=0, pady=10, padx=5)

        two_button = Button(master=self.master, text="2",
                            command=lambda: self.func.cache_inputs("2"))
        two_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                          activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        two_button.grid(row=row, column=1, pady=10, padx=5)

        three_button = Button(master=self.master, text="3",
                              command=lambda: self.func.cache_inputs("3"))
        three_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                            activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        three_button.grid(row=row, column=2, pady=10, padx=5)

        bmi_button = Button(master=self.master, text="bmi")
        bmi_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                          activeforeground='black', fg='white', bg='#2d2d2d')
        bmi_button.grid(row=row, column=3, pady=10, padx=5)

        plus_button = Button(master=self.master, text="+",
                             command=lambda: self.func.cache_inputs("+"))
        plus_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                           activeforeground='black', fg='white', bg='#2d2d2d')
        plus_button.grid(row=row, column=4, pady=10, padx=5)

    def second_row(self, row):
        four_button = Button(master=self.master, text="4",
                             command=lambda: self.func.cache_inputs("4"))
        four_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                           activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        four_button.grid(row=row, column=0, pady=10, padx=5)

        five_button = Button(master=self.master, text="5",
                             command=lambda: self.func.cache_inputs("5"))
        five_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                           activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        five_button.grid(row=row, column=1, pady=10, padx=5)

        six_button = Button(master=self.master, text="6",
                            command=lambda: self.func.cache_inputs("6"))
        six_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                          activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        six_button.grid(row=row, column=2, pady=10, padx=5)

        leap_button = Button(master=self.master, text="leap", width=5,
                             command=self.func.leap)
        leap_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                           activeforeground='black', fg='white', bg='#2d2d2d')
        leap_button.grid(row=row, column=3, pady=10, padx=5)

        minus_button = Button(master=self.master, text="-",
                              command=lambda: self.func.cache_inputs("-"))
        minus_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                            activeforeground='black', fg='white', bg='#2d2d2d')
        minus_button.grid(row=row, column=4, pady=10, padx=5)

    def third_row(self, row):
        seven_button = Button(master=self.master, text="7",
                              command=lambda: self.func.cache_inputs("7"))
        seven_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                            activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        seven_button.grid(row=row, column=0, pady=10, padx=5)

        eight_button = Button(master=self.master, text="8",
                              command=lambda: self.func.cache_inputs("8"))
        eight_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                            activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        eight_button.grid(row=row, column=1, pady=10, padx=5)

        nine_button = Button(master=self.master, text="9",
                             command=lambda: self.func.cache_inputs("9"))
        nine_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                           activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        nine_button.grid(row=row, column=2, pady=10, padx=5)

        palindrome_button = Button(self.master, text="palin")
        palindrome_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                                 activeforeground='black', fg='white', bg='#2d2d2d')
        palindrome_button.grid(row=row, column=3, pady=10, padx=5)

        divide_button = Button(master=self.master, text="/",
                               command=lambda: self.func.cache_inputs("/"))
        divide_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                             activeforeground='black', fg='white', bg='#2d2d2d')
        divide_button.grid(row=row, column=4, pady=10, padx=5)

    def fourth_row(self, row):
        zero_button = Button(master=self.master, text="0",
                             command=lambda: self.func.cache_inputs("0"))
        zero_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                           activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        zero_button.grid(row=row, column=0, pady=10, padx=5)

        dot_button = Button(master=self.master, text=".",
                            command=lambda: self.func.cache_inputs("."))
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
                                 command=lambda: self.func.cache_inputs("*"))
        multiply_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                               activeforeground='black', fg='white', bg='#2d2d2d')
        multiply_button.grid(row=row, column=4, pady=10, padx=5)

    def fifth_row(self, row):
        open_parenthesis_button = Button(master=self.master, text="(",
                                         command=lambda: self.func.cache_inputs("("))
        open_parenthesis_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                                       activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        open_parenthesis_button.grid(row=row, column=1, pady=10, padx=5)

        exponent_button = Button(master=self.master, text="^",
                                 command='')
        exponent_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                               activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        exponent_button.grid(row=row, column=0, pady=10, padx=5)

        closing_parenthesis_button = Button(master=self.master, text=")",
                                            command=lambda: self.func.cache_inputs(")"))
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

    def sixth_row(self, row):
        factorial_button = Button(master=self.master, text="n!",
                                  command=self.func.factorial)
        factorial_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                                activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        factorial_button.grid(row=row, column=0, pady=10, padx=5)

        permutation_button = Button(master=self.master, text="nPr", command=self.func.perm)
        permutation_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                                  activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        permutation_button.grid(row=row, column=1, pady=10, padx=5)

        combination_button = Button(master=self.master, text="nCr", command=self.func.comb)
        combination_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                                  activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        combination_button.grid(row=row, column=2, pady=10, padx=5)

        square_root_btn = Button(master=self.master, text="√", command=self.func.square_root)
        square_root_btn.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                               activeforeground='black', highlightthickness=0, fg='white', bg='#2d2d2d')
        square_root_btn.grid(row=row, column=3, pady=10, padx=5)

        enter_btn = Button(master=self.master, text="enter", command=self.func.equal_to)
        enter_btn.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                         activeforeground='black', fg='white', bg='#2d2d2d')
        enter_btn.grid(row=row, column=4, pady=10, padx=5)

    def seventh_row(self, row):
        weather_button = Button(master=self.master, text="weather",
                                command='')
        weather_button.config(font=(FONT_NAME, 20, "bold"), width=13, height=2, activebackground='blue',
                              activeforeground='black', fg='white', bg='#2d2d2d')
        weather_button.grid(row=row, column=0, columnspan=2, pady=10, padx=5)

        backspace_button = Button(master=self.master, text="back",
                                  command=self.func.backspace)
        backspace_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='green',
                                activeforeground='black', fg='white', bg='#2d2d2d')
        backspace_button.grid(row=row, column=2, pady=10, padx=5)

        cancel_button = Button(master=self.master, text="CE",
                               command=self.func.reset)
        cancel_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='green',
                             activeforeground='black', fg='white', bg='#2d2d2d')
        cancel_button.grid(row=row, column=3, pady=10, padx=5)

        off_button = Button(master=self.master, text="OFF",
                            command=self.func.exit)
        off_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='red',
                          activeforeground='black', fg='white', bg='#2d2d2d')
        off_button.grid(row=row, column=4, pady=10, padx=5)

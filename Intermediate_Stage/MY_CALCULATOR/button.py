from tkinter import *

FONT_NAME = "Arial"


class MyButton:
    def __init__(self, master, func):
        self.master = master
        self.func = func
        self.first_row_button()
        self.second_row_button()
        self.third_row_button()
        self.fourth_row_button()
        self.fifth_row_button()
        self.six_row_buttons()

    def first_row_button(self):
        one_button = Button(master=self.master, text="1",
                            command=lambda: self.func.digits_or_operators("1"))
        one_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                          activeforeground='black', highlightthickness=0)
        one_button.grid(row=0, column=0, pady=10, padx=5)

        two_button = Button(master=self.master, text="2",
                            command=lambda: self.func.digits_or_operators("2"))
        two_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                          activeforeground='black', highlightthickness=0)
        two_button.grid(row=0, column=1, pady=10, padx=5)

        three_button = Button(master=self.master, text="3",
                              command=lambda: self.func.digits_or_operators("3"))
        three_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                            activeforeground='black', highlightthickness=0)
        three_button.grid(row=0, column=2, pady=10, padx=5)

        bmi_button = Button(master=self.master, text="bmi")
        bmi_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                          activeforeground='black')
        bmi_button.grid(row=0, column=3, pady=10, padx=5)

        plus_button = Button(master=self.master, text="+",
                             command=lambda: self.func.digits_or_operators("+"))
        plus_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                           activeforeground='black')
        plus_button.grid(row=0, column=4, pady=10, padx=5)

    def second_row_button(self):
        four_button = Button(master=self.master, text="4",
                             command=lambda: self.func.digits_or_operators("4"))
        four_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4D4D4D',
                           activeforeground='black', highlightthickness=0)
        four_button.grid(row=1, column=0, pady=10, padx=5)

        five_button = Button(master=self.master, text="5",
                             command=lambda: self.func.digits_or_operators("5"))
        five_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                           activeforeground='black', highlightthickness=0)
        five_button.grid(row=1, column=1, pady=10, padx=5)

        six_button = Button(master=self.master, text="6",
                            command=lambda: self.func.digits_or_operators("6"))
        six_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                          activeforeground='black', highlightthickness=0)
        six_button.grid(row=1, column=2, pady=10, padx=5)

        leap_button = Button(master=self.master, text="leap", width=5,
                             command=self.func.leap)
        leap_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                           activeforeground='black')
        leap_button.grid(row=1, column=3, pady=10, padx=5)

        minus_button = Button(master=self.master, text="-",
                              command=lambda: self.func.digits_or_operators("-"))
        minus_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                            activeforeground='black')
        minus_button.grid(row=1, column=4, pady=10, padx=5)

    def third_row_button(self):
        seven_button = Button(master=self.master, text="7",
                              command=lambda: self.func.digits_or_operators("7"))
        seven_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                            activeforeground='black', highlightthickness=0)
        seven_button.grid(row=2, column=0, pady=10, padx=5)

        eight_button = Button(master=self.master, text="8",
                              command=lambda: self.func.digits_or_operators("8"))
        eight_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                            activeforeground='black', highlightthickness=0)
        eight_button.grid(row=2, column=1, pady=10, padx=5)

        nine_button = Button(master=self.master, text="9",
                             command=lambda: self.func.digits_or_operators("9"))
        nine_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                           activeforeground='black', highlightthickness=0)
        nine_button.grid(row=2, column=2, pady=10, padx=5)

        palindrome_button = Button(self.master, text="palin")
        palindrome_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                                 activeforeground='black')
        palindrome_button.grid(row=2, column=3, pady=10, padx=5)

        divide_button = Button(master=self.master, text="/",
                               command=lambda: self.func.digits_or_operators("/"))
        divide_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                             activeforeground='black')
        divide_button.grid(row=2, column=4, pady=10, padx=5)

    def fourth_row_button(self):
        zero_button = Button(master=self.master, text="0",
                             command=lambda: self.func.digits_or_operators("0"))
        zero_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                           activeforeground='black', highlightthickness=0)
        zero_button.grid(row=3, column=0, pady=10, padx=5)

        dot_button = Button(master=self.master, text=".",
                            command=lambda: self.func.digits_or_operators("."))
        dot_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                          activeforeground='black', highlightthickness=0)
        dot_button.grid(row=3, column=1, pady=10, padx=5)

        percent_button = Button(master=self.master, text="%",
                                command=self.func.percent)
        percent_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                              activeforeground='black', highlightthickness=0)
        percent_button.grid(row=3, column=2, pady=10, padx=5)

        password_button = Button(master=self.master, text="pswd",
                                 command='')
        password_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                               activeforeground='black')
        password_button.grid(row=3, column=3, pady=10, padx=5)

        multiply_button = Button(master=self.master, text="*",
                                 command=lambda: self.func.digits_or_operators("*"))
        multiply_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                               activeforeground='black')
        multiply_button.grid(row=3, column=4, pady=10, padx=5)

    def fifth_row_button(self):
        open_parenthesis_button = Button(master=self.master, text="(",
                                         command=lambda: self.func.digits_or_operators("{("))
        open_parenthesis_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                                       activeforeground='black', highlightthickness=0)
        open_parenthesis_button.grid(row=4, column=1, pady=10, padx=5)

        factorial_button = Button(master=self.master, text="!",
                                  command=self.func.factorial)
        factorial_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                                activeforeground='black', highlightthickness=0)
        factorial_button.grid(row=4, column=0, pady=10, padx=5)

        closing_parenthesis_button = Button(master=self.master, text=")",
                                            command=lambda: self.func.digits_or_operators(")}"))
        closing_parenthesis_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#4d4d4d',
                                          activeforeground='black', highlightthickness=0)
        closing_parenthesis_button.grid(row=4, column=2, pady=10, padx=5)

        mod_button = Button(master=self.master, text="mod",
                            command=self.func.mod)
        mod_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#808080',
                          activeforeground='black')
        mod_button.grid(row=4, column=3, pady=10, padx=5)

        equal_button = Button(master=self.master, text="=", command=self.func.equal_to)
        equal_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='#CC5500',
                            activeforeground='black')
        equal_button.grid(row=4, column=4, pady=10, padx=5)

    def six_row_buttons(self):
        weather_button = Button(master=self.master, text="check weather",
                                command='')
        weather_button.config(font=(FONT_NAME, 20, "bold"), width=20, height=2, activebackground='blue',
                              activeforeground='black')
        weather_button.grid(row=5, column=0, columnspan=3, pady=10, padx=5)

        reset_button = Button(master=self.master, text="CE", width=5,
                              command=self.func.reset)
        reset_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='green',
                            activeforeground='black')
        reset_button.grid(row=5, column=3, pady=10, padx=5)

        off_button = Button(master=self.master, text="OFF",
                            command='')
        off_button.config(font=(FONT_NAME, 20, "bold"), width=5, height=2, activebackground='red',
                          activeforeground='black')
        off_button.grid(row=5, column=4, pady=10, padx=5)

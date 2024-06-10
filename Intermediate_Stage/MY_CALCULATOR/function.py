import math


class Functions:
    def __init__(self, screen):
        self.my_canvas = screen
        self.cached_string = f""
        self.result = None
        self.is_there_previous_operation = False

    # ---- caching digits or operator -------
    def digits_or_operators(self, input_string: str):
        self.cached_string += input_string

    def equal_to(self):
        self.trial_function(self.cached_string)

    def trial_function(self, func):
        try:
            self.result = eval(func)
        except ZeroDivisionError:
            formatted_answer = "Undefined"
            self.my_canvas.display_equals_to(formatted_answer)
        else:
            formatted_answer = f"Result: {self.result}"
            print(self.result)
            self.my_canvas.display_equals_to(formatted_answer)
        finally:
            self.cached_string = ""

    def mod(self):
        self.cached_string += "%"

    def percent(self):
        result = float(self.cached_string) / 100
        self.cached_string = ""
        print(result)

    def factorial(self):
        positive_integer = int(self.cached_string)
        result = math.factorial(positive_integer)
        self.cached_string = ""
        print(result)

    def leap(self):
        year = int(self.cached_string)
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            print("leap year")
        elif year % 4 == 0 and year % 100 != 0:
            print("leap year")
        else:
            print("Not a leap year")

        self.cached_string = ""

    def reset(self):
        self.my_canvas.reset_canvas()

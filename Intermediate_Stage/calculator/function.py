import math
import time
import tkinter as tk


class Functions:
    def __init__(self, master: tk.Tk, screen):
        self.master = master
        self.my_canvas = screen
        self.cached_string = ""
        self.result = None
        self.is_there_previous_operation = False
        self.permutate = False
        self.combinatorial = False
        self.enable_pemdas = False

    def get_datetime(self):
        """return the current date and time string"""
        year = time.strftime('%Y')
        month = time.strftime('%B')
        day = time.strftime('%d')
        hr = time.strftime('%l')
        minute = time.strftime('%M')
        day_name = time.strftime('%a')
        am_pm = time.strftime('%p')
        time_zone = time.strftime('%Z')

        if day in (1, 21, 31):
            day = f'{day}st'
        elif day in (2, 22):
            day = f'{day}nd'
        elif day in (3, 23):
            day = f'{day}rd'
        else:
            day = f'{day}th'

        date_str = f'{day_name} {day} {month} {year}'
        time_str = f'{hr}:{minute}{am_pm} {time_zone}'

        return f'{date_str};  {time_str}'

    def on_key_press(self, event):
        """KeyPress event binding function"""
        if event.keysym in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            self.cache_inputs(input_string=event.char)
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Return' or event.keysym == 'equal':
            self.equal_to()
        elif event.keysym == 'q':
            self.exit()
        elif event.keysym == 'Delete':
            self.reset()
        elif event.keysym == 'parenright':
            self.cache_inputs(input_string=')')
        elif event.keysym == 'parenleft':
            self.cache_inputs(input_string='(')
        elif event.keysym == 'minus':
            self.cache_inputs(input_string='-')
        elif event.keysym == 'plus':
            self.cache_inputs(input_string='+')
        elif event.keysym == 'slash':
            self.cache_inputs(input_string='/')
        elif event.keysym == 'period':
            self.cache_inputs(input_string='.')
        elif event.keysym == 'asterisk':
            self.cache_inputs(input_string='*')
        elif event.keysym == 'percent':
            self.percent()
        elif event.keysym == 'exclam':
            self.factorial()
        elif event.keysym == 'asciicircum':
            self.cache_inputs(input_string='**')

    def cache_inputs(self, input_string: str):
        """"cache the user arithmetic digits, symbols or operators"""
        if input_string == '(':
            self.enable_pemdas = True
        self.cached_string += input_string
        self.my_canvas.display(input_=self.cached_string, purpose='input')

    def equal_to(self):
        if self.permutate or self.combinatorial:
            first_num = int(self.first_cache)
            second_num = int(self.cached_string)
            if self.permutate:
                result = math.perm(first_num, second_num)
            else:
                result = math.comb(first_num, second_num)
            self.my_canvas.display(input_=result, purpose='result')
            self.cached_string = ''
        elif self.enable_pemdas:
            self.arithmetic_processor(eval_string=self.pemdas())
        else:
            self.arithmetic_processor(self.cached_string)

    def arithmetic_processor(self, eval_string):
        """process an arithmetic calculation"""
        try:
            self.result = eval(eval_string)
        except SyntaxError:
            pass
        except ZeroDivisionError:
            self.my_canvas.display(input_='Undefined', purpose='result')
        else:
            print(self.result)
            self.my_canvas.display(input_=self.result, purpose='result')
        finally:
            self.cached_string = ""

    def mod(self):
        self.cached_string += "%"
        self.my_canvas.ask_for_r()

    def perm(self):
        self.permutate = True
        self.first_cache = self.cached_string
        self.cached_string = ''
        self.my_canvas.ask_for_r()

    def comb(self):
        self.combinatorial = True
        self.first_cache = self.cached_string
        self.cached_string = ''
        self.my_canvas.ask_for_r()

    def percent(self):
        result = float(self.cached_string) / 100
        self.cached_string = ""
        self.my_canvas.display(input_=result, purpose='result')

    def square_root(self):
        # how do you check if a string is a float?

        try:
            num = float(self.cached_string)
        except ValueError:
            self.my_canvas.display(input_=f'ValueError', purpose='error')
        else:
            self.my_canvas.display(input_=f'{math.sqrt(num):.2f}', purpose='result')
        finally:
            self.cached_string = ""

    def factorial(self):
        try:
            positive_integer = int(self.cached_string)
            result = math.factorial(positive_integer)
        except ValueError:
            self.my_canvas.display(input_='ValueError: enter only positive integer', purpose='error')
        else:
            self.my_canvas.display(input_=result, purpose='result')
        finally:
            self.cached_string = ""

    def leap(self):
        try:
            year = int(self.cached_string)
        except ValueError:
            self.my_canvas.display(input_='ValueError: enter year', purpose='error')
        else:
            if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
                self.my_canvas.display(input_='A leap year', purpose='result')
            elif year % 4 == 0 and year % 100 != 0:
                self.my_canvas.display(input_='A leap year', purpose='result')
            else:
                self.my_canvas.display(input_='Not a leap year', purpose='result')
        finally:
            self.cached_string = ""

    def reset(self):
        self.cached_string = ''
        self.my_canvas.reset()

    def backspace(self):
        self.cached_string = self.cached_string[:-1]
        self.my_canvas.display(input_=self.cached_string, purpose='input')

    def exit(self):
        """exit the program"""
        self.master.destroy()

    def pemdas(self):
        index1 = self.cached_string.find('(')
        index2 = self.cached_string.find(')')

        result = eval(self.cached_string[index1 + 1:index2])
        print(f'{self.cached_string[:index1]}*{result}')
        return f'{self.cached_string[:index1]}*{result}'

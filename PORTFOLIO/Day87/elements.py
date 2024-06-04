import turtle
from turtle import Turtle

GREEN = '#008000'
RED = '#880808'
YELLOW = '#8B8000'
BLUE = '#00008B'
THEME = '#4D4D4D'


class Borderline(Turtle):
    """create the borderline"""

    def __init__(self):
        super().__init__()
        self.color(RED)
        self.pen(speed=0, pensize=10)
        self.hideturtle()
        self.penup()
        self.goto(400, -500)
        self.pendown()
        self.goto(400, 350)
        self.goto(-400, 350)
        self.goto(-400, -500)
        self.goto(400, -500)

        self.display_name()

    def display_name(self):
        self.penup()
        self.home()
        self.goto(0, 470)
        self.pendown()
        self.color('sea green')
        self.write('BREAKOUT', align='center', font=('San Serif', 25, 'bold'))


class Bricks(Turtle):
    def __init__(self, rol, col, color: str):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.speed(0)
        self.color(color)
        self.shapesize(0.5, 2)
        self.penup()
        self.goto(rol, col)
        self.showturtle()

        if color == 'yellow':
            self.damage_score = 1
        elif color == 'green':
            self.damage_score = 3
        elif color == 'orange':
            self.damage_score = 5
        elif color == 'red':
            self.damage_score = 7
        else:
            self.damage_score = 0


class Element:
    """the game elements (bricks)"""

    def __init__(self):
        Borderline()

        self.bricks = {}
        self.create_bricks()

    def create_bricks(self):
        """create bricks"""
        columns_dict = {
            130: 'yellow',
            150: 'yellow',
            180: 'green',
            200: 'green',
            230: 'orange',
            250: 'orange',
            280: 'red',
            300: 'red'
        }

        try:
            for col in columns_dict.keys():
                color = columns_dict[col]

                for rol in range(-350, 400, 50):
                    brick = Bricks(rol=rol, col=col, color=color)

                    # storing each brick instance
                    self.bricks.update(
                        {(rol, col): brick}
                    )
        except turtle.Terminator:
            pass

    def reset_bricks(self):
        """clear all bricks off the screen and create it again"""
        for bricks in self.bricks.values():
            bricks.reset()
        self.create_bricks()


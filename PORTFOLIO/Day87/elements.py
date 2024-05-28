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
        self.goto(400, 400)
        self.goto(-400, 400)
        self.goto(-400, -500)
        self.goto(400, -500)

        self.display_name()

    def display_name(self):
        self.penup()
        self.home()
        self.goto(0, 470)
        self.pendown()
        self.color('sea green')
        self.write('BREAKOUT', align='center', font=('Serif', 25, 'bold'))


class Element:
    """the game elements (bricks)"""
    def __init__(self):
        Borderline()

        self.bricks = {}
        self.create_bricks()

    def create_bricks(self):
        """create bricks"""
        columns_dict = {
            180: 'yellow',
            200: 'yellow',
            230: 'green',
            250: 'green',
            280: 'orange',
            300: 'orange',
            330: 'red',
            350: 'red'
        }

        for col in columns_dict.keys():
            color = columns_dict[col]
            for rol in range(-350, 400, 50):
                brick = Turtle('square')
                brick.hideturtle()
                brick.speed(0)
                brick.color(color)
                brick.shapesize(0.5, 2)
                brick.penup()
                brick.goto(rol, col)
                brick.showturtle()

                # storing each brick instance
                self.bricks.update(
                    {(rol, col): brick}
                )

from turtle import Turtle

MOVE_STEP = 10
STRETCH_LEN = 8


class Paddle(Turtle):
    """create the paddle"""
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.penup()
        self.goto(0, -420)
        self.showturtle()
        self.shapesize(stretch_wid=1, stretch_len=STRETCH_LEN)
        self.move_step = MOVE_STEP

    def go_right(self):
        """moves the paddle right"""
        if self.xcor() <= 300:
            self.goto(self.xcor() + self.move_step, self.ycor())

    def go_left(self):
        """moves the paddle left"""
        if self.xcor() >= -300:
            self.goto(self.xcor() - self.move_step, self.ycor())

    def shrink(self):
        """shrink the paddle by half its length"""
        self.shapesize(1, STRETCH_LEN/2)

    def extend(self):
        """extend the paddle to its full length"""
        self.shapesize(1, STRETCH_LEN)

from turtle import Turtle

MOVE_STEP = 10


class Paddle(Turtle):
    """create the paddle"""
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.penup()
        self.goto(0, -350)
        self.showturtle()
        self.shapesize(1, 5)
        self.move_step = MOVE_STEP

    def go_right(self):
        self.speed('fast')
        if self.xcor() <= 300:
            self.goto(self.xcor() + self.move_step, self.ycor())

    def go_left(self):
        self.speed('fast')
        if self.xcor() >= -300:
            self.goto(self.xcor() - self.move_step, self.ycor())

from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=10, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves the paddles by some distance up"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle by some distance down"""
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


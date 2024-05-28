from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('purple')
        self.penup()
        self.shapesize(1, 1)
        self.x_move = 1
        self.y_move = 36
        self.goto(0, -250)
        self.move_speed = 0.1

    def move(self):
        """moves the ball the same distance in both directions"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """negate the vertical move parameter"""
        self.move_speed *= 0.7
        self.y_move *= -1

    def bounce_x(self):
        """negate the horizontal move parameter"""
        self.x_move *= -1

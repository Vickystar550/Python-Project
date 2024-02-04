from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x_move = 10  # the horizontal move parameter
        self.y_move = 10  # the vertical move parameter
        self.move_speed = 0.1

    def move(self):
        """Move the ball by same distance in both coordinate"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """negate the vertical move parameter"""
        self.y_move *= -1

    def bounce_x(self):
        """negate the horizontal move parameter"""
        # self.move_speed *= 0.9
        self.x_move *= -1

    def reset_position(self):
        """this reset the ball to the origin, and calls the bounce_x method"""
        self.goto((0, 0))
        self.bounce_x()

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        """Move the player object a certain distance"""
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        """Returns the player object to the starting position"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Checks if player object is at finish line"""
        return self.ycor() >= FINISH_LINE_Y

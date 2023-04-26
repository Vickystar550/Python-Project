from turtle import Turtle
import random


class Food(Turtle):
    """ this class create & instantiate the food (i.e. bait) to be eaten by the snake """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5, 1)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """ it refreshes and randomize the food location on the canvas screen """
        x = random.randrange(-580, 600, 20)
        y = random.randrange(-280, 300, 20)
        self.goto(x, y)



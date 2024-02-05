from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.fleet = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """This function randomly create a car object according to random chance"""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.fleet.append(new_car)

    def move_car(self):
        """Move each car object in the fleet"""
        for car in self.fleet:
            car.backward(self.move_speed)

    def increase_speed(self):
        """Increase the car object speed"""
        self.move_speed += MOVE_INCREMENT

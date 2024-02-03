from turtle import Turtle, Screen
import heroes
import random

vicky = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("white")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_square():
    for _ in range(4):
        vicky.forward(100)
        vicky.left(90)


def draw_dash_line():
    for _ in range(10):
        vicky.forward(20)
        vicky.penup()
        vicky.forward(20)
        vicky.pendown()


def draw_polygon(side):
    for i in range(side):
        angle = 360 / side
        vicky.forward(100)
        vicky.left(angle)


# for k in range(3, 11):
#     vicky.color(random.choice(colours))
#     draw_polygon(k)


def random_walk():
    for _ in range(20):
        direction = [45, 90, 135, 180, -45, -90, -135, -180, 225, 270, 315, 360, -225, -270, -315, -360]
        vicky.color(random_color())
        vicky.setheading(random.choice(direction))
        vicky.speed('fastest')
        vicky.pensize(10)
        vicky.forward(100)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        vicky.color(random_color())
        vicky.speed('fastest')
        vicky.circle(100)
        vicky.setheading(vicky.heading() + size_of_gap)


screen.exitonclick()

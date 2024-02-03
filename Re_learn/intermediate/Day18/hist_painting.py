import random
import colorgram
from turtle import Turtle, Screen


rgb_list = colorgram.extract("hirst_paint.jpeg", 30)
color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in rgb_list]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


vicky = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")


vicky.penup()
vicky.hideturtle()
vicky.speed("fastest")
vicky.setheading(225)
vicky.forward(300)
vicky.setheading(0)
num_of_dots = 100

# drawing dots with turtle:
for dot_count in range(1, num_of_dots + 1):
    vicky.dot(20, random.choice(color_list))
    vicky.fd(50)

    if dot_count % 10 == 0:
        vicky.setheading(90)
        vicky.forward(50)
        vicky.setheading(180)
        vicky.forward(500)
        vicky.setheading(0)


screen.exitonclick()

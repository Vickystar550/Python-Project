from turtle import Turtle, Screen

# create a Turtle, Screen class objects, set screen colormode and background color
vikky = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

# move turtle object to an arbitrary position (-300, -375); increase its speed; hide the pen while doing this
vikky.penup()
vikky.hideturtle()
vikky.goto(-300, -375)
vikky.speed("fastest")


def produce_color():
    """ this function return a list of generated rgb color tuples gotten from an JPEG file """
    import colorgram
    image = colorgram.extract('peacock.jpeg', 100)

    color_list = []
    for _ in image:
        color_list.append((_.rgb.r, _.rgb.g, _.rgb.b))
    return color_list


color = produce_color()


def draw_dot():
    """ this create dots on the screen """
    import random
    for _ in range(10):
        vikky.dot(20, random.choice(color))
        vikky.penup()
        vikky.fd(40)
        vikky.pendown()


def turn_left():
    """ turns the turtle orientation left before drawing dots """
    vikky.penup()
    vikky.left(90)
    vikky.fd(40)
    vikky.left(90)
    vikky.fd(40)
    vikky.pendown()


def turn_right():
    """ turns the turtle orientation right before drawing dots """
    vikky.penup()
    vikky.right(90)
    vikky.fd(40)
    vikky.right(90)
    vikky.fd(40)
    vikky.pendown()


def first_draw():
    """ draw the first row of dots and that after the turn_right() is activated """
    draw_dot()
    turn_left()


def second_draw():
    """ draw the second row of dots and that after the turn_left() is activated """
    draw_dot()
    turn_right()


for i in range(10):
    first_draw()
    second_draw()

screen.exitonclick()

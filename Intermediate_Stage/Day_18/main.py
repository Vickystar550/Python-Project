from turtle import Turtle, Screen

vikky = Turtle()
screen = Screen()


def draw_square():
    """draw a square"""
    for _ in range(4):
        vikky.forward(100)
        vikky.left(90)

        screen.exitonclick()


def draw_square_():
    """draw a square using the goto method"""
    vikky.goto(100, 0)
    vikky.goto(100, 100)
    vikky.goto(0, 100)
    vikky.goto(0, 0)

    screen.exitonclick()


def draw_dash_line():
    """draw dash lines"""
    vikky.hideturtle()

    for _ in range(20):
        vikky.fd(10)
        vikky.penup()
        vikky.fd(10)
        vikky.pendown()

    vikky.showturtle()
    screen.exitonclick()


def draw_polygons():
    """draw different polygons"""
    color_list = ['red', 'blue', 'brown', 'yellow', 'orange', 'maroon', 'green', 'violet']
    for _ in range(3, 11):
        angle = 360 / _
        vikky.color(color_list[_ - 3])

        for i in range(_):  # producing each polygon
            vikky.fd(100)
            vikky.right(angle)

    screen.exitonclick()


def random_walk():
    """ produce a random walk """
    import random
    angle_list = [0, 90, 180, 270]
    vikky.pensize(5)
    vikky.speed("fastest")

    for _ in range(100):
        vikky.color(random_color())
        vikky.fd(30)
        vikky.setheading(random.choice(angle_list))
    screen.exitonclick()


def random_color():
    """ returns a random color as rgb tuple """
    import random
    screen.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# draw a spirograph
def draw_spirograph():
    """ draw a spirograph """
    screen.bgcolor("black")  # set the canvas background color to black
    vikky.speed("fastest")
    vikky.hideturtle()
    for _ in range(0, 365, 5):
        vikky.color(random_color())
        # set heading
        vikky.setheading(_)
        vikky.circle(200)
    screen.exitonclick()

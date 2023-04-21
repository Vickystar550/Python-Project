from turtle import Turtle, Screen

# screen
screen = Screen()
screen.bgcolor('lightblue')
screen.listen()

# turtle
vikky = Turtle()
vikky.color('red')
vikky.shape('turtle')


def go_home():
    # this function take the turtle to its starting position
    vikky.penup()
    vikky.home()
    vikky.pendown()


def random_color():
    """ returns a random color as rgb tuple """
    import random
    screen.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# keyboard event
screen.onkey(lambda: vikky.setheading(0), 'Right')  # turn the turtle to the right
screen.onkey(lambda: vikky.setheading(90), 'Up')  # turn the turtle to up
screen.onkey(lambda: vikky.setheading(270), 'Down')  # turn the turtle down
screen.onkey(lambda: vikky.setheading(180), 'Left')  # turn the turtle left
screen.onkey(fun=lambda: vikky.clear(), key='c')  # clear the screen
screen.onkey(go_home, 'h')  # return the turtle to the starting position.
screen.onkey(key="space", fun=lambda: vikky.fd(100))  # move the turtle by 100 when the space key is pressed


# mouse event function
def click_left(x, y):
    vikky.color(random_color())


def click_right(x, y):
    vikky.stamp()


# mouse event
screen.onclick(fun=click_right, btn=3)  # btn 3 is for Right Mouse Button
screen.onclick(fun=click_left, btn=1)  # btn 1 is for Left Mouse Button


screen.mainloop()  # must be the last statement

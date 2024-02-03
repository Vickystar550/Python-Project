from turtle import Turtle, Screen

vicky = Turtle()
screen = Screen()


def move_forward():
    vicky.forward(100)


def move_backward():
    vicky.backward(100)


def turn_left():
    vicky.setheading(vicky.heading() + 10)
    # or vicky.left(10)


def turn_right():
    vicky.right(10)


def clear_screen():
    vicky.penup()
    vicky.speed("fastest")
    vicky.home()
    screen.clear()
    vicky.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=clear_screen, key="c")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")

screen.mainloop()



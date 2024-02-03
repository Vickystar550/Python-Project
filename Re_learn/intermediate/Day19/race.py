import random
from turtle import Turtle, Screen

# Create the screen object, set attributes and methods
screen = Screen()
screen.setup(width=1500, height=500)


def create_turtle_object():
    """This function create turtle objects and assign attributes, methods to each instance of the object
    returns a list of created turtle objects"""
    color_list = ["blue", "orange", "green", "yellow", "black", "pink", "red", "violet", "brown"]
    turtle_object_list = [Turtle() for _ in range(9)]
    turtle_coordinate = [(-700, x) for x in range(-200, 250, 50)]
    for t in turtle_object_list:
        t.hideturtle()
        t.shape("turtle")
        t.penup()
        t.speed("fastest")
        t.color(color_list[turtle_object_list.index(t)])
        t.goto(turtle_coordinate[turtle_object_list.index(t)])
        t.showturtle()

    return turtle_object_list


def finish_line():
    """This function create the finish line for the race"""
    line = Turtle()
    line.hideturtle()
    line.speed("fastest")
    line.color("gold")
    line.penup()
    line.goto(x=700, y=-250)
    line.pendown()
    line.pensize(5)
    line.goto(x=700, y=250)


# Get the user bet:
user = screen.textinput(title="Make a BET", prompt="Which turtle will win the race? Enter a color:")
is_race_on = False
if user:
    is_race_on = True

finish_line()
all_turtles = create_turtle_object()
while is_race_on:
    for k in all_turtles:
        # Check if each racing turtle object has crossed the finish line:
        if k.xcor() > 700:
            is_race_on = False
            # Get the winning turtle color:
            winning_turtle = k.pencolor()
            if winning_turtle == user:
                print(f"You've won! The {winning_turtle} is the winner")
            else:
                print(f"You've lost! The {winning_turtle} is the winner")

        # move each racing turtle by a random forward distance between 0 and 10:
        k.forward(random.randint(0, 10))


screen.mainloop()

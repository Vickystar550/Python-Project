from turtle import Turtle, Screen
import pandas

# create the screen object:
screen = Screen()
screen.setup(width=1000, height=600)
screen.title("U.S. States Game")
screen.bgcolor("black")
# screen.bgpic("blank_states_img.gif")
screen.addshape("blank_states_img.gif")

# create turtle object:
turtle = Turtle()
turtle.shape("blank_states_img.gif")

# read csv:
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

score = 0
counter = 50
while counter > 0:
    counter -= 1
    # get input:
    usr_input = screen.textinput(f"{score}/50 States Correct", prompt="What's another state name?").title()

    # check user input:
    if usr_input in states_list:
        score += 1
        state_data = data[data.state == usr_input]

        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(float(state_data.x), float(state_data.y))
        writer.write(f"{usr_input}", align="center", font=("Courier", 10, "bold"))

    # end game prematurely:
    if usr_input == "Stop":
        counter = 0

screen.mainloop()

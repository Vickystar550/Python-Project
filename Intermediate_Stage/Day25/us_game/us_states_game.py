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

correct_states = []
score = 0
counter = 50
while counter > 0:
    counter -= 1
    # get input:
    usr_input = screen.textinput(f"{score}/50 States Correct", prompt="What's another state name?").title()

    # check user input:
    if usr_input in states_list:
        correct_states.append(usr_input)
        score += 1
        state_data = data[data.state == usr_input]

        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(float(state_data.x), float(state_data.y))
        writer.write(f"{usr_input}", align="center", font=("Courier", 10, "bold"))

    # End game prematurely and get new states to learn. Educationally incentive:
    if usr_input == "Stop":
        missing_state = []
        for state in states_list:
            if state not in correct_states:
                missing_state.append(state)

        missing_state_df = pandas.DataFrame(missing_state)
        print(missing_state_df)
        missing_state_df.to_csv("state_to_learn.csv")
        break

screen.mainloop()

from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')  # the game background color is set to black
screen.setup(width=1250, height=400)  # setting my canvas screen to this arbitrary value

# Ask the player for a bet
bet = screen.textinput(title='Make your Bet', prompt="We've RED, GREEN, BLUE, VIOLET, YELLOW, and ORANGE as "
                                                     "contestants. Enter your prediction as a color")


def create_turtles_and_finish_line():
    """ create six turtles object align at the same location and return a list of them; create a finish line """
    # this section create the turtle
    vikky = []
    color_tuple = ('red', 'blue', 'green', 'yellow', 'orange', 'violet')
    position = [(-600, -150), (-600, -90), (-600, -30), (-600, 30), (-600, 90), (-600, 150)]
    for i in range(len(position)):
        vikky.append(Turtle())
        vikky[i].hideturtle()
        vikky[i].shape('turtle')
        vikky[i].color(color_tuple[i])
        vikky[i].penup()
        vikky[i].speed('fastest')
        vikky[i].goto(position[i])
        vikky[i].showturtle()

    # this section creates the finish line
    tim = Turtle()
    tim.color('white')  # the finish line is made white
    tim.hideturtle()
    tim.penup()
    tim.speed('fastest')
    tim.goto(598, -200)  # starting point for the finish line
    tim.pendown()
    tim.pensize(width=2)  # end point for the finish line
    tim.goto(598, 200)

    # return vikky, list of turtle objects
    return vikky


def random_move(t_list=None):
    if t_list is None:
        t_list = create_turtles_and_finish_line()
    import random
    game_on = True
    winner = None
    while game_on:
        t_list[0].fd(random.randint(1, 20))
        t_list[1].fd(random.randint(1, 20))
        t_list[2].fd(random.randint(1, 20))
        t_list[3].fd(random.randint(1, 20))
        t_list[4].fd(random.randint(1, 20))
        t_list[5].fd(random.randint(1, 20))

        for _ in range(6):
            if t_list[_].xcor() > 600:  # 600 is the benchmark to win
                # this conditional statement check if the X coordinate of each turtle is greater 600
                # We couldn't set it to exactly 600 (i.e ==599) because the position of each turtle keeps changing
                # based on the random.randint() function, thus is likely the X-cor != 600
                game_on = False
                winner = t_list[_]
    # return winner, the turtle object that whose X-cor is greater than the benchmark, 600
    return winner


def check_winner(race=None):
    """ this function checks the winner ---- compares the user's input with the actual winner """
    if race is None:
        race = random_move()

    wining_color = race.color()[0]
    t_write = Turtle()
    t_write.hideturtle()

    if wining_color == bet.lower():
        t_write.pencolor("green")  # the pencolor will change to green denoting winning
        t_write.write(arg='Congratulations, You won', align='center', font=('Times New Roman', 30, 'bold'))
    else:
        t_write.color('red')  # the pencolor will change to red denoting failed
        t_write.write(arg=f'Oops, You lose. '
                          f'The {wining_color} turtle WON', align='center', font=('Times New Roman', 30, 'bold'))

    screen.mainloop()


# THE GAME IS INITIALIZE
check_winner()

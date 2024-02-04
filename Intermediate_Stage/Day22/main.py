from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Create the screen object, define attributes and methods:
screen = Screen()
screen.setup(width=1500, height=700)
screen.bgcolor("white")
screen.title("Welcome to Pong Game")
screen.tracer(0)


# create a paddles, ball, and scoreboard objects:
l_paddle = Paddle((-700, 0))
r_paddle = Paddle((700, 0))
ball_object = Ball()
scoreboard_object = Scoreboard()


# Get the screen object to listen to keystrokes for the two paddles:
screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up, key="d")
screen.onkey(fun=l_paddle.go_down, key="c")

# Start the game:
game_on = True
while game_on:
    time.sleep(ball_object.move_speed)
    screen.update()
    ball_object.move()

    # detect collision with wall:
    if ball_object.ycor() >= 300 or ball_object.ycor() <= -300:
        ball_object.bounce_y()

    # detect collision with paddle
    if ball_object.distance(r_paddle) <= 50 or ball_object.distance(l_paddle) <= 50:
        ball_object.bounce_x()

    # detect when the right paddle miss the ball object:
    if ball_object.xcor() > 700:
        scoreboard_object.l_point()
        ball_object.reset_position()

    # detect when the left paddle miss the ball object:
    if ball_object.xcor() < -700:
        scoreboard_object.r_point()
        ball_object.reset_position()


screen.exitonclick()

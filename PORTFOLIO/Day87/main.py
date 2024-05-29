from elements import Element
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from turtle import Screen
import time

MOVE_Y = 370

screen = Screen()
screen.title('Breakout Game')
screen.setup(width=2000, height=1200)
screen.bgcolor('black')
screen.title('Welcome to Breakout Game')
screen.tracer(0)

element = Element()
scoreboard = Scoreboard()
ball = Ball()
paddle = Paddle()

# Get the screen object to listen to keystrokes for the paddle:
screen.listen()
screen.onkey(fun=paddle.go_right, key='Right')
screen.onkey(fun=paddle.go_left, key='Left')


def timer():
    """set timing mechanism"""
    global ball, element, paddle

    if scoreboard.reset_screen:
        element.reset_bricks()
        ball = ball.reset_ball()

        scoreboard.reset_screen = False
        scoreboard.toggle()
    else:
        scoreboard.countdown()

    screen.ontimer(timer, 1000)


timer()


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    # move ball
    ball.move()

    # detect ball collisions with vertical wall:
    if ball.xcor() >= 350 or ball.xcor() <= -350:
        ball.bounce_x()

    # detect when ball is beyond +ve y threshold (border)
    if ball.ycor() > MOVE_Y:
        ball.bounce_y()
    else:
        # detect collision with bricks:
        bricks = element.bricks

        for coordinate, brick in bricks.items():

            if ball.distance(brick) <= 20:
                brick.reset()
                # reward player
                scoreboard.update_score()
                ball.bounce_y()

    # detect when paddle misses the ball
    if ball.ycor() <= -380:
        ball.bounce_y()
        # penalize player
        # print('miss paddle')

    # detect collision with paddle:
    if ball.distance(paddle) <= 20:
        ball.bounce_y()


screen.mainloop()

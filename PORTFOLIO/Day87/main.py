from elements import Element
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from turtle import Screen
import time

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

move_y = 200


def damage():
    # detect collision with bricks:
    global move_y
    bricks = element.bricks
    for coordinate, brick in bricks.items():

        # line_row = coordinate[1]
        # if coordinate[1] == 200:
        #     move_y = 250

        if ball.distance(brick) <= 20:
            print('damage')
            brick.reset()
            ball.bounce_y()


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    # update screen
    screen.update()

    # move ball
    ball.move()

    # detect ball collisions with vertical wall:
    if ball.xcor() >= 350 or ball.xcor() <= -350:
        ball.bounce_x()

    # detect when ball is beyond +ve y threshold
    if ball.ycor() > move_y:
        ball.bounce_y()
    else:
        damage()

    # detect when paddle misses the ball
    if ball.ycor() <= -380:
        ball.bounce_y()
        print('miss paddle')

    # detect collision with paddle:
    if ball.distance(paddle) <= 20:
        ball.bounce_y()


screen.mainloop()


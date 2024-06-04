import tkinter
import turtle
from turtle import Screen
import time
import subprocess
import sys
import os
import json

from elements import Element
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

MOVE_Y = 320

screen = Screen()
screen.title('Breakout Game')
screen.setup(width=2000, height=1200)
screen.bgcolor('black')
screen.title('Welcome to Breakout Game')
screen.tracer(0)


def read():
    """reads from a json file"""
    try:
        with open('data.json', 'r') as file:
            content = json.load(fp=file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {'player one': [0], 'player two': [0]}
    else:
        return content


readings = read()

element = Element()
scoreboard = Scoreboard(scores_dict=readings)
ball = Ball()
paddle = Paddle()

# Get the screen object to listen to keystrokes for the paddle:
screen.listen()
screen.onkey(fun=paddle.go_right, key='Right')
screen.onkey(fun=paddle.go_left, key='Left')


def save():
    """saves to a json file"""
    with open('data.json', 'w') as file:
        json.dump(obj=scoreboard.get_scores(), fp=file, indent=4)


def timer():
    """set timing mechanism"""
    global ball, element, paddle

    if scoreboard.reset_screen:
        restart()
    else:
        scoreboard.countdown()
    screen.ontimer(timer, 1000)


timer()

bricks = element.bricks

game_on = True


def play_game():
    try:
        while game_on:
            time.sleep(0.001)
            screen.update()
            ball.move()

            # detect ball collisions with vertical wall:
            if ball.xcor() >= 350 or ball.xcor() <= -350:
                ball.bounce_x()

            # detect when ball is beyond +ve y threshold (border)
            if ball.ycor() > MOVE_Y:
                ball.bounce_y()
            else:
                # detect collision with bricks:
                for coordinate in list(bricks.keys()):
                    brick = bricks[coordinate]

                    if brick is None:
                        scoreboard.update_score(score=0)
                        continue
                    else:
                        if ball.distance(brick) <= 20:
                            if brick.color()[0] == 'red':
                                # shrink the paddle
                                paddle.shrink()

                            scoreboard.update_score(score=brick.damage_score)
                            brick.reset()
                            brick = None
                            del bricks[coordinate]
                            ball.bounce_y()

            # detect when paddle misses the ball
            if ball.ycor() <= -450:
                ball.bounce_y()
                # reduce the player chances:
                scoreboard.update_chance()
                if scoreboard.chances <= 0:
                    restart()

            # detect collision with paddle:
            if ball.distance(paddle) <= 40:
                ball.bounce_y()
    except (tkinter.TclError, turtle.Terminator):
        # erase the store file
        with open('data.json', 'w') as file:
            json.dump(obj={'player one': [0], 'player two': [0]}, fp=file, indent=4)


def restart():
    save()
    screen.bye()

    # determine the current python interpreter
    python = sys.executable

    # determine the path to the main script
    script_path = os.path.join(os.path.dirname(__file__), 'main.py')

    # use subprocess to restart the script
    subprocess.run([python, script_path])

    # optional: exiting the current script
    sys.exit()


if __name__ == '__main__':
    play_game()

screen.mainloop()

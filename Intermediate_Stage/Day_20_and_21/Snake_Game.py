from turtle import Screen
from snake import Snake, BorderLine
from food import Food
from scoreboard import ScoreBoard
import time


# CREATE AND SET CANVAS SCREEN PROPERTIES
screen = Screen()
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

# OBJECT CREATION
snake = Snake()
food = Food()
border = BorderLine()
scoreboard = ScoreBoard()

# KEYBOARD EVENT
screen.listen()
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.down, key='Down')

# START THE GAME
game_on = True
while game_on:
    screen.update()
    time.sleep(0.07)

    # move the snake after refreshing the screen
    snake.move()

    # detect collision with food
    if food.distance(snake.head) < 15:
        # refresh food position
        food.refresh()

        # add a body to the snake end
        snake.add_snake()

        # update scoreboard
        scoreboard.increase_score()

    # detect collision with tail or any body part. Here the snake is assumed to bite itself
    if snake.detect_collision():
        game_on = False
        scoreboard.game_over()
screen.exitonclick()

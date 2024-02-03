import time
from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard

# Create the screen object, assign attributes and methods
screen = Screen()
screen.title("Welcome to the Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

# Create other objects:
snake_object = Snake()
food_object = Food()
scoreboard_object = Scoreboard()  # create a scoreboard

# Get the screen to listen to key strokes:
screen.listen()
screen.onkey(fun=snake_object.left, key="Left")
screen.onkey(fun=snake_object.right, key="Right")
screen.onkey(fun=snake_object.up, key="Up")
screen.onkey(fun=snake_object.down, key="Down")

# START the game:
game_on = True
while game_on:
    screen.update()     # update the screen after each successful iteration
    time.sleep(0.1)     # sleep it for 0.1 sec
    snake_object.move()     # moves the snake object

    # detect collision with food
    if snake_object.head.distance(food_object) < 15:
        food_object.refresh()
        snake_object.extend()
        scoreboard_object.increase_score()

    # detect collision with wall
    if snake_object.head.xcor() > 280 or snake_object.head.xcor() < -280 or snake_object.head.ycor() > 280 or snake_object.head.ycor() < -280:
        game_on = False
        scoreboard_object.game_over()

    # detect collision with tail
    for seg in snake_object.segment_list[1:]:
        if snake_object.head.distance(seg) < 10:
            game_on = False
            scoreboard_object.game_over()


screen.exitonclick()

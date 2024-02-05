import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create the screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Other objects:
player_object = Player()
car_object = CarManager()
scoreboard = Scoreboard()


# listen to keystrokes:
screen.listen()
screen.onkey(fun=player_object.move, key="Up")

game_is_on = True
while game_is_on:
    # delay every update of the screen by 0.1 sec
    time.sleep(0.1)
    screen.update()

    # create and move the car object
    car_object.create_car()
    car_object.move_car()

    # detect when the player hit the car:
    for car in car_object.fleet:
        if player_object.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False

    # detect when player crosses the finish line:
    if player_object.is_at_finish_line():
        player_object.refresh()
        scoreboard.increase_level()
        car_object.increase_speed()


screen.exitonclick()

## Day 22

Today challenge was building a pong game

Inside this folder contains four python scripts:

- The main.py 
- The scoreboard.py
- The ball.py
- The paddle.py

Their short descriptions are given below:

##### paddle.py:
Contains the Paddle class which inherit from the Turtle class.
Responsible for creating the paddle objects to the screen. 
It contains method for controlling the paddle's up and down movements.

##### scoreboard.py:
Contains the Scoreboard class, a child class of Turtle.
Responsible for displays the current score on the screen.

##### ball.py:
Contains the Ball class, a child class of Turtle.
Responsible for creating the ball, checking its movement against the screen 
boundaries and trigger its bounce method if contact is made with the boundary or the paddle

#### main.py:
This is the main game script that call others scripts (scoreboard, ball and paddle).
It create the screen object from the turtle library, set it to listen to keystrokes
and manage other functionalities of the Pong Game.
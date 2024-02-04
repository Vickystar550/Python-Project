from turtle import Turtle

# useful constants
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


# create the snake class
class Snake:
    """ this is the snake class; create and instantiate snake object(s) """
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        self.last_snake_position = self.snakes[-1].pos()

    def create_snake(self):
        """ this method creates the first three snake component to the screen when the class is initialized """
        for _ in range(len(STARTING_POSITION)):
            new_snake = Turtle('square')
            new_snake.penup()
            new_snake.color('orange')
            new_snake.goto(STARTING_POSITION[_])
            self.snakes.append(new_snake)

    def add_snake(self):
        """ this method adds a body piece (i.e. makes it grow) to the snake when the food is eaten """
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.speed('fastest')
        new_segment.color('orange')
        new_segment.goto(self.last_snake_position)
        self.snakes.append(new_segment)

    def move(self):
        """ This method add continuity to the snake.
            It continues the snake movement in the opposite direction when the head crosses
            the borderlines"""
        if (self.head.heading() == 90) and (self.head.ycor() >= 300):
            self.head.goto(self.head.xcor(), -300)
        elif (self.head.heading() == 270) and (self.head.ycor() <= -300):
            self.head.goto(self.head.xcor(), 300)
        elif (self.head.heading() == 180) and (self.head.xcor() <= -600):
            self.head.goto(600, self.head.ycor())
        elif (self.head.heading() == 0) and (self.head.xcor() >= 600):
            self.head.goto(-600, self.head.ycor())

        for i in range(len(self.snakes) - 1, 0, -1):  # starting from the last turtle in snake
            self.snakes[i].goto(self.snakes[i - 1].pos())
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        """ set the snake's head heading up (i.e. 90 degrees measured anti-clockwise) if it's not going down"""
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        """ set the snake's head heading down (i.e. 270 degrees measured anti-clockwise) if it's not going up"""
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        """ set the snake's head heading left (i.e. 180 degrees measured anti-clockwise) if it's not going right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        """ set the snake's head heading right (i.e. 0 degrees measured anti-clockwise) if it's not going left"""
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def detect_collision(self):
        """ this method detects collision with the tail or other body part; returns a boolean"""
        for _ in self.snakes[1:]:
            if self.head.distance(_) < 10:
                return True

    def reset(self):
        """This method clears the screen and initialized the starting snake"""
        self.snakes.clear()
        self.create_snake()


class BorderLine(Turtle):
    """ this class create borderline on the canvas when called"""
    def __init__(self):
        super().__init__()
        self.color('red')
        self.hideturtle()
        self.penup()
        self.goto(600, -305)
        self.pendown()
        self.goto(600, 305)
        self.goto(-600, 305)
        self.goto(-600, -305)
        self.goto(600, -305)


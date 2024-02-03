from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        """This function create three snake objects when the Snake class is initialized"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """This function create and add a snake object at the specified position
            append the result to a list of snakes"""
        segment = Turtle(shape="square")
        segment.penup()
        segment.goto(position)
        self.segment_list.append(segment)

    def extend(self):
        """This function extend the snake body by add to its end"""
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        """This function moves the snakes forward"""
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            self.segment_list[seg_num].goto(self.segment_list[seg_num - 1].pos())

        self.segment_list[0].forward(MOVE_DISTANCE)

    def left(self):
        """This turns the snake head left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """This turns the snake head right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        """This turns the snake head up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """This turns the snake head down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


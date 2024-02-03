import turtle


def draw_panda(x, y, direction):
    # Set the direction of the bunny
    turtle.setheading(direction)

    # Draw first ear
    turtle.up()
    turtle.setpos(x - 24, y + 95)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(11)
    turtle.end_fill()

    # Draw second ear
    turtle.up()
    turtle.setpos(x + 24, y + 95)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(11)
    turtle.end_fill()

    # Draw head
    turtle.up()
    turtle.setpos(x, y + 35)
    turtle.down()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(35)
    turtle.end_fill()

    # Draw first eye
    turtle.up()
    turtle.setpos(x - 18, y + 75)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(8)
    turtle.end_fill()

    # Draw second eye
    turtle.up()
    turtle.setpos(x + 18, y + 75)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(8)
    turtle.end_fill()

    # Draw first colored eye
    turtle.up()
    turtle.setpos(x - 18, y + 77)
    turtle.down()
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(4)
    turtle.end_fill()

    # Draw second colored eye
    turtle.up()
    turtle.setpos(x + 18, y + 77)
    turtle.down()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(4)
    turtle.end_fill()

    # Draw nose
    turtle.up()
    turtle.setpos(x, y + 55)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    # Draw mouth
    turtle.up()
    turtle.setpos(x, y + 55)
    turtle.down()
    turtle.right(90)
    turtle.circle(5, 180)
    turtle.up()
    turtle.setpos(x, y + 55)
    turtle.down()
    turtle.left(360)
    turtle.circle(5, -180)


# Draw six bunnies facing different directions
turtle.speed('fastest')

draw_panda(0, 0, 0)
draw_panda(100, 0, 45)
draw_panda(200, 0, 90)
draw_panda(0, -100, 135)
draw_panda(100, -100, 180)
draw_panda(200, -100, 225)

turtle.done()


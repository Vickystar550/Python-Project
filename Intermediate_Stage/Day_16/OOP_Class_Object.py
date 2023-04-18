""" this file is a practice on OOP """

import turtle
from prettytable import PrettyTable

# create a turtle object from Turtle class
vikky = turtle.Turtle()
print(vikky)

# create a screen object from the Screen class
my_screen = turtle.Screen()
print(my_screen.canvheight)

# modify the turtle object default attributes
vikky.shape('turtle')
vikky.color("burlywood4")

# move the turtle
vikky.forward(200)

# this set the screen and exit it on click
my_screen.exitonclick()

# create a table from the prettyTable class
my_table = PrettyTable()

# add columns to it
my_table.add_column('Name', ['John', 'James', 'Peter', 'Paul'])
my_table.add_column('Age', [23, 56, 67, 78])
my_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Straw Berry"])
my_table.add_column("Type", ["Electric", "Water", "Fire", "Fruit"])

# print the table
print(my_table)

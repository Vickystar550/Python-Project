# This function calculates the number of cans of paint that will be sufficient to paint a wall
# Given that one paint-can carries 5 square meters

import math

test_h = float(input("Height of Wall:\n"))
test_w = float(input("Width of Wall:\n"))
coverage = 5


def paint_calc(height=test_h, width=test_w, cover=coverage):
    numbers_of_can = math.ceil((height * width) / cover)
    print(f"You will need {numbers_of_can} cans of paint")


paint_calc()

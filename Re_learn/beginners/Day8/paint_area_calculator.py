def paint_area_calculator():
    """This program calculate the numbers of paint can needed to paint a given area
    of a wall.
    Height and Width are assumed to be in  meters"""

    import math
    height = int(input("Enter the height in metres\n"))
    width = int(input("Enter the width in metres\n"))

    numbers_of_can = math.ceil((height * width) / 5)
    print(f"\nNumbers of cans needed is {numbers_of_can}")
    
paint_area_calculator()
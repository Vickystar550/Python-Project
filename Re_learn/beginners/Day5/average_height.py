"""This program calculates the average height given a set of heights"""

print("Welcome to your Average Height Calculator\n")

# Get the list of heights:
height_list = input("\nENTER DIIFERENT HEIGHTS SEPERATED BY A SPACE\n").split()

# Get the height sum using list comprehension:
height_sum = sum([float(j) for j in height_list])

# Print the average height:
print("The Average Height is: {:.2f}".format(height_sum / len(height_list)))

"""This program print the highest score from list of scores"""

print("Welcome to your Highest score Checker program")

# Get the different score:
score_list = input("Enter different score seperated by a space\n").split()

# Make a clean list of the scores as float data type:
score_cleaned = [float(x) for x in score_list]

# Initialize any element of score_cleaned to be the highest score:
highest = score_cleaned[-1]

# Write a loop to check against all elements in score_cleaned:
for i in score_cleaned:
    if i > highest:
        highest = i

# Print the highest score:
print(highest)
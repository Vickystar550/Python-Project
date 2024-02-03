"""This program checks if a given number is even or odd"""

# Print our customary welcome message:
print("Welcome to your amazing even and odd number checker\n")

# Prompt the user for number input:
number = int(input("Please enter any positive integer:\n"))

# Check the inputed number:
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

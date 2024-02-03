"""This program calculate and print the BMI of a given individual"""

# Print a welcome message:
print("Welcome to your amazing BMI calculator")

# Obtain the necessary variables:
height = float(input("Enter your height in Kilometer:\n"))
weight = float(input("Enter your weight in Kilogram:\n"))

# Calculate the BMI:
BMI = weight / (height ** 2)

# Prints the result:
print(f"Your BMI is {BMI: .2f}")
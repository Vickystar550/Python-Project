"""This program calculates the Body Mass Index given the weight and height

BMI is a measure of some people's weight taking into account their height.
It is expressed as the ratio of weight (in kg) to the square of height (in m)"""

print("This is a Body Mass Index Calculator")

weight = float(input("Enter your weight in kg:\n"))
height = float(input("Enter your height in meters:\n"))

bmi = weight / (height ** 2); print("Your BMI is: " + str(int(bmi)))
"""This is an advanced BMI calculator"""

print("Welcome to an improved version of BMI calcilator")

height = float(input("Enter your height in meters:\n"))
weight = float(input("Enter your weight in meters:\n"))

bmi = round((weight / (height ** 2)))


if bmi < 18.5:
    print(f"Your BMI is {bmi} and your are Underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi} and your are Normal Weight")
elif bmi < 30:
    print(f"Your BMI is {bmi} and your are Slightly Overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi} and your are Obese")
else:
    print(f"Your BMI is {bmi} and your are Clinically Obese")
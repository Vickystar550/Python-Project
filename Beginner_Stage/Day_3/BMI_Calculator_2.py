"""This program calculates the Body Mass Index BMI based on user's weight and height"""

# Ask for user's weight and height:
weight = float(input("Enter your weight in kg:\n"))
height = float(input("Enter your height in m:\n"))

# Calculate BMI:
bmi = round(weight / height ** 2)

# Check conditions for different bmi values:
if bmi < 18.50:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25.00:
    print(f"Your BMI is {bmi}, you have normal weight.")
elif bmi < 30.00:
    print(f"Your BMI is {bmi}, you are overweight.")
elif bmi < 35.00:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
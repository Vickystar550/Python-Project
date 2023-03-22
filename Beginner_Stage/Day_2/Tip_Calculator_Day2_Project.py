"""calculates percentage tip"""

print("Welcome to the tip calculator")

bill = float(input("What was the total bill:\n"))

tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))

people = int(input("How many people to split the bill?\n"))

p_tip = bill + ((tip / 100) * bill)

each_pay = round(p_tip / 7, 2)

print(f"Each person should pay: ${each_pay}")
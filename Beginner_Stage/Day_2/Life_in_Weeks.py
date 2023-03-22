"""
This program calculates how many days, weeks, and months you have left if you live still 90 years old

It will take your current age and output a message with our time left

Assumption: We do not consider leap years!!!
"""

age = int(input("Enter your current age:\n"))

#This calculates the detail for the remaining life:
remaining_age = 90 - age
months = 12 * remaining_age; weeks = 52 * remaining_age; days = 365 * remaining_age

print(f"You have {days} days, {weeks} weeks, and {months} months left")


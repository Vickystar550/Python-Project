"""This program is a tip calculator"""

# Print a welcome message:
print("Welcome to your tip calculator\n")

# Ask for the total bill:
bill = float(input("What is the total bill?\n"))

# Ask for the percentage tip:
tip = float(input("What percentage tip would you like to give?\n"))

# Ask for the number of people to share the bill
people = int(input("How many people would you like to split the bill into?\n"))

# Calculate the total bill and the amount to be paid by each person:
total_bill = bill * ((100 + tip) / 100)
bill_each = total_bill / people

# print the bill per person:
print("Then each person will pay ${:.2f}".format(bill_each))
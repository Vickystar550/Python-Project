"""This program checks whether a given year is a leap year"""

# Ask for input:
year = int(input("Enter any year:\n"))

# Check for leap year:

# if year is evenly divisible by 4, --leap year except
if year % 4 == 0:
    # if evenly divisible by 100 -- not leap year unless
    if year % 100 == 0:
        # if evenly divisible by 400 -- leap year.
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
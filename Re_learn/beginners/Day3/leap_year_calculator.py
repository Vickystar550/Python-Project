"""This program checks if a given year is a leap year"""

print("This program checks if a given year is a leap year")

year = int(input("Enter any year\n"))

# RULES:
#1 year is leap year if it's evenly divisible by 4,
#2 except it is evenly divisible by 100,
#3 unless it is evenly divisible by 400

if year % 4 == 0:  
    if year % 100 == 0:  
        if year % 400 == 0: 
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")
"""This program calculate the statistics of life left to live"""

print("Our program is optimistic and it presumes that we all will live upto 90 years.")

# Add for the person's age:
year_live = int(input("Please input your age:\n"))

# calculate the basic life statistics:
weeks_left = 52 * (90 - year_live)
month_left = 12 * (90 - year_live)
days_left = 365 * (90 - year_live)

# print the result:
print(f"\nCongratulations you have {days_left} days, {month_left} months and {weeks_left} weeks left to live upto 90 years.\n")

def leap_year_checker(year=int(input("Enter a year\n"))):
    """ This function checks for a leap year """
    if year % 4 == 0:
        # if evenly divisible by 100 -- not leap year unless
        if year % 100 == 0:
            # if evenly divisible by 400 -- leap year.
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(x=leap_year_checker(), month=int(input("Enter the month\n"))):
    """ This function calculate the days in a month; calls the leap year function """
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if x:
        days[1] = 29
    return days[month - 1]


a = days_in_month()
print(a)

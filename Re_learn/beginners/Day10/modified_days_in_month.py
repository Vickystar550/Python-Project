def days_in_month(year=int(input("Enter the year\n")), month=int(input("Enter the month\n"))):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def leap_year(x):
        """This program checks if a given year is a leap year"""
        if x % 4 == 0:
            if x % 100 == 0:
                if x % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    if leap_year(year):
        month_list[1] = 29
        return month_list[month - 1]
    else:
        return month_list[month - 1]


print(days_in_month())

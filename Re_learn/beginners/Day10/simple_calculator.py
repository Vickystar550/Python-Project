""" This program is a simple arithmetic calculator"""

logo1 = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |   
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""

logo2 = ("\n"
         "   _____      _            _       _             \n"
         "  / ____|    | |          | |     | |            \n"
         " | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ \n"
         " | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|\n"
         " | |___| (_| | | (__| |_| | | (_| | || (_) | |   \n"
         "  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|")


# Create arithmetic functions:
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def multiply(x, y):
    return x*y


# print the logos,
print(logo1, "\t", logo2)
# Getting the first number
first_number = float(input("\nWhat is your first number?  "))

# Initialize the result variable to zero:
result = 0

# Start the game, initializing the boolean game_on to True:
game_on = True
while game_on:
    # print the allowable operators
    print("\n+\n-\n*\n/\n")
    operation = input("Pick an Operation:   ")
    next_number = float(input("What is your next number?    "))

    # Check given operator input and perform the required arithmetic function:
    if operation == "+":
        result += add(first_number, next_number)
        print(f"\n{first_number:.2f} {operation} {next_number} = {result:.2f}")
    elif operation == "-":
        result += subtract(first_number, next_number)
        print(f"\n{first_number:.2f} {operation} {next_number} = {result:.2f}")
    elif operation == "*":
        result += multiply(first_number, next_number)
        print(f"\n{first_number:.2f} {operation} {next_number} = {result:.2f}")
    elif operation == "/":
        result += divide(first_number, next_number)
        print(f"\n{first_number:.2f} {operation} {next_number} = {result:.2f}")
    else:
        print("Invalid Operator")

    contd_calculating = input(
        f"\nType 'y' to continue calculating with {result:.2f}, or type 'n' to start a new calculation  ")
    if contd_calculating == "y" or contd_calculating == "n":
        game_on = True
    else:
        print("\ninvalid Choice! Thanks for using the Calculator")
        break

    if contd_calculating == 'n':
        result = 0
        first_number = float(input("\nWhat is your first number?  "))
    else:
        first_number = result
        result = 0

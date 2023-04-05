def calculator():
    """ This functions is a calculator.
    It contains other sub-functions.
    And repeat the calculation is desired. """

    logo = """
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
    |_____________________|
    
               _            _       _             
              | |          | |     | |            
      ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
     / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | (_| (_| | | (__| |_| | | (_| | || (_) | |   
     \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
     """

    # Operator Functions
    def add(n1, n2):
        """ Adds two numbers"""
        return n1 + n2

    def multiply(n1, n2):
        """ Multiply two numbers """
        return n1 * n2

    def subtract(n1, n2):
        """ Subtract two numbers """
        return n1 - n2

    def divide(n1, n2):
        """ Divides the first number by the second"""
        return n1 / n2

    # Create a dict where key is the operation symbols and the value, the operation
    operation = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    print("Welcome to the best calculator in the world")
    print(logo)

    # Ask for the first number:
    first_numb = float(input("What is the first number?\n"))
    # Get the user desired operation:
    for symbols in operation:
        print(symbols)
    operation_symbol = input("Pick an operation from the line above\n")
    # Ask for the second number:
    last_numb = float(input("What is the second number?\n"))

    print(f"{first_numb} {operation_symbol} {last_numb} equals  {operation[operation_symbol](first_numb, last_numb)}")
    # Capture the last result:
    last_result = operation[operation_symbol](first_numb, last_numb)

    # CREATE A REPETITION:
    should_continue = True
    while should_continue:
        next_operation = input(
            f"Type 'y' to continue calculating with {last_result},"
            f" or type 'n' to exit.:\n").lower()

        if next_operation == 'y':
            next_operation_symbol = input("Pick an operation\n")
            next_numb = float(input("What is the next number?\n"))
            # Print the result:
            print(f"{last_result} {next_operation_symbol} {next_numb} equals "
                  f" {operation[next_operation_symbol](last_result, next_numb)}")
            # Update last result
            last_result = operation[next_operation_symbol](last_result, next_numb)
        else:
            should_continue = False
            restart = input("Do you want to restart all over again?"
                            " type 'y' to restart, 'n' to exit\n").lower()
            if restart == 'y':
                calculator()
            else:
                print("Thank you for using")


calculator()

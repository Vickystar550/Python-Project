""" This is your digital coffee machine """
from data import *
from art import *

print(logo)
print("Welcome to your Fantastic Coffee Machine")


# FUNCTIONS DEFINITION
def process_transaction():
    """ This function sum the inputted coins and check if the transaction matches each flavour price"""
    print("\nPlease insert coins.")
    q = int(input("How many quarters?  "))
    d = int(input("How many dimes?  "))
    n = int(input("How many nickels?  "))
    p = int(input("How many pennies?  "))

    # Add the coins
    user_money = QUARTER * q + DIME * d + NICKEL * n + PENNY * p

    global user_choice
    if user_choice == 'latte':
        # Checks if the user's money is enough to purchase latte and make purchase
        if user_money > latte['cost']:
            report['money'] += latte['cost']
            report['balance'] = user_money - latte['cost']

            print(f"\nHere is ${round(report['balance'], 2)} in change")
            print("Here is your Latte. Enjoy!")
        else:
            print(f"\nOops your money isn't enough. Here is your money: ${round(user_money, 2)}")

            # Returns the ingredients
            report['water'] += latte['water']
            report['milk'] += latte['milk']
            report['coffee'] += latte['coffee']

    elif user_choice == 'espresso':
        # Checks if the user's money is enough to purchase espresso and make purchase
        if user_money > espresso['cost']:
            report['money'] += espresso['cost']
            report['balance'] = user_money - espresso['cost']

            print(f"\nHere is ${round(report['balance'], 2)} in change")
            print("Here is your Espresso. Enjoy!")
        else:
            print(f"\nOops your money isn't enough. Here is your money: ${round(user_money, 2)}")

            # Returns the ingredients
            report['water'] += espresso['water']
            report['coffee'] += espresso['coffee']

    else:
        # Checks if the user's money is enough to purchase cappuccino and make purchase
        if user_money > cappuccino['cost']:
            report['money'] += cappuccino['cost']
            report['balance'] = user_money - cappuccino['cost']

            print(f"\nHere is ${round(report['balance'], 2)} in change")
            print("Here is your Cappuccino. Enjoy!")
        else:
            print(f"\nOops your money isn't enough. Here is your money: ${round(user_money, 2)}")

            # Returns the ingredients
            report['water'] += cappuccino['water']
            report['milk'] += cappuccino['milk']
            report['coffee'] += cappuccino['coffee']


def show_report():
    """ this function prints the summary report for the coffee """
    print(f"Water: {report['water']}\nMilk: {report['milk']}\nCoffee: {report['coffee']}\nMoney: ${report['money']}")


def check_latte():
    """ Check resources sufficient to make Latte """
    if report['water'] >= latte['water']:  # checks for water
        if report['milk'] >= latte['milk']:  # checks for milk
            if report['coffee'] >= latte['coffee']:  # checks for coffee
                # Make necessary deductions:
                report['water'] -= latte['water']
                report['milk'] -= latte['milk']
                report['coffee'] -= latte['coffee']
                # return a value
                return "good"
            else:
                print("\nInsufficient Coffee. No Latte!")
                return "bad"
        else:
            print("\nInsufficient Milk. No Latte!")
            return "bad"
    else:
        print("\nInsufficient Water. No Latte!")
        return "bad"


def check_espresso():
    """ Check resources sufficient to make Espresso """
    if report['water'] >= espresso['water']:  # checks for water
        if report['coffee'] >= espresso['coffee']:  # checks for coffee
            # Make necessary deductions in ingredients:
            report['water'] -= espresso['water']
            report['coffee'] -= espresso['coffee']
            # return a value
            return "good"
        else:
            print("\nInsufficient Coffee. No Espresso!")
            return "bad"
    else:
        print("\nInsufficient Water. No Espresso!")
        return "bad"


def check_cappuccino():
    """ Check resources sufficient to make Latte """
    if report['water'] >= cappuccino['water']:  # checks for water
        if report['milk'] >= cappuccino['milk']:  # checks for milk
            if report['coffee'] >= cappuccino['coffee']:  # checks for coffee
                # Make necessary deductions in ingredients:
                report['water'] -= cappuccino['water']
                report['milk'] -= cappuccino['milk']
                report['coffee'] -= cappuccino['coffee']
                # return a value
                return "good"
            else:
                print("\nInsufficient Coffee. No Cappuccino!")
                return "bad"
        else:
            print("\nInsufficient Milk. No Cappuccino!")
            return "bad"
    else:
        print("\nInsufficient Water. No Cappuccino!")
        return "bad"


# START THE GAME
game_on = True
while game_on:
    user_choice = input("\nWhat would you like (espresso/latte/cappuccino)?"
                        "___Enter 'report' to see the summary, or 'exit' to end the game\n").lower()

    if user_choice == 'exit':
        game_on = False
    elif user_choice == 'report':
        show_report()
    elif user_choice == 'latte':
        if check_latte() == 'good':
            process_transaction()
        else:
            game_on = False
    elif user_choice == 'espresso':
        if check_espresso() == 'good':
            process_transaction()
        else:
            game_on = False
    elif user_choice == 'cappuccino':
        if check_cappuccino() == 'good':
            process_transaction()
        else:
            game_on = False
    else:
        print("\nInvalid Coffee Flavour")

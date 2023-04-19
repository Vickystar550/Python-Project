from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating Objects from Classes
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

# get items
items = my_menu.get_items()

game_on = True
while game_on:
    print(f"\nThe available coffee flavors are:    {items}")
    # ask for user choice of drink
    choice = input(f"What do you want to drink? Enter 'report' to get the summary, 'exit' to end the game\n")

    if choice == 'exit':
        game_on = False
    elif choice == 'report':
        # print report:
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        # find drink object
        drink = my_menu.find_drink(choice)
        # Check if the required coffee flavor is available and has sufficient resources. Then make payment
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            # when payment is successful, make the coffee
            my_coffee_maker.make_coffee(drink)

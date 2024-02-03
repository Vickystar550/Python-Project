from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_object = Menu()
coffee_maker_object = CoffeeMaker()
money_machine_object = MoneyMachine()


game_on = True
while game_on:
    drink = input(f"\nWhat would you like? ({menu_object.get_items()}):\t").lower()

    if drink in ['exit', 'off', 'shutdown']:
        break
    elif drink == 'report':
        coffee_maker_object.report()
        money_machine_object.report()
    else:
        drink_item = menu_object.find_drink(drink)

        if (coffee_maker_object.is_resource_sufficient(drink_item) and
                money_machine_object.make_payment(cost=drink_item.cost)):
            coffee_maker_object.make_coffee(order=drink_item)

    play_again = input("Will you play again? Type 'yes' or 'no'\t").lower()
    if play_again not in ['yes', 'y']:
        game_on = False

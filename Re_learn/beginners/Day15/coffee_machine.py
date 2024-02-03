import data
import art

resource_bank = data.report


def report():
    """This function print the report on available resources"""
    print(f"Water: {resource_bank['water']}ml\nMilk: {resource_bank['milk']}ml")
    print(f"Coffee: {resource_bank['coffee']}g\nMoney: ${resource_bank['money']: .2f}")


def check_resource_sufficiency(resource) -> bool:
    """This function check if there are available resources for any drink choice"""
    if resource == 'espresso':
        return resource_bank['water'] >= 50 and resource_bank['milk'] >= 0 and resource_bank['coffee'] >= 18
    elif resource == 'latte':
        return resource_bank['water'] >= 200 and resource_bank['milk'] >= 150 and resource_bank['coffee'] >= 24
    elif resource == 'cappuccino':
        return resource_bank['water'] >= 250 and resource_bank['milk'] >= 100 and resource_bank['coffee'] >= 24


def process_coin() -> float:
    """This function ask for different coins and return the total sum"""
    quarter = int(input("How many quarters?:\t"))
    dime = int(input("How many dimes?:\t"))
    nickel = int(input("How many nickels?:\t"))
    penny = int(input("How many pennies?:\t"))
    return (quarter * data.QUARTER) + (dime * data.DIME) + (nickel * data.DIME) + (penny * data.PENNY)


def check_transaction_and_manage_resources(dk, amount) -> bool:
    """For any drink choice, checks if the amount paid is sufficient to purchase it.
    Also, make the necessary reductions and addition to the resource_bank
    returns True if successful"""
    if dk == 'espresso':
        if amount > data.espresso['cost']:
            resource_bank['water'] -= 50
            resource_bank['coffee'] -= 18
            resource_bank['money'] += amount
            resource_bank['balance'] = amount - data.espresso['cost']
            return True
        else:
            return False
    elif dk == 'latte':
        if amount > data.latte['cost']:
            resource_bank['water'] -= 200
            resource_bank['milk'] -= 150
            resource_bank['coffee'] -= 24
            resource_bank['money'] += amount
            resource_bank['balance'] = amount - data.latte['cost']
            return True
        else:
            return False
    elif dk == 'cappuccino':
        if amount > data.cappuccino['cost']:
            resource_bank['water'] -= 250
            resource_bank['milk'] -= 100
            resource_bank['coffee'] -= 24
            resource_bank['money'] += amount
            resource_bank['balance'] = amount - data.cappuccino['cost']
            return True
        else:
            return False


def print_resource_deficiency(dk):
    """For any drink choice, print out the insufficient item required to make it."""
    if dk == 'espresso':  # for espresso
        if resource_bank['water'] < data.espresso['water']:
            print("Insufficient Water")
        elif resource_bank['coffee'] < data.espresso['coffee']:
            print("Insufficient Coffee")
    elif dk == 'latte':  # for latte
        if resource_bank['water'] < data.latte['water']:
            print("Insufficient Water")
        elif resource_bank['milk'] < data.latte['milk']:
            print("Insufficient Milk")
        elif resource_bank['coffee'] < data.latte['coffee']:
            print("Insufficient Coffee")
    elif dk == 'cappuccino':  # for cappuccino
        if resource_bank['water'] < data.cappuccino['water']:
            print("Insufficient Water")
        elif resource_bank['milk'] < data.cappuccino['milk']:
            print("Insufficient Milk")
        elif resource_bank['coffee'] < data.cappuccino['coffee']:
            print("Insufficient Coffee")


# Start game
game_on = True
print(art.logo)
while game_on:
    drink = input("\nWhat would you like? (espresso/latte/cappuccino/report):\t").lower()

    if drink == 'report':
        report()
    elif drink == 'off':
        break
    else:
        if check_resource_sufficiency(drink):
            coin = process_coin()

            if check_transaction_and_manage_resources(dk=drink, amount=coin):
                print(f"Here is your ${resource_bank['balance']: .2f} in change")
                print(f"Here is your {drink}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money Refunded!")
        else:
            print_resource_deficiency(drink)

    play_again = input("Will you play again? Type 'yes' or 'no'\t").lower()
    if play_again not in ['yes', 'y']:
        game_on = False


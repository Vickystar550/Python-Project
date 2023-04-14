"""" This is the Blackjack game, also known as 21 """
import random

# SALUTATION
print("\nWelcome to the BLACKJACK GAME, also called 21")

# MODULE ONE:
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'Q', 'K', 'J']

dealer_cards = []
player_cards = []

# Filling the dealer's and players card list with cards
for i in range(2):
    dealer_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))

# Print the player's card collection:
print(f"\nYou\'ve {player_cards[0]} and {player_cards[1]} in your card collection\n")

# Print the dealer's first card but hide the other:
print(f"The dealer's first dealt card is {dealer_cards[0]} while the other is hidden!!!")


# MODULE TWO:
# FUNCTION LIBRARY
def card_calculator(collection):
    """ This function sum the value of the Number Cards, the face card (King, Queen, Jack),
    and also decide the value for Ace depending on the player's choice"""

    # checking for blackjack:
    if 'A' in collection and ('J' in collection or 'K' in collection or 'Q' in collection) and len(collection) == 2:
        return 0
    else:
        card_sum = 0
        for card in collection:
            if (card == 'J') or (card == 'K') or (card == 'Q'):
                card_sum += 10
            elif card == 'A':
                # Prompt the player to decide the count of his Ace card
                card_sum += int(
                    input(f"\nYour current hand value is {card_sum}, and you have an Ace in your Collection. "
                          f"How should it be counted?___Hint: Ace is count as 1 or 11\n"))
            else:
                card_sum += card
        return card_sum


def check_final_score():
    """ This function check both the dealer's and player's hand value """
    dealer_total = card_calculator(dealer_cards)
    player_total = card_calculator(player_cards)

    if (dealer_total > 21) and (player_total > 21):
        print(f"You both bust!! player\'s scored {player_total}; dealer\'s scored {dealer_total}")
    elif dealer_total == 0:
        print("The dealer has a blackjack")
    elif player_total == 0:
        print("The player has a blackjack")
    elif dealer_total > 21:
        print(f"The dealer\'s hand value is {dealer_total}. It is a bust. Hence, you win")
    elif player_total > 21:
        print(f"Your total hand value is {player_total}. Lol you bust")
    elif player_total == dealer_total:
        print("Your hand value and that of the dealer is the same. Hence is a push, your bet is returned")
    elif dealer_total > player_total:
        print(f"The dealer's total hand value is {dealer_total} and your is "
              f"{player_total}. You bust! Hence, the dealer wins")
    else:  # Then player's total is greater than dealer's own
        print(f"The dealer\'s hand value is {dealer_total}, and yours is {player_total}. Hence you win")


# MODULE THREE:
# Ask the player's for another dealing, and iterate through it based on their option.
next_deal = input("\nYou ought to request another deal. "
                  "Enter \'hit\' to get another card otherwise, you \'stand\' \n").lower()

if next_deal == 'hit':
    # Deal out another card for the player
    player_cards.append(random.choice(cards))
    print(f"\nYou now have {player_cards[2]} added to you collection")

# Reveal the dealer's face down card
print(f"\nThe hidden dealer's card is {dealer_cards[1]}, "
      f"Therefore, his first and second dealt cards are {dealer_cards[0]} and {dealer_cards[1]}\n")

# Checks dealer's card, make it more than 16 if the total hand value is less:
while card_calculator(dealer_cards) <= 16:
    dealer_cards.append(random.choice(cards))
    print(f"dealer\'s card total isn\'t above 16, so {dealer_cards[-1]} has been added to dealer\'s collection\n")

# MODULE FOUR:
check_final_score()

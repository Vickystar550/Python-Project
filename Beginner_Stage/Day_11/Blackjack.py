"""" This is the Blackjack game, also known as 21 """
import random


# MODULE ONE:
logo = """  _____   _              ___   _               _       _               _        ___                      
 |_   _| | |_    ___    | _ ) | |  __ _   __  | |__   (_)  __ _   __  | |__    / __|  __ _   _ __    ___ 
   | |   | ' \  / -_)   | _ \ | | / _` | / _| | / /   | | / _` | / _| | / /   | (_ | / _` | | '  \  / -_)
   |_|   |_||_| \___|   |___/ |_| \__,_| \__| |_\_\  _/ | \__,_| \__| |_\_\    \___| \__,_| |_|_|_| \___|
                                                    |__/                                                 """

underscore = """_____________________________________________________________________________________________________"""
CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'Q', 'K', 'J']


# MODULE TWO:
# FUNCTION LIBRARY
def card_calculator(cards):
    """ This function sum the value of the Number Cards, the face card (King, Queen, Jack),
    and also decide the value for Ace depending on the player's choice"""

    # checking for blackjack:
    if 'A' in cards and ('J' in cards or 'K' in cards or 'Q' in cards) and len(cards) == 2:
        return 0
    else:
        card_sum = 0
        for card in cards:
            if (card == 'J') or (card == 'K') or (card == 'Q'):
                card_sum += 10
            elif card == 'A':
                if cards == player_cards:
                    # this is possible when the cards parameter is the same as player_cards
                    # Prompt the player to decide the count of his Ace card
                    card_sum += int(
                        input(f"\nThe player's current score is {card_sum}. You've an Ace, "
                              f"How should it be counted?  HINT: Ace is count as 1 or 11\n"))
                elif cards == dealer_cards:
                    # when cards is equivalent to dealer_cards. Here, the function argument is dealer's cards
                    # Prompt the dealer to decide the count of his Ace card
                    card_sum += int(
                        input(f"\nThe dealer's current score is {card_sum}. You've an Ace, "
                              f"How should it be counted?  HINT: Ace is count as 1 or 11\n"))
                else:
                    # a universal list or when cards is any given list
                    card_sum += int(
                        input(f"\nYour current score is {card_sum}. You've an Ace, "
                              f"How should it be counted?  HINT: Ace is count as 1 or 11\n"))
            else:
                card_sum += card
        return card_sum


def check_final_score():
    """ This function check both the dealer's and player's scores """
    dealer_card_total = card_calculator(dealer_cards)
    player_card_total = card_calculator(player_cards)

    if (dealer_card_total > 21) and (player_card_total > 21):
        print(f"\nYou both bust! Player\'s scored {player_card_total}, dealer\'s scored {dealer_card_total}")
    elif dealer_card_total == 0:
        print("\nThe dealer has a blackjack")
    elif player_card_total == 0:
        print("\nThe player has a blackjack")
    elif dealer_card_total > 21:
        print(f"\nThe dealer\'s score is {dealer_card_total}. Yours is {player_card_total}. Dealer bust. You win")
    elif player_card_total > 21:
        print(f"\nYour score is {player_card_total}, greater than 21. Lol you bust")
    elif player_card_total == dealer_card_total:
        print("\nYour score and that of the dealer is the same. It's a push, your bet is returned")
    elif dealer_card_total > player_card_total:
        print(f"\nThe dealer's total score is {dealer_card_total}. Your is "
              f"{player_card_total}. The dealer win")
    else:  # Then player's total is greater than dealer's own
        print(f"\nThe dealer\'s score is {dealer_card_total}. Yours is {player_card_total}. You win")


def dealer_card_less_than_16(cards):
    """ this function checks if dealer cards is less than or equal to 16. Design only for that purpose """
    card_sum = 0
    for _ in cards:
        if _ == 'A':
            # take the maximum possible value of Ace: 11
            card_sum += 11
        elif (_ == 'J') or (_ == 'K') or (_ == 'Q'):
            card_sum += 10
        else:
            card_sum += _
    return card_sum


# MODULE THREE:
game_on = True
while game_on:
    # WELCOME MESSAGE
    print(logo)
    print("\n                             Welcome to the BLACKJACK GAME, also called 21")
    print(underscore)

    # just for fun. shuffle the CARDS element again.
    random.shuffle(CARDS)
    # create an empty list to hold dealer's and player's cards. It's created inside this while loop, so that it get
    # during each iteration of the while loop
    dealer_cards = []
    player_cards = []

    # filling the dealer's and players hand with cards
    for i in range(2):
        dealer_cards.append(random.choice(CARDS))
        player_cards.append(random.choice(CARDS))

    # Print the player's cards:
    print(f"\n\nYou\'ve {player_cards[0]} and {player_cards[1]} in your card collection")

    # Print the dealer's first card but hide the other:
    print(f"\nThe dealer's first card is {dealer_cards[0]}, while the other is hidden!\n")

    # Ask the player's for another dealing, and iterate through it based on their option.
    next_deal = input("Enter \'hit\' to get another card otherwise, you \'stand\' \n").lower()

    if next_deal == 'hit':
        # Deal out another card for the player
        player_cards.append(random.choice(CARDS))
        print(f"\nYou now have {player_cards[2]} added to you cards")

    # Reveal the dealer's face down card
    print(f"\nThe dealer's hidden card is {dealer_cards[1]}, "
          f"His first and second cards are {dealer_cards[0]} and {dealer_cards[1]}\n")

    # Checks dealer's card, make it more than 16 if the total hand value is less:
    while dealer_card_less_than_16(dealer_cards) <= 16:
        dealer_cards.append(random.choice(CARDS))
        print(f"The dealer\'s card total isn\'t above 16, so {dealer_cards[-1]} has been added to dealer\'s cards\n")

    # check final score:
    check_final_score()

    play_again = input("\nDo you want to play the Blackjack Game again? Enter 'y' or 'n'\n").lower()
    if play_again == 'y':
        game_on = True
    else:
        print("\nThank you for Playing.")
        game_on = False

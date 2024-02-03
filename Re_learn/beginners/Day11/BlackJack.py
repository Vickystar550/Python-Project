"""The First Capstone Project in 100 Days of Coding"""
import random
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
random.shuffle(cards)
user_list = []
dealer_list = []


def sum_cards(card_list):
    """This function sums the face value of a card deck. The Queen, King and Jack is sum as 10
        while Ace is counted as 1 or 11 depending on the cummulative sum before Ace and the player's choice."""  
    card_total = 0
    for g in card_list:
        if g == "J" or g == "K" or g == "Q":
            card_total += 10
        elif g == "A":
            if card_total < 21:
                print(f"Your total score is {card_total} and your have an 'A' in your card deck")
                
                ace = int(input("Your 'A' value can either be 1 or 11. What is your choice?     "))
                card_total += ace
        else:
            card_total += g
    return card_total


def deal():
    """This function deals out cards to both the player and the dealer at start."""
    for _ in range(2):
        user_list.append(random.choice(cards))
        dealer_list.append(random.choice(cards))


# def hit():
#     """This is activated when the player request for a hit.
#         In this case a card is randomly added to the player's deck"""
#     user_list.append(random.choice(cards))
#     dealer_list.append(random.choice(cards))
#     print("Your new extended card deck is: ", user_list, "summing up to", sum_cards(user_list))


# def repeating_hit():
#     """This function is a repeated action of the hit() function as long as the player demands a hit."""
#     while input("Hit 'h' or Stand 's':   ").lower() != "s":
#         hit()
#         if sum_cards(user_list) > 21:
#             # terminate the loop if the player's card deck exceed 21 in total.
#             break


def printing_result():
    if sum_cards(user_list) == 21:
        print("JACKPOT")
    elif sum_cards(user_list) > 21:
        print("You're busted")
    else:
        if sum_cards(user_list) == sum_cards(dealer_list):
            print(f"The dealer's deck is {dealer_list} summing to {sum_cards(dealer_list)}")
            print(f"Your total score is {sum_cards(user_list)}, You DRAW with the dealer.")
        elif sum_cards(user_list) > sum_cards(dealer_list):
            print(f"The dealer's deck is {dealer_list} summing to {sum_cards(dealer_list)}")
            print(f"Your total score is {sum_cards(user_list)}, You Lose!")
        else:
            print(f"The dealer's deck is {dealer_list} summing to {sum_cards(dealer_list)}")
            print(f"Your total score is {sum_cards(user_list)}, You Win!")


def game():
    deal()
    print("Your card deck is: ", user_list, "summing to", sum_cards(user_list))
    print(f"The dealer's revealed card is: {dealer_list[0]}")

    user_sum = sum_cards(user_list)
    while user_sum < 21:
        print("Your total sum is less than 21, would you like to 'hit' or 'stand' ? ")
        choice = input("\tEnter 'h' to hit or 's' to stand:\t").lower()
        if choice == "h":
            user_list.append(random.choice(cards))
        else:
            break
    
    print(f"Your new extended deck now is: {user_list}")
        
    # repeating_hit()
    printing_result()


game()


while input("\nDo you want to play again?     ").lower() == "y":
    game()
print("Thanks for Playing")
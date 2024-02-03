import random
CARDS = ["A", 2, 3, 4, 5, 6, 7, 8, 9 ,10, "J", "Q", "K"]
random.shuffle(CARDS)

dealer = []
players_collection = {}

# Geting the players information:
number_of_players = int(input("How many players do we have?     "))
for p in range(number_of_players):
    print(f"\n\t PLAYER {p+1}:  Enter your Blackjack details")
    name = input("What is your name?    ")
    bet = float(input("How much are betting?    "))
    cards = []
    players_collection[p] = {"name": name, "bet": bet, "cards": cards}
    
# Dealing cards:
def deal_cards():
    dealer.append(random.choice(CARDS))
    for j in range(number_of_players):
        players_collection[j]['cards'].append(random.choice(CARDS))

deal_cards()
deal_cards()

# Revealing Cards:
print(f"\n\tThe dealer's collection: [ *** , {dealer[-1]} ]\n")
for k in range(number_of_players):
    each_player = players_collection[k]
    print(f"\t{each_player['name'].title()} card collection: {each_player['cards']}\n")


# Counting Cards:
def card_calculator(cards, player_name) -> int:
    # checking for a blackjack
    if 'A' in cards and ('J' in cards or 'K' in cards or 'Q' in cards) and len(cards) ==2:
        return 21
    else:
        total = 0
        for h in cards:
            if h in ["J", "Q", "K"]:
                total += 10
            elif h == "A":
                if cards == dealer:
                    # when cards is equivalent to dealer_cards. Here, the function argument is dealer's cards
                    # Prompt the dealer to decide the count of his Ace card
                    x = int(
                        input(f"\nThe dealer's current score is {total}. You've an Ace, "
                              f"How should it be counted?  HINT: Ace is count as 1 or 11\t"))
                    total += x
                else: 
                    if cards.index(h) <= 2:
                        print(f"\nMr. {player_name}, your current sum is {total}. You have an Ace at index {cards.index(h) + 1}")
                        total += int(input("How should we count your Ace. Hint: it can either be 1 or 11      "))
                    else:
                        print(f"\nMr. {player_name}, Ace has been added again to your collection.")
                        total += int(input("What is your choice again?      "))
            else:
                total += h
        return total
                        
## ------ counting user cards (first count):
print("-----------------first count")
for d in range(number_of_players):
    each_owner_card = players_collection[d]['cards']
    player_name = players_collection[d]['name']
    players_collection[d]['sum_of_cards'] = card_calculator(each_owner_card, player_name)



# asking user for a hit or to stay:
def hit_func():
    for _ in range(number_of_players):
        player_name = players_collection[_]['name'].title()
        if players_collection[_]['sum_of_cards'] < 21:
            print(f"\n\n{player_name}, your score is less than 21")
            hit = input("\tDo you want to hit or stay. Enter 'h' or 's' respectively:  ").lower()
            if hit == "h":
                players_collection[_]['cards'].append(random.choice(CARDS))
                
hit_func()


## ----------counting again (second count):
print("\n----------------second count")
for d in range(number_of_players):
    each_owner_card = players_collection[d]['cards'][2:]
    player_name = players_collection[d]['name']
    players_collection[d]['sum_of_cards'] += card_calculator(each_owner_card, player_name)
    
    
# check if the dealers card is less than 16:
dealer_total = card_calculator(dealer, "dealer")
if dealer_total < 16:
    dealer.append(random.choice(CARDS))
dealer_total = card_calculator(dealer, "dealer")


### ____________________________checking highest score:
def highest_score_among_players():
    "checks for highest score among players"
    highest_score = 0
    highest_player_name = ""
    for _ in range(number_of_players):
        each_player_score = players_collection[_]["sum_of_cards"]
        player_name = players_collection[_]['name']
        if each_player_score > highest_score:
            highest_score = each_player_score
            highest_player_name = player_name
            
    return highest_score, highest_player_name
        
print(f"\nThe highest score is: ", highest_score_among_players())


# __________________________printing results:











print("\n---------------------------------------")
print(dealer, "which total", dealer_total)
print(players_collection)

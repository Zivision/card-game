from card import Deck

def dealer(deck: Deck) -> int:
    dealer_cards = [deck.random_card(), deck.random_card()]
   
    # Show top card from dealer
    print(f"Dealer top card is: {dealer_cards[1].card}\n")

    # Collect dealers total play value
    dealer_sum = 0
    for card in dealer_cards:
        if card.variant.name == "Ace":
            dealer_sum += 11
        else:
            dealer_sum += card.value
    return dealer_sum 

def player(deck: Deck) -> int:
    player_cards = [deck.random_card(), deck.random_card()]
    
    while True:
        # Show the player their cards
        print("Your cards: ")
        for i, card in enumerate(player_cards):
            print(f"Card {i + 1}: {card.card}")
        print(f"\nCards remaining: {deck.count_cards()}\n")
        res = input("Hit or Stand?: ")
        match res:
            case "Hit" | "hit":
                print("\nHit! Adding a card.\n")
                player_cards.append(deck.random_card())
            case "Stand" | "stand":
                print("\nStand! Calculating Score\n")
                break
            case _:
                print("\nInvalid input, try again.\n")

    player_sum = 0
    for card in player_cards:
        if card.variant.name == "Ace":
            player_sum += int(input("Ace found! 1 or 11?: "))
        else:
            player_sum += card.value
    return player_sum
        

def compare_score(deck: Deck):
    dealer_score = dealer(deck)
    player_score = player(deck)

    print(f"Dealer's score: {dealer_score}")
    print(f"Player's score: {player_score}")

    if player_score > 21: print("Player bust! dealer wins!")
    elif dealer_score > player_score: print("Dealer has higher score! Dealer wins!")
    elif dealer_score < player_score: print("Player has higher score! Player wins!")
    else: print("Draw!")

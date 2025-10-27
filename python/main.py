from card import Deck

def main():
    deck = Deck()
    deck.build_deck()
    deck.display_cards()
    deck.count_cards()

if __name__ == "__main__":
    main()
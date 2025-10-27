from enum import Enum
import random

class Suit(Enum):
    Clubs = 0
    Spades = 1
    Hearts = 2
    Diamonds = 3

class Variant(Enum):
    Ace = 0
    Two = 1
    Three = 2
    Four = 3
    Five = 4
    Six = 5
    Seven = 6
    Eight = 7
    Nine = 8
    Ten = 9
    Jack = 10
    Queen = 11
    King = 12

class Card:
    def __init__(self, suit: int, variant: int):
        self.suit = Suit(suit)
        self.variant = Variant(variant)
        self.value = self.find_value()
        self.card = "{} of {}. Value is: {}".format(
            self.variant.name, self.suit.name, self.value)

    def find_value(self) -> int:
        match self.variant.name:
            case "Ace":
                return [1, 11]
            case "Jack" | "Queen" | "King":
                return 10
            case _:
                return self.variant.value + 1
            

class Deck:
    def __init__ (self):
        self.deck = self.build_deck()

    def build_deck(self):
        deck = []
        for suit in range(4):
            for variant in range(13):
                deck.append(Card(suit, variant))
        return deck

    def random_card(self) -> Card:
        card = random.choice(self.deck)
        self.deck.remove(card)

        return card

    def display_cards(self):
        for card in self.deck:
            print(card.card)
    
    def count_cards(self):
        return len(self.deck)
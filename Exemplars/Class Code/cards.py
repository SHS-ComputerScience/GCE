import random

RANKS = ['Ace',
         'Two',
         'Three',
         'Four',
         'Five',
         'Six', 
         'Seven',
         'Eight',
         'Nine',
         'Ten',
         'Jack',
         'Queen',
         'King'
]
SUITS = ['Spades',
         'Hearts',
         'Clubs',
         'Diamonds'
]


class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return RANKS[self.rank] + ' of ' + SUITS[self.suit]


class Deck():
    cards = [Card(rank, suit) for suit in range(4) for rank in range(13)]

    def shuffle(self):
        for i in range(3):
            random.shuffle(self.cards)
    
    # def sort(self):
    #     pass
    
    def deal_card(self, player):
        player.hand.append(self.cards.pop())
    
    def print_deck(self):
        for card in self.cards:
            print(card)


class Player():
    hand = []

    def print_hand(self):
        for card in self.hand:
            print(card)



deck = Deck()
players = [Player(), Player()]

print(deck.cards[0])

# shuffle cards
# deal cards

# repeat until 1 player has no cards
#     player 1 puts card down
#     player 2 puts card down
#     check if card ranks match
#     if true, work out which player says snap
#         that player gets point and cards
#         repeat
#     if false
#         repeat
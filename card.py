
from random import shuffle
# import turtle

# wn = turtle.Screen()
# wn.bgcolor('black')
# wn.setup(600, 800)
# wn.title('Game')

# pen = turtle.Turtle()
# pen.speed(0)
# pen.hideturtle()

class Card:
    def __init__(self, suit, rank, srank, symbol):
        self.suit = suit
        self.rank = rank
        self.srank = srank
        self.symbol = symbol

    def show(self):
        print('{}{}'.format(self.srank, self.symbol))
    # def render(self, x, y, pen):
        # pen.penup

# card = Card('Clubs', 6)
# card.show()


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in []:
            for r in [['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'], ['8', '8'], ['9', '9'], ['10', '10'], ['Jack', 'J'], ['Queen', 'Q'], ['King', 'K'], ['Ace', 'A']]:
                self.cards.append(Card(s[0], r[0], r[1], s[1]))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        deck = self.cards
        shuffle(deck)
        shuffle(deck)
        shuffle(deck)

    def draw_card(self):
        return self.cards.pop()

# Deck().show()
#       OR
# deck =  Deck()
# deck.shuffle()
# deck.show()

# deck = Deck()
# deck.shuffle()
# card = deck.draw_card()
# card.show()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

    # def discard_card(self):
        # return self.hand.pop()


deck = Deck()
deck.shuffle()
bob = Player('Bob')
bob.draw_card(deck).draw_card(deck)
bob.show_hand()



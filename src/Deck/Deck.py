import random

from Card import Card
from Rank import Rank
from Suit import Suit


class Deck:
    def __init__(self, numDecks=1):
        self._deck = []
        for i in range(numDecks):
            for suit in Suit:
                for value in range(2, 15):
                    c = Card(Rank(value), suit)
                    self._deck.append(c)

    def __str__(self):
        return str(self._deck)

    def __repr__(self):
        return repr(self._deck)

    def size(self):
        return len(self._deck)

    def shuffle(self):
        random.shuffle(self._deck)

    def draw(self):
        return self._deck.pop(0)

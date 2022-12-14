import random

from src.Card.Card import Card
from src.Card.Rank import Rank
from src.Card.Suit import Suit


class Deck:
    def __init__(self, num_decks: int = 1) -> None:
        self._deck = []
        for i in range(num_decks):
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

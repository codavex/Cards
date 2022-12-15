import random

from src.Card.Card import Card
from src.Card.Rank import Rank
from src.Card.Suit import Suit


class Deck(list):
    def __init__(self, num_decks: int = 1) -> None:
        super().__init__()
        for i in range(num_decks):
            for suit in Suit:
                for value in range(2, 15):
                    c = Card(Rank(value), suit)
                    self.append(c)
    def size(self):
        return len(self)

    def shuffle(self):
        random.shuffle(self)

    def draw(self):
        return self.pop(0)

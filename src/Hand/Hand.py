from src.Card.Card import Card
from src.Card.Rank import Rank
from src.Card.Suit import Suit


class Hand(list):
    def size(self):
        return len(self)

    def draw(self):
        return super().pop(0)

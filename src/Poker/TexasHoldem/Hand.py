from src.Card.Card import Card
from src.Card.Rank import Rank
from src.Card.Suit import Suit
from src.Poker.TexasHoldem.Rank import Rank


class Hand:
    def __init__(self) -> None:
        self._hand = []

    def add(self, card):
        self._hand.append(card)

    def __str__(self):
        return str(self._hand)

    def __repr__(self):
        return repr(self._hand)

    def size(self):
        return len(self._hand)

    def rank(self, community):
        return Rank.FOUR_OAK

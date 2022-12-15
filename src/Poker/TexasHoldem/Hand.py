from src.Card.Card import Card
from src.Card.Rank import Rank
from src.Card.Suit import Suit
from src.Poker.Rank import Rank

from src.Hand.Hand import Hand


class Hand(Hand):
    def rank(self, community):
        flush_count = {}
        value_count = {}
        value_bitmap = 0

        flush = False

        for card in self + community:
            rank = card.get_rank().get_rank()
            suit = card.get_suit()

            if suit not in flush_count:
                flush_count[suit] = 0
            if rank not in value_count:
                value_count[rank] = 0
            flush_count[suit] += 1
            value_count[rank] += 1

        for suit in flush_count:
            if flush_count[suit] >= 5:
                flush = True

        return Rank.FOUR_OAK

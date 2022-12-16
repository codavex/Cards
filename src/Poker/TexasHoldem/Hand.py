import src.Hand.Hand
from src.Card.Rank import Rank
from src.Poker.Rank import Rank


class Hand(src.Hand.Hand.Hand):
    def rank(self, board):
        flush_count = {}
        value_count = {}

        flush = False
        straight = False
        three_oak = 0
        two_oak = 0

        for card in self + board:
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

        for rank in range(2, 11):
            if rank in value_count:
                if rank + 1 in value_count:
                    if rank + 2 in value_count:
                        if rank + 3 in value_count:
                            if rank + 4 in value_count:
                                straight = True

        if flush and straight:
            return Rank.STRAIGHT_FLUSH

        for rank in value_count:
            if value_count[rank] == 4:
                return Rank.FOUR_OAK
            elif value_count[rank] == 3:
                three_oak += 1
            elif value_count[rank] == 2:
                two_oak += 1

        if three_oak == 2:
            return Rank.FULL_HOUSE

        if three_oak == 1 and two_oak >= 1:
            return Rank.FULL_HOUSE

        if flush:
            return Rank.FLUSH

        if straight:
            return Rank.STRAIGHT

        if three_oak == 1:
            return Rank.THREE_OAK

        if two_oak >= 2:
            return Rank.TWO_TWO_OAK

        if two_oak == 1:
            return Rank.TWO_OAK

        return Rank.HIGH_CARD

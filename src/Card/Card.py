from src.Card.Rank import Rank
from src.Card.Suit import Suit


class Card:
    def __init__(self, *args):
        self._rank = None
        self._suit = None

        if len(args) == 1:
            self.constructor_with_string(args[0])
        elif len(args) == 2:
            self.constructor_with_rank_and_suit(args[0], args[1])
        else:
            raise ValueError("Bad argument(s) in Card constructor")

    def constructor_with_rank_and_suit(self, rank: Rank, suit: Suit) -> None:
        self._rank = rank
        self._suit = suit

    def constructor_with_string(self, card_str: str) -> None:
        length = len(card_str)
        if length > 3:
            raise ValueError("Bad argument in Card constructor")
        suit_str = card_str.upper()[-1]  # in case anyone uses lower case
        rank_str = card_str[:length - 1]
        for suit in Suit:
            if suit.name == suit_str:
                rank = Rank(Rank.key_from_value(rank_str))
                self.constructor_with_rank_and_suit(rank, suit)
                return
        raise ValueError("Bad argument in Card constructor")

    def __repr__(self):
        return "%s%s" % (repr(self._rank), self._suit.name)

    def __str__(self):
        return "%s of %s" % (str(self._rank), self._suit.value)

    def __eq__(self, other):
        return self._rank == other._rank

    def __ne__(self, other):
        return self._rank != other._rank

    def __lt__(self, other):
        return self._rank < other._rank

    def __le__(self, other):
        return self._rank <= other._rank

    def __gt__(self, other):
        return self._rank > other._rank

    def __ge__(self, other):
        return self._rank >= other._rank

    def get_rank(self):
        return self._rank

    def get_suit(self):
        return self._suit

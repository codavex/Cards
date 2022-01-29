class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

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

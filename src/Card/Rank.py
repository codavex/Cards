class Rank:
    def __init__(self, rank):
        self._rank = rank

    def _stringify(self):
        if self._rank == 11:
            return "J", "Jack"
        elif self._rank == 12:
            return "Q", "Queen"
        elif self._rank == 13:
            return "K", "King"
        elif self._rank == 14:
            return "A", "Ace"
        else:
            s = "%d" % self._rank
            return s, s

    def __repr__(self):
        return self._stringify()[0]

    def __str__(self):
        return self._stringify()[1]

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

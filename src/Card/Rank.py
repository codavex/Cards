class Rank:
    _str_mapping = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                    7: '7', 8: '8', 9: '9', 10: '10',
                    11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

    _repr_mapping = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                     7: '7', 8: '8', 9: '9', 10: '10',
                     11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

    def __init__(self, rank: int) -> None:
        if rank in range(2, 15):
            self._rank = rank
            return
        raise ValueError('Bad argument in Rank constructor')

    def get_rank(self):
        return self._rank

    def __repr__(self):
        return self._repr_mapping[self._rank]

    def __str__(self):
        return self._str_mapping[self._rank]

    def __eq__(self, other):
        return self._rank == other.get_rank()

    def __ne__(self, other):
        return self._rank != other.get_rank()

    def __lt__(self, other):
        return self._rank < other.get_rank()

    def __le__(self, other):
        return self._rank <= other.get_rank()

    def __gt__(self, other):
        return self._rank > other.get_rank()

    def __ge__(self, other):
        return self._rank >= other.get_rank()

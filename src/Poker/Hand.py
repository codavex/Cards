import src.Hand.Hand
from src.Card.Rank import Rank
from src.Poker.Rank import Rank


class Hand(src.Hand.Hand.Hand):

    def _is_flush(self):
        flush_count = {}

        for card in self:
            suit = card.get_suit()

            if suit not in flush_count:
                flush_count[suit] = 0
            flush_count[suit] += 1

        for suit in flush_count:
            if flush_count[suit] >= 5:
                return True, suit

        return None, False

    def _extract_suit(self, suit):
        flush = Hand()
        for card in self:
            if card.get_suit() == suit:
                flush.append(card)
        flush.sort(reverse=True)
        return flush

    def _is_straight(self):
        value_bitmap = 0

        for card in self:
            rank = card.get_rank().get_rank()
            value_bitmap |= (1 << rank)
            if rank == 14:  # aces can be low
                value_bitmap |= 1

        for rank in range(10, 0, -1):
            test = 31 << rank
            if test & value_bitmap == test:
                return True, rank + 4

        return False, None

    def _extract_straight(self, high_card):
        straight = Hand()
        next_card = high_card - 4
        for card in self:
            if (card.get_rank().get_rank() == next_card) or (next_card == 1 and card.get_rank().get_rank() == 14):
                straight.append(card)
                next_card += 1
        # straight.sort(reverse=True)
        return straight

    def _analyse(self):
        value_count = {}
        four_oak = 0
        three_oak = 0
        two_oak = 0

        for card in self:
            rank = card.get_rank().get_rank()

            if rank not in value_count:
                value_count[rank] = 0
            value_count[rank] += 1

        for rank in value_count:
            if value_count[rank] == 4:
                four_oak += 1
            elif value_count[rank] == 3:
                three_oak += 1
            elif value_count[rank] == 2:
                two_oak += 1

        return four_oak, three_oak, two_oak

    def rank(self):
        is_flush, suit = self._is_flush()

        if is_flush:
            flush = self._extract_suit(suit)
            is_straight, high_card = flush._is_straight()
            if is_straight:
                return Rank.STRAIGHT_FLUSH, flush._extract_straight(high_card)

        four_oak, three_oak, two_oak = self._analyse()

        if four_oak >= 1:
            return Rank.FOUR_OAK, self

        if three_oak == 2:
            return Rank.FULL_HOUSE, self

        if three_oak == 1 and two_oak >= 1:
            return Rank.FULL_HOUSE, self

        if is_flush:
            flush = self._extract_suit(suit)
            return Rank.FLUSH, flush[:5]

        is_straight, high_card = self._is_straight()

        if is_straight:
            straight = self._extract_straight(high_card)
            return Rank.STRAIGHT, straight

        if three_oak == 1:
            return Rank.THREE_OAK, self

        if two_oak >= 2:
            return Rank.TWO_TWO_OAK, self

        if two_oak == 1:
            return Rank.TWO_OAK, self

        return Rank.HIGH_CARD, self

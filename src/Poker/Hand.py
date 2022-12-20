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
            value_bitmap |= (1 << rank - 1)
            if rank == 14:  # aces can be low
                value_bitmap |= 1

        for rank in range(10, -1, -1):
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
        four_oak = []
        three_oak = []
        two_oak = []

        for card in self:
            rank = card.get_rank().get_rank()

            if rank not in value_count:
                value_count[rank] = 0
            value_count[rank] += 1

        for rank in value_count:
            if value_count[rank] == 4:
                four_oak.append(rank)
            elif value_count[rank] == 3:
                three_oak.append(rank)
            elif value_count[rank] == 2:
                two_oak.append(rank)

        return four_oak, three_oak, two_oak

    def rank(self):
        self.sort()
        is_flush, suit = self._is_flush()

        if is_flush:
            flush = self._extract_suit(suit)
            is_straight, high_card = flush._is_straight()
            if is_straight:
                return Rank.STRAIGHT_FLUSH, flush._extract_straight(high_card)

        four_oak, three_oak, two_oak = self._analyse()

        if len(four_oak) == 1:
            return_hand = list(filter(lambda card: card.get_rank().get_rank() == four_oak[0], self))
            leftovers = list(filter(lambda card: card.get_rank().get_rank() != four_oak[0], self))
            return Rank.FOUR_OAK, return_hand + leftovers[:1]

        if len(three_oak) == 2:
            three_oak.sort()
            high_three_oak = list(filter(lambda card: card.get_rank().get_rank() == three_oak[0], self))
            low_three_oak = list(filter(lambda card: card.get_rank().get_rank() == three_oak[1], self))
            return Rank.FULL_HOUSE, high_three_oak + low_three_oak[:2]

        if len(three_oak) == 1 and len(two_oak) >= 1:
            two_oak.sort()
            high_three_oak = list(filter(lambda card: card.get_rank().get_rank() == three_oak[0], self))
            high_two_oak = list(filter(lambda card: card.get_rank().get_rank() == two_oak[0], self))
            return Rank.FULL_HOUSE, high_three_oak + high_two_oak

        if is_flush:
            flush = self._extract_suit(suit)
            return Rank.FLUSH, flush[:5]

        is_straight, high_card = self._is_straight()

        if is_straight:
            straight = self._extract_straight(high_card)
            return Rank.STRAIGHT, straight

        if len(three_oak) == 1:
            return_hand = list(filter(lambda card: card.get_rank().get_rank() == three_oak[0], self))
            leftovers = list(filter(lambda card: card.get_rank().get_rank() != three_oak[0], self))
            return Rank.THREE_OAK, return_hand + leftovers[:2]

        if len(two_oak) >= 2:
            two_oak.sort()
            high_two_oak = list(filter(lambda card: card.get_rank().get_rank() == two_oak[0], self))
            low_two_oak = list(filter(lambda card: card.get_rank().get_rank() == two_oak[1], self))
            leftovers = list(filter(lambda card: card.get_rank().get_rank() not in two_oak, self))
            return Rank.TWO_TWO_OAK, high_two_oak + low_two_oak + leftovers[:1]

        if len(two_oak) == 1:
            return_hand = list(filter(lambda card: card.get_rank().get_rank() == two_oak[0], self))
            leftovers = list(filter(lambda card: card.get_rank().get_rank() != two_oak[0], self))
            return Rank.TWO_OAK, return_hand + leftovers[:3]

        return Rank.HIGH_CARD, self[:5]

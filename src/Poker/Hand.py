import src.Hand.Hand
from src.Card.Rank import Rank
from src.Card.Suit import Suit
from src.Poker.Rank import Rank


class Hand(src.Hand.Hand.Hand):
    _STRAIGHT_BITMAP = {14: 0b11111000000000,
                        13: 0b01111100000000,
                        12: 0b00111110000000,
                        11: 0b00011111000000,
                        10: 0b00001111100000,
                        9: 0b00000111110000,
                        8: 0b00000011111000,
                        7: 0b00000001111100,
                        6: 0b00000000111110,
                        5: 0b00000000011111,
                        }

    def _is_flush(self):
        flush_count = {Suit.S: 0, Suit.C: 0, Suit.H: 0, Suit.D: 0}

        for card in self:
            flush_count[card.suit] += 1

        for suit in flush_count:
            if flush_count[suit] >= 5:
                return True, suit

        return False, None

    def _extract_suit(self, suit):
        flush = Hand(filter(lambda card: card.suit == suit, self))
        return flush

    def _is_straight(self):
        value_bitmap = 0

        for card in self:
            rank = card.value
            value_bitmap |= (1 << rank - 1)
            if rank == 14:  # aces can be low
                value_bitmap |= 1

        for rank in self._STRAIGHT_BITMAP:
            test_value = self._STRAIGHT_BITMAP[rank]
            if test_value & value_bitmap == test_value:
                return True, rank
        return False, None

    def _extract_straight(self, high_card):
        self.sort(reverse=False)
        if high_card == 5:
            self.insert(0, self.pop())

        straight = Hand()
        next_card = high_card - 4
        for card in self:
            if (card.value == next_card) or \
                    (next_card == 1 and card.value == 14):
                straight.insert(0, card)
                next_card += 1
        return straight

    def _extract_cards_with_value(self, rank):
        return list(filter(lambda card: card.value == rank, self))

    def _extract_cards_without_value(self, ranks):
        return list(filter(lambda card: card.value not in ranks, self))

    def _analyse(self):
        value_count = {}
        four_oak = []
        three_oak = []
        two_oak = []

        for card in self:
            rank = card.value

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

        four_oak.sort(reverse=True)
        three_oak.sort(reverse=True)
        two_oak.sort(reverse=True)

        return four_oak, three_oak, two_oak[:2]

    def rank(self):
        self.sort(reverse=True)
        is_flush, suit = self._is_flush()

        if is_flush:
            flush = self._extract_suit(suit)
            is_straight, high_card = flush._is_straight()
            if is_straight:
                return Rank.STRAIGHT_FLUSH, flush._extract_straight(high_card)

        four_oak, three_oak, two_oak = self._analyse()

        if len(four_oak) == 1:
            return_hand = self._extract_cards_with_value(four_oak[0])
            leftovers = self._extract_cards_without_value(four_oak)
            return Rank.FOUR_OAK, return_hand + leftovers[:1]

        if len(three_oak) == 2:
            high_three_oak = self._extract_cards_with_value(three_oak[0])
            low_three_oak = self._extract_cards_with_value(three_oak[1])
            return Rank.FULL_HOUSE, high_three_oak + low_three_oak[:2]

        if len(three_oak) == 1 and len(two_oak) >= 1:
            high_three_oak = self._extract_cards_with_value(three_oak[0])
            high_two_oak = self._extract_cards_with_value(two_oak[0])
            return Rank.FULL_HOUSE, high_three_oak + high_two_oak

        if is_flush:
            flush = self._extract_suit(suit)
            return Rank.FLUSH, flush[:5]

        is_straight, high_card = self._is_straight()

        if is_straight:
            straight = self._extract_straight(high_card)
            return Rank.STRAIGHT, straight

        if len(three_oak) == 1:
            return_hand = self._extract_cards_with_value(three_oak[0])
            leftovers = self._extract_cards_without_value(three_oak)
            return Rank.THREE_OAK, return_hand + leftovers[:2]

        if len(two_oak) >= 2:
            high_two_oak = self._extract_cards_with_value(two_oak[0])
            low_two_oak = self._extract_cards_with_value(two_oak[1])
            leftovers = self._extract_cards_without_value(two_oak)
            return Rank.TWO_TWO_OAK, high_two_oak + low_two_oak + leftovers[:1]

        if len(two_oak) == 1:
            return_hand = self._extract_cards_with_value(two_oak[0])
            leftovers = self._extract_cards_without_value(two_oak)
            return Rank.TWO_OAK, return_hand + leftovers[:3]

        return Rank.HIGH_CARD, self[:5]

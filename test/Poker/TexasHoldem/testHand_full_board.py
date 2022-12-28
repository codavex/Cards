import unittest
from src.Card.Card import Card
from src.Poker.TexasHoldem.Hand import Hand
from src.Poker.Rank import Rank


# noinspection PyPep8Naming
class testHand(unittest.TestCase):
    def test_hand_ranking(self):
        test_cases = (
            ("[AS, KS]", "[QS, JS, 10S, AD, KD]", Rank.STRAIGHT_FLUSH, "\[AS, KS, QS, JS, 10S\]"),
            ("[AS, AC]", "[AH, AD, 2D, 2C, 2H]", Rank.FOUR_OAK, "\[A[SCHD], A[SCHD], A[SCHD], A[SCHD], 2[CHD]\]"),
            ("[AS, AC]", "[KH, KD, KS, 2S, 2S]", Rank.FULL_HOUSE, "\[K[SHD], K[SHD], K[SHD], A[SC], A[SC]\]"),
            ("[AS, 7S]", "[5S, 3S, 2S, 6H, 4D]", Rank.FLUSH, "\[AS, 7S, 5S, 3S, 2S\]"),
            ("[9S, 8C]", "[7H, 6D, 5D, 5H, 5C]", Rank.STRAIGHT, "\[9S, 8C, 7H, 6D, 5[CHD]\]"),
            ("[AS, 5C]", "[4H, 2D, 3D, 8C, 3C]", Rank.STRAIGHT, "\[5C, 4H, 3[CD], 2D, AS\]"),
            ("[AS, 10C]", "[KH, JD, QD, 8C, 3C]", Rank.STRAIGHT, "\[AS, KH, QD, JD, 10C\]"),
            ("[AS, AC]", "[AH, 3D, 2D, 9C, 6S]", Rank.THREE_OAK, "\[A[SCH], A[SCH], A[SCH], 9C, 6S\]"),
            ("[AS, AC]", "[KH, KD, 2D, 6C, 8S]", Rank.TWO_TWO_OAK, "\[A[SC], A[SC], K[HD], K[HD], 8S\]"),
            ("[AS, AC]", "[KH, KD, 6D, 6C, 4S]", Rank.TWO_TWO_OAK, "\[A[SC], A[SC], K[HD], K[HD], 6[CD]\]"),
            ("[AS, AC]", "[KH, KD, 6D, 6C, 8S]", Rank.TWO_TWO_OAK, "\[A[SC], A[SC], K[HD], K[HD], 8S\]"),
            ("[AS, AC]", "[3H, 4D, 2D, 8D, JD]", Rank.TWO_OAK, "\[A[SC], A[SC], JD, 8D, 4D\]"),
            ("[AS, KC]", "[8H, 5D, 2D, 9S, 3D]", Rank.HIGH_CARD, "\[AS, KC, 9S, 8H, 5D\]"),
        )
        for test_hole_cards, test_board, expected_rank, expected_best_regex in test_cases:
            with self.subTest(f"test {test_hole_cards} / {test_board} = {expected_rank}"):
                hole = Hand()
                hole.build_from_str(test_hole_cards)
                hole.shuffle()
                board = Hand()
                board.build_from_str(test_board)
                board.shuffle()
                rank, best_hand = hole.rank_with_board(board)
                self.assertEqual(expected_rank, rank)
                self.assertRegex(str(best_hand), expected_best_regex)


if __name__ == '__main__':
    unittest.main()

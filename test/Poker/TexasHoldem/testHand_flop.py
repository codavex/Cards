import unittest
from src.Card.Card import Card
from src.Poker.TexasHoldem.Hand import Hand
from src.Poker.Rank import Rank


# noinspection PyPep8Naming
class testHand(unittest.TestCase):
    def test_hand_ranking(self):
        test_cases = (
            ("[AS, KS]", "[QS, JS, 10S]", Rank.STRAIGHT_FLUSH, "\[AS, KS, QS, JS, 10S\]"),
            ("[AS, AC]", "[AH, AD, 2D]", Rank.FOUR_OAK, "\[A[SCHD], A[SCHD], A[SCHD], A[SCHD], 2D\]"),
            ("[KH, KD]", "[KS, AS, AC]", Rank.FULL_HOUSE, "\[K[SHD], K[SHD], K[SHD], A[SC], A[SC]\]"),
            ("[AS, 7S]", "[5S, 3S, 2S]", Rank.FLUSH, "\[AS, 7S, 5S, 3S, 2S\]"),
            ("[9S, 8C]", "[7H, 6D, 5D]", Rank.STRAIGHT, "\[9S, 8C, 7H, 6D, 5D\]"),
            ("[5C, 4H]", "[3D, 2D, AS]", Rank.STRAIGHT, "\[5C, 4H, 3D, 2D, AS\]"),
            ("[AS, KH]", "[QD, JD, 10C]", Rank.STRAIGHT, "\[AS, KH, QD, JD, 10C\]"),
            ("[AS, AC]", "[AH, 3D, 2D]", Rank.THREE_OAK, "\[A[SCH], A[SCH], A[SCH], 3D, 2D\]"),
            ("[AS, AC]", "[KH, KD, 2D]", Rank.TWO_TWO_OAK, "\[A[SC], A[SC], K[HD], K[HD], 2D\]"),
            ("[AS, AC]", "[4D, 3H, 2D]", Rank.TWO_OAK, "\[A[SC], A[SC], 4D, 3H, 2D\]"),
            ("[AS, KC]", "[8H, 5D, 2D]", Rank.HIGH_CARD, "\[AS, KC, 8H, 5D, 2D\]")
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

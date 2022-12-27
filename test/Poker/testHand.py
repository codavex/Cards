import unittest
from src.Poker.Hand import Hand
from src.Poker.Rank import Rank


# noinspection PyPep8Naming
class testHand(unittest.TestCase):
    def test_hand_ranking(self):
        test_cases = (
            ("[AS, KS, QS, JS, 10S]", Rank.STRAIGHT_FLUSH, "[AS, KS, QS, JS, 10S]"),
            ("[AS, AC, AH, AD, 2D]", Rank.FOUR_OAK, "[AS, AC, AH, AD, 2D]"),
            ("[KH, KD, KS, AS, AC]", Rank.FULL_HOUSE, "[KH, KD, KS, AS, AC]"),
            ("[AS, 7S, 5S, 3S, 2S]", Rank.FLUSH, "[AS, 7S, 5S, 3S, 2S]"),
            ("[9S, 8C, 7H, 6D, 5D]", Rank.STRAIGHT, "[9S, 8C, 7H, 6D, 5D]"),
            ("[5C, 4H, 3D, 2D, AS]", Rank.STRAIGHT, "[5C, 4H, 3D, 2D, AS]"),
            ("[AS, KH, QD, JD, 10C]", Rank.STRAIGHT, "[AS, KH, QD, JD, 10C]"),
            ("[AS, AC, AH, 3D, 2D]", Rank.THREE_OAK, "[AS, AC, AH, 3D, 2D]"),
            ("[AS, AC, KH, KD, 2D]", Rank.TWO_TWO_OAK, "[AS, AC, KH, KD, 2D]"),
            ("[AS, AC, 4D, 3H, 2D]", Rank.TWO_OAK, "[AS, AC, 4D, 3H, 2D]"),
            ("[AS, KC, 8H, 5D, 2D]", Rank.HIGH_CARD, "[AS, KC, 8H, 5D, 2D]")
        )
        for case, expected_rank, expected_best in test_cases:
            with self.subTest(f"test {case} = {expected_rank}"):
                hand = Hand()
                hand.build_from_str(case)
                rank, best_hand = hand.rank()
                self.assertEqual(expected_rank, rank)
                self.assertEqual(expected_best, best_hand.__str__())


if __name__ == '__main__':
    unittest.main()

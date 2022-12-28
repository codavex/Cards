import unittest
from src.Card.Card import Card
from src.Poker.TexasHoldem.Hand import Hand
from src.Poker.Rank import Rank


# noinspection PyPep8Naming
class testHand(unittest.TestCase):
    def test_hand_straight_flush(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("KS"))

        community.append(Card("QS"))
        community.append(Card("JS"))
        community.append(Card("10S"))
        community.append(Card("AD"))
        community.append(Card("KD"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.STRAIGHT_FLUSH, rank)
        self.assertEqual("[AS, KS, QS, JS, 10S]", str(best_hand))

    def test_hand_four_oak(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("AH"))
        community.append(Card("AD"))
        community.append(Card("2D"))
        community.append(Card("2C"))
        community.append(Card("2H"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.FOUR_OAK, rank)
        self.assertEqual("[AS, AC, AH, AD, 2D]", str(best_hand))

    def test_hand_full_house(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("KH"))
        community.append(Card("KD"))
        community.append(Card("KS"))
        community.append(Card("2S"))
        community.append(Card("2S"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.FULL_HOUSE, rank)
        self.assertEqual("[KH, KD, KS, AS, AC]", str(best_hand))

    def test_hand_flush(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("7S"))

        community.append(Card("5S"))
        community.append(Card("3S"))
        community.append(Card("2S"))
        community.append(Card("6H"))
        community.append(Card("4D"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.FLUSH, rank)
        self.assertEqual("[AS, 7S, 5S, 3S, 2S]", str(best_hand))

    def test_hand_straight(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("9S"))
        hole.append(Card("8C"))

        community.append(Card("7H"))
        community.append(Card("6D"))
        community.append(Card("5D"))
        community.append(Card("5H"))
        community.append(Card("5C"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.STRAIGHT, rank)
        self.assertEqual("[9S, 8C, 7H, 6D, 5D]", str(best_hand))

    def test_hand_straight_ace_low(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("5C"))

        community.append(Card("4H"))
        community.append(Card("2D"))
        community.append(Card("3D"))
        community.append(Card("8C"))
        community.append(Card("3C"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.STRAIGHT, rank)
        self.assertEqual("[5C, 4H, 3D, 2D, AS]", str(best_hand))

    def test_hand_straight_ace_high(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("10C"))

        community.append(Card("KH"))
        community.append(Card("JD"))
        community.append(Card("QD"))
        community.append(Card("8C"))
        community.append(Card("3C"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.STRAIGHT, rank)
        self.assertEqual("[AS, KH, QD, JD, 10C]", str(best_hand))

    def test_hand_three_oak(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("AH"))
        community.append(Card("3D"))
        community.append(Card("2D"))
        community.append(Card("9C"))
        community.append(Card("6S"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.THREE_OAK, rank)
        self.assertEqual("[AS, AC, AH, 9C, 6S]", str(best_hand))

    def test_hand_two_pair(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("KH"))
        community.append(Card("KD"))
        community.append(Card("2D"))
        community.append(Card("6C"))
        community.append(Card("8S"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.TWO_TWO_OAK, rank)
        self.assertEqual("[AS, AC, KH, KD, 8S]", str(best_hand))

    def test_hand_three_pair_a(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("KH"))
        community.append(Card("KD"))
        community.append(Card("6D"))
        community.append(Card("6C"))
        community.append(Card("4S"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.TWO_TWO_OAK, rank)
        self.assertEqual("[AS, AC, KH, KD, 6D]", str(best_hand))

    def test_hand_three_pair_b(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("KH"))
        community.append(Card("KD"))
        community.append(Card("6D"))
        community.append(Card("6C"))
        community.append(Card("8S"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.TWO_TWO_OAK, rank)
        self.assertEqual("[AS, AC, KH, KD, 8S]", str(best_hand))

    def test_hand_two_oak(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("3H"))
        community.append(Card("4D"))
        community.append(Card("2D"))
        community.append(Card("8D"))
        community.append(Card("JD"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.TWO_OAK, rank)
        self.assertEqual("[AS, AC, JD, 8D, 4D]", str(best_hand))

    def test_hand_high_card(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("KC"))

        community.append(Card("8H"))
        community.append(Card("5D"))
        community.append(Card("2D"))
        community.append(Card("9S"))
        community.append(Card("3D"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(Rank.HIGH_CARD, rank)
        self.assertEqual("[AS, KC, 9S, 8H, 5D]", str(best_hand))


if __name__ == '__main__':
    unittest.main()

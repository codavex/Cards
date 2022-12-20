import unittest
from src.Card.Card import Card
from src.Poker.Hand import Hand
from src.Poker.Rank import Rank


# noinspection PyPep8Naming
class testHand(unittest.TestCase):
    def test_hand_straight_flush(self):
        hand = Hand()

        hand.append(Card("AS"))
        hand.append(Card("KS"))
        hand.append(Card("QS"))
        hand.append(Card("JS"))
        hand.append(Card("10S"))

        rank, best_hand = hand.rank()
        self.assertEqual(rank, Rank.STRAIGHT_FLUSH)
        self.assertEqual("[AS, KS, QS, JS, 10S]", best_hand.__str__())

    def test_hand_four_oak(self):
        hand = Hand()

        hand.append(Card("AS"))
        hand.append(Card("AC"))
        hand.append(Card("AH"))
        hand.append(Card("AD"))
        hand.append(Card("2D"))

        rank, best_hand = hand.rank()
        self.assertEqual(Rank.FOUR_OAK, rank)
        self.assertEqual("[AS, AC, AH, AD, 2D]", best_hand.__str__())

    def test_hand_full_house(self):
        hand = Hand()

        hand.append(Card("AS"))
        hand.append(Card("AC"))
        hand.append(Card("KH"))
        hand.append(Card("KD"))
        hand.append(Card("KS"))

        rank, best_hand = hand.rank()
        self.assertEqual(Rank.FULL_HOUSE, rank)
        self.assertEqual("[KH, KD, KS, AS, AC]", best_hand.__str__())

    def test_hand_flush(self):
        hand = Hand()

        hand.append(Card("AS"))
        hand.append(Card("7S"))
        hand.append(Card("5S"))
        hand.append(Card("3S"))
        hand.append(Card("2S"))

        rank, best_hand = hand.rank()
        self.assertEqual(Rank.FLUSH, rank)
        self.assertEqual("[AS, 7S, 5S, 3S, 2S]", best_hand.__str__())

    def test_hand_straight(self):
        hand = Hand()

        hand.append(Card("9S"))
        hand.append(Card("8C"))
        hand.append(Card("7H"))
        hand.append(Card("6D"))
        hand.append(Card("5D"))

        rank, best_hand = hand.rank()
        self.assertEqual(Rank.STRAIGHT, rank)
        self.assertEqual("[9S, 8C, 7H, 6D, 5D]", best_hand.__str__())

    def test_hand_straight_ace_low(self):
        hand = Hand()

        hand.append(Card("AS"))
        hand.append(Card("5C"))
        hand.append(Card("4H"))
        hand.append(Card("2D"))
        hand.append(Card("3D"))

        rank, best_hand = hand.rank()
        self.assertEqual(Rank.STRAIGHT, rank)
        self.assertEqual("[5C, 4H, 3D, 2D, AS]", best_hand.__str__())

    def test_hand_straight_ace_high(self):
        hand = Hand()

        hand.append(Card("AS"))
        hand.append(Card("10C"))
        hand.append(Card("KH"))
        hand.append(Card("JD"))
        hand.append(Card("QD"))

        rank, best_hand = hand.rank()
        self.assertEqual(Rank.STRAIGHT, rank)
        self.assertEqual("[AS, KH, QD, JD, 10C]", best_hand.__str__())

    def test_hand_three_oak(self):
        hand = Hand()

        hand.append(Card("AS"))
        hand.append(Card("AC"))
        hand.append(Card("AH"))
        hand.append(Card("3D"))
        hand.append(Card("2D"))

        rank, best_hand = hand.rank()
        self.assertEqual(Rank.THREE_OAK, rank)
        self.assertEqual("[AS, AC, AH, 3D, 2D]", best_hand.__str__())

    def test_hand_two_pair(self):
        hand = Hand()

        hand.append(Card("AS"))
        hand.append(Card("AC"))
        hand.append(Card("KH"))
        hand.append(Card("KD"))
        hand.append(Card("2D"))

        rank, best_hand = hand.rank()
        self.assertEqual(Rank.TWO_TWO_OAK, rank)
        self.assertEqual("[AS, AC, KH, KD, 2D]", best_hand.__str__())

    def test_hand_two_oak(self):
        hand = Hand()

        hand.append(Card("AS"))
        hand.append(Card("AC"))
        hand.append(Card("3H"))
        hand.append(Card("4D"))
        hand.append(Card("2D"))

        rank, best_hand = hand.rank()
        self.assertEqual(Rank.TWO_OAK, rank)
        self.assertEqual("[AS, AC, 4D, 3H, 2D]", best_hand.__str__())

    def test_hand_high_card(self):
        hand = Hand()

        hand.append(Card("AS"))
        hand.append(Card("KC"))
        hand.append(Card("8H"))
        hand.append(Card("5D"))
        hand.append(Card("2D"))

        rank, best_hand = hand.rank()
        self.assertEqual(Rank.HIGH_CARD, rank)
        self.assertEqual("[AS, KC, 8H, 5D, 2D]", best_hand.__str__())


if __name__ == '__main__':
    unittest.main()

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

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(rank, Rank.STRAIGHT_FLUSH)

    def test_hand_four_oak(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("AH"))
        community.append(Card("AD"))
        community.append(Card("2D"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(rank, Rank.FOUR_OAK)

    def test_hand_full_house(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("KH"))
        community.append(Card("KD"))
        community.append(Card("KS"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(rank, Rank.FULL_HOUSE)

    def test_hand_flush(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("7S"))

        community.append(Card("5S"))
        community.append(Card("3S"))
        community.append(Card("2S"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(rank, Rank.FLUSH)

    def test_hand_straight(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("9S"))
        hole.append(Card("8C"))

        community.append(Card("7H"))
        community.append(Card("6D"))
        community.append(Card("5D"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(rank, Rank.STRAIGHT)

    def test_hand_three_oak(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("AH"))
        community.append(Card("3D"))
        community.append(Card("2D"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(rank, Rank.THREE_OAK)

    def test_hand_two_pair(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("KH"))
        community.append(Card("KD"))
        community.append(Card("2D"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(rank, Rank.TWO_TWO_OAK)

    def test_hand_two_oak(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("3H"))
        community.append(Card("4D"))
        community.append(Card("2D"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(rank, Rank.TWO_OAK)

    def test_hand_high_card(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("KC"))

        community.append(Card("8H"))
        community.append(Card("5D"))
        community.append(Card("2D"))

        rank, best_hand = hole.rank_with_board(community)
        self.assertEqual(rank, Rank.HIGH_CARD)


if __name__ == '__main__':
    unittest.main()
import unittest
from src.Card.Card import Card
from src.Poker.TexasHoldem.Hand import Hand
from src.Poker.Rank import Rank


class testHand(unittest.TestCase):

    def test_empty_hand(self):
        hole = Hand()

        self.assertEqual(hole.size(), 0)
        self.assertEqual(hole.__str__(), "[]")
        self.assertEqual(hole.__repr__(), "[]")

    def test_pocket_aces_hand(self):
        hole = Hand()

        hole.add(Card("AS"))
        hole.add(Card("AC"))

        self.assertEqual(hole.size(), 2)
        self.assertEqual(hole.__str__(), "[AS, AC]")
        self.assertEqual(hole.__repr__(), "[AS, AC]")

    def test_hand_4oak(self):
        hole = Hand()
        community = Hand()

        hole.add(Card("AS"))
        hole.add(Card("AC"))

        community.add(Card("AH"))
        community.add(Card("AD"))
        community.add(Card("2D"))

        self.assertEqual(hole.rank(community), Rank.FOUR_OAK)


if __name__ == '__main__':
    unittest.main()

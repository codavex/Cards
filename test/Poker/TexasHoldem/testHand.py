import unittest
from src.Card.Card import Card
from src.Poker.TexasHoldem.Hand import Hand
from src.Poker.TexasHoldem.Rank import Rank

class testHand(unittest.TestCase):

    def test_enpty_hand(self):
        hole = Hand()

        self.assertEqual(hole.size(), 0)
        self.assertEqual(hole.__str__(), "[]")
        self.assertEqual(hole.__repr__(), "[]")

    def test_enpty_hand(self):
        hole = Hand()

        hole.add(Card("AS"))
        hole.add(Card("AC"))

        self.assertEqual(hole.size(), 2)
        self.assertEqual(hole.__str__(), "[AS, AC]")
        self.assertEqual(hole.__repr__(), "[AS, AC]")


if __name__ == '__main__':
    unittest.main()

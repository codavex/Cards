import unittest
from src.Card.Card import Card
from src.Card.Suit import Suit
from src.Blackjack.Hand import Hand


# noinspection PyPep8Naming
class testHand(unittest.TestCase):

    def test_hand_score(self):
        hand = Hand()
        hand.append(Card(2, Suit.S))
        hand.append(Card(2, Suit.C))
        self.assertEqual({4}, hand.score())

        hand = Hand()
        hand.append(Card(11, Suit.S))
        hand.append(Card(12, Suit.C))
        self.assertEqual({20}, hand.score())

        hand = Hand()
        hand.append(Card(13, Suit.S))
        hand.append(Card(14, Suit.C))
        self.assertEqual({11, 21}, hand.score())

        hand = Hand()
        hand.append(Card(14, Suit.S))
        hand.append(Card(14, Suit.C))
        self.assertEqual({2, 12}, hand.score())

        hand = Hand()
        hand.append(Card(14, Suit.S))
        hand.append(Card(14, Suit.C))
        hand.append(Card(14, Suit.H))
        self.assertEqual({3, 13}, hand.score())

        hand = Hand()
        hand.append(Card(14, Suit.S))
        hand.append(Card(14, Suit.C))
        hand.append(Card(14, Suit.H))
        hand.append(Card(14, Suit.D))
        self.assertEqual({4, 14}, hand.score())

        hand = Hand()
        hand.append(Card(14, Suit.S))
        hand.append(Card(14, Suit.C))
        hand.append(Card(14, Suit.H))
        hand.append(Card(14, Suit.D))
        hand.append(Card(14, Suit.S))
        self.assertEqual({5, 15}, hand.score())


if __name__ == '__main__':
    unittest.main()

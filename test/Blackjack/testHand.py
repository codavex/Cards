import unittest
from src.Card.Card import Card
from src.Card.Suit import Suit
from src.Blackjack.Hand import Hand


class testHand(unittest.TestCase):

    def test_hand_score(self):
        hand = Hand()
        hand.append(Card(2, Suit.S))
        hand.append(Card(2, Suit.C))
        self.assertEqual(hand.score(), {4})

        hand = Hand()
        hand.append(Card(11, Suit.S))
        hand.append(Card(12, Suit.C))
        self.assertEqual(hand.score(), {20})

        hand = Hand()
        hand.append(Card(13, Suit.S))
        hand.append(Card(14, Suit.C))
        self.assertEqual(hand.score(), {11, 21})

        hand = Hand()
        hand.append(Card(14, Suit.S))
        hand.append(Card(14, Suit.C))
        self.assertEqual(hand.score(), {2, 12})

        hand = Hand()
        hand.append(Card(14, Suit.S))
        hand.append(Card(14, Suit.C))
        hand.append(Card(14, Suit.H))
        self.assertEqual(hand.score(), {3, 13})

        hand = Hand()
        hand.append(Card(14, Suit.S))
        hand.append(Card(14, Suit.C))
        hand.append(Card(14, Suit.H))
        hand.append(Card(14, Suit.D))
        self.assertEqual(hand.score(), {4, 14})

        hand = Hand()
        hand.append(Card(14, Suit.S))
        hand.append(Card(14, Suit.C))
        hand.append(Card(14, Suit.H))
        hand.append(Card(14, Suit.D))
        hand.append(Card(14, Suit.S))
        self.assertEqual(hand.score(), {5, 15})


if __name__ == '__main__':
    unittest.main()

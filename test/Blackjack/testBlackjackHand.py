import unittest
from src.Card.Card import Card
from src.Card.Suit import Suit
from src.Blackjack.BlackjackHand import BlackjackHand


class testBlackjackHand(unittest.TestCase):

    def test_hand_score(self):
        hand = BlackjackHand()
        hand.draw(Card(2, Suit.S))
        hand.draw(Card(2, Suit.C))
        self.assertEqual(hand.score(), {4})

        hand = BlackjackHand()
        hand.draw(Card(11, Suit.S))
        hand.draw(Card(12, Suit.C))
        self.assertEqual(hand.score(), {20})

        hand = BlackjackHand()
        hand.draw(Card(13, Suit.S))
        hand.draw(Card(14, Suit.C))
        self.assertEqual(hand.score(), {11, 21})

        hand = BlackjackHand()
        hand.draw(Card(14, Suit.S))
        hand.draw(Card(14, Suit.C))
        self.assertEqual(hand.score(), {2, 12})

        hand = BlackjackHand()
        hand.draw(Card(14, Suit.S))
        hand.draw(Card(14, Suit.C))
        hand.draw(Card(14, Suit.H))
        self.assertEqual(hand.score(), {3, 13})

        hand = BlackjackHand()
        hand.draw(Card(14, Suit.S))
        hand.draw(Card(14, Suit.C))
        hand.draw(Card(14, Suit.H))
        hand.draw(Card(14, Suit.D))
        self.assertEqual(hand.score(), {4, 14})

        hand = BlackjackHand()
        hand.draw(Card(14, Suit.S))
        hand.draw(Card(14, Suit.C))
        hand.draw(Card(14, Suit.H))
        hand.draw(Card(14, Suit.D))
        hand.draw(Card(14, Suit.S))
        self.assertEqual(hand.score(), {5, 15})


if __name__ == '__main__':
    unittest.main()

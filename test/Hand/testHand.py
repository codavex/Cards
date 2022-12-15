import unittest
from src.Card.Card import Card
from src.Hand.Hand import Hand


class testHand(unittest.TestCase):

    def test_empty_hand(self):
        hand = Hand()

        self.assertEqual(hand.size(), 0)
        self.assertEqual(hand.__str__(), "[]")
        self.assertEqual(hand.__repr__(), "[]")

    def test_pocket_append_cards(self):
        hand = Hand()

        hand.append(Card("AS"))

        self.assertEqual(hand.size(), 1)
        self.assertEqual(hand.__str__(), "[AS]")
        self.assertEqual(hand.__repr__(), "[AS]")

        hand.append(Card("AC"))

        self.assertEqual(hand.size(), 2)
        self.assertEqual(hand.__str__(), "[AS, AC]")
        self.assertEqual(hand.__repr__(), "[AS, AC]")


if __name__ == '__main__':
    unittest.main()

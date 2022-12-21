import unittest
from src.Card.Card import Card
from src.Hand.Hand import Hand


# noinspection PyPep8Naming
class testHand(unittest.TestCase):

    def test_empty_hand(self):
        hand = Hand()

        self.assertEqual(0, hand.size())
        self.assertEqual("[]", str(hand))
        self.assertEqual("[]", str(hand))

    def test_pocket_append_cards(self):
        hand = Hand()

        hand.append(Card("AS"))

        self.assertEqual(1, hand.size())
        self.assertEqual("[AS]", str(hand))

        hand.append(Card("AC"))

        self.assertEqual(2, hand.size())
        self.assertEqual("[AS, AC]", str(hand))


if __name__ == '__main__':
    unittest.main()

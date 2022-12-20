import unittest
from src.Card.Card import Card
from src.Hand.Hand import Hand


# noinspection PyPep8Naming
class testHand(unittest.TestCase):

    def test_empty_hand(self):
        hand = Hand()

        self.assertEqual(0, hand.size())
        self.assertEqual("[]", hand.__str__())
        self.assertEqual("[]", hand.__repr__())

    def test_pocket_append_cards(self):
        hand = Hand()

        hand.append(Card("AS"))

        self.assertEqual(1, hand.size())
        self.assertEqual("[AS]", hand.__str__())
        self.assertEqual("[AS]", hand.__repr__())

        hand.append(Card("AC"))

        self.assertEqual(2, hand.size())
        self.assertEqual("[AS, AC]", hand.__str__())
        self.assertEqual("[AS, AC]", hand.__repr__())


if __name__ == '__main__':
    unittest.main()

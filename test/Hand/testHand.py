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

    def test_build_from_str(self):
        test_cases = (
            "[AS, AC, AH, AD, 2D]",
            "[KH, KD, KS, AS, AC]",
            "[AS, 7S, 5S, 3S, 2S]",
            "[9S, 8C, 7H, 6D, 5D]",
            "[5C, 4H, 3D, 2D, AS]",
            "[AS, KH, QD, JD, 10C]",
            "[AS, AC, AH, 3D, 2D]"
        )

        for case in test_cases:
            with self.subTest(f"build {case}"):
                hand = Hand()
                hand.build_from_str(case)
                self.assertEqual(case, str(hand))


if __name__ == '__main__':
    unittest.main()

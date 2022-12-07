import unittest
from Card import Card
from Rank import Rank
from Suit import Suit


class testCard(unittest.TestCase):

    def setUp(self):
        self.s = Suit.S
        self.c = Suit.C
        self.h = Suit.H
        self.d = Suit.D

        self.two = Rank(2)
        self.three = Rank(3)

        self.j = Rank(11)
        self.q = Rank(12)
        self.k = Rank(13)
        self.a = Rank(14)

    def test_card_repr(self):
        card = Card(self.two, self.s)
        self.assertEqual(repr(card), "2S")

        card = Card(self.j, self.s)
        self.assertEqual(repr(card), "JS")

        card = Card(self.q, self.c)
        self.assertEqual(repr(card), "QC")

        card = Card(self.k, self.h)
        self.assertEqual(repr(card), "KH")

        card = Card(self.a, self.d)
        self.assertEqual(repr(card), "AD")

    def test_card_str(self):
        card = Card(self.two, self.s)
        self.assertEqual(str(card), "2 of Spades")

        card = Card(self.j, self.s)
        self.assertEqual(str(card), "Jack of Spades")

        card = Card(self.q, self.c)
        self.assertEqual(str(card), "Queen of Clubs")

        card = Card(self.k, self.h)
        self.assertEqual(str(card), "King of Hearts")

        card = Card(self.a, self.d)
        self.assertEqual(str(card), "Ace of Diamonds")

    def test_card_gt(self):
        card1 = Card(self.two, self.c)
        card2 = Card(self.three, self.c)
        self.assertTrue(card2 > card1)
        self.assertTrue(card1 < card2)
        self.assertTrue(card1 != card2)


if __name__ == '__main__':
    unittest.main()

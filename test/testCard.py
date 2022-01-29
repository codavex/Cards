import unittest
from Card import Card
from Rank import Rank
from Suit import Suit


class testCard(unittest.TestCase):

    def test_card_repr(self):
        card = Card(Rank(2), Suit.S)
        self.assertEqual(repr(card), "2S")
        card = Card(Rank(11), Suit.S)
        self.assertEqual(repr(card), "JS")
        card = Card(Rank(12), Suit.C)
        self.assertEqual(repr(card), "QC")
        card = Card(Rank(13), Suit.H)
        self.assertEqual(repr(card), "KH")
        card = Card(Rank(14), Suit.D)
        self.assertEqual(repr(card), "AD")

    def test_card_str(self):
        card = Card(Rank(2), Suit.S)
        self.assertEqual(str(card), "2 of Spades")
        card = Card(Rank(11), Suit.S)
        self.assertEqual(str(card), "Jack of Spades")
        card = Card(Rank(12), Suit.C)
        self.assertEqual(str(card), "Queen of Clubs")
        card = Card(Rank(13), Suit.H)
        self.assertEqual(str(card), "King of Hearts")
        card = Card(Rank(14), Suit.D)
        self.assertEqual(str(card), "Ace of Diamonds")

    def test_card_gt(self):
        card1 = Card(Rank(2), Suit.C)
        card2 = Card(Rank(3), Suit.C)
        self.assertTrue(card2 > card1)
        self.assertTrue(card1 < card2)
        self.assertTrue(card1 != card2)


if __name__ == '__main__':
    unittest.main()

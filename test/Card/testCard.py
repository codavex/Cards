import unittest
from src.Card.Card import Card
from src.Card.Rank import Rank
from src.Card.Suit import Suit


class testCard(unittest.TestCase):

    def setUp(self):
        self.card_2s = Card(Rank(2), Suit.S)
        self.card_js = Card(Rank(11), Suit.S)
        self.card_qc = Card(Rank(12), Suit.C)
        self.card_kh = Card(Rank(13), Suit.H)
        self.card_ad = Card(Rank(14), Suit.D)

    def test_card_repr(self):
        self.assertEqual(repr(self.card_2s), "2S")
        self.assertEqual(repr(self.card_js), "JS")
        self.assertEqual(repr(self.card_qc), "QC")
        self.assertEqual(repr(self.card_kh), "KH")
        self.assertEqual(repr(self.card_ad), "AD")

    def test_card_str(self):
        self.assertEqual(str(self.card_2s), "2 of Spades")
        self.assertEqual(str(self.card_js), "Jack of Spades")
        self.assertEqual(str(self.card_qc), "Queen of Clubs")
        self.assertEqual(str(self.card_kh), "King of Hearts")
        self.assertEqual(str(self.card_ad), "Ace of Diamonds")

    def test_card_gt(self):
        self.assertTrue(self.card_ad > self.card_kh)
        self.assertTrue(self.card_kh > self.card_qc)
        self.assertTrue(self.card_qc > self.card_js)
        self.assertTrue(self.card_js > self.card_2s)

        self.assertTrue(self.card_2s < self.card_js)
        self.assertTrue(self.card_js < self.card_qc)
        self.assertTrue(self.card_qc < self.card_kh)
        self.assertTrue(self.card_kh < self.card_ad)

        self.assertTrue(self.card_2s != self.card_js)
        self.assertTrue(self.card_js != self.card_qc)
        self.assertTrue(self.card_qc != self.card_kh)
        self.assertTrue(self.card_kh != self.card_ad)


if __name__ == '__main__':
    unittest.main()

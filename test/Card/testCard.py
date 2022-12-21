import unittest
from src.Card.Card import Card
from src.Card.Rank import Rank
from src.Card.Suit import Suit


# noinspection PyPep8Naming
class testCard(unittest.TestCase):

    def setUp(self):
        self.card_2s = Card(Rank(2), Suit.S)
        self.card_js = Card(Rank(11), Suit.S)
        self.card_qc = Card(Rank(12), Suit.C)
        self.card_kh = Card(Rank(13), Suit.H)
        self.card_ad = Card(Rank(14), Suit.D)

    def test_card_repr(self):
        self.assertEqual("2S", repr(self.card_2s))
        self.assertEqual("JS", repr(self.card_js))
        self.assertEqual("QC", repr(self.card_qc))
        self.assertEqual("KH", repr(self.card_kh))
        self.assertEqual("AD", repr(self.card_ad))

    def test_card_str(self):
        self.assertEqual("2S", str(self.card_2s))
        self.assertEqual("JS", str(self.card_js))
        self.assertEqual("QC", str(self.card_qc))
        self.assertEqual("KH", str(self.card_kh))
        self.assertEqual("AD", str(self.card_ad))

    def test_card_gt(self):
        self.assertTrue(self.card_ad > self.card_kh)
        self.assertTrue(self.card_kh > self.card_qc)
        self.assertTrue(self.card_qc > self.card_js)
        self.assertTrue(self.card_js > self.card_2s)

    def test_card_ge(self):
        self.assertTrue(self.card_ad >= self.card_ad)
        self.assertTrue(self.card_ad >= self.card_kh)
        self.assertTrue(self.card_kh >= self.card_kh)
        self.assertTrue(self.card_kh >= self.card_qc)
        self.assertTrue(self.card_qc >= self.card_qc)
        self.assertTrue(self.card_qc >= self.card_js)
        self.assertTrue(self.card_js >= self.card_js)
        self.assertTrue(self.card_js >= self.card_2s)
        self.assertTrue(self.card_2s >= self.card_2s)

    def test_card_lt(self):
        self.assertTrue(self.card_2s < self.card_js)
        self.assertTrue(self.card_js < self.card_qc)
        self.assertTrue(self.card_qc < self.card_kh)
        self.assertTrue(self.card_kh < self.card_ad)

    def test_card_le(self):
        self.assertTrue(self.card_2s <= self.card_2s)
        self.assertTrue(self.card_2s <= self.card_js)
        self.assertTrue(self.card_js <= self.card_js)
        self.assertTrue(self.card_js <= self.card_qc)
        self.assertTrue(self.card_qc <= self.card_qc)
        self.assertTrue(self.card_qc <= self.card_kh)
        self.assertTrue(self.card_kh <= self.card_kh)
        self.assertTrue(self.card_kh <= self.card_ad)

    def test_card_ne(self):
        self.assertTrue(self.card_2s != self.card_js)
        self.assertTrue(self.card_js != self.card_qc)
        self.assertTrue(self.card_qc != self.card_kh)
        self.assertTrue(self.card_kh != self.card_ad)

    def test_card_eq(self):
        my_card_2d = Card(Rank(2), Suit.D)
        my_card_jd = Card(Rank(11), Suit.D)
        my_card_qh = Card(Rank(12), Suit.H)
        my_card_kc = Card(Rank(13), Suit.C)
        my_card_as = Card(Rank(14), Suit.S)

        self.assertTrue(self.card_2s == my_card_2d)
        self.assertTrue(self.card_js == my_card_jd)
        self.assertTrue(self.card_qc == my_card_qh)
        self.assertTrue(self.card_kh == my_card_kc)
        self.assertTrue(self.card_ad == my_card_as)

    def test_construct_from_string(self):
        card_2s_str = '2S'
        card_js_str = 'JS'
        card_qc_str = 'QC'
        card_kh_str = 'KH'
        card_ad_str = 'AD'
        card_td_str = '10D'

        card_2s = Card(card_2s_str)
        card_js = Card(card_js_str)
        card_qc = Card(card_qc_str)
        card_kh = Card(card_kh_str)
        card_ad = Card(card_ad_str)
        card_td = Card(card_td_str)

        self.assertEqual(card_2s_str, repr(card_2s))
        self.assertEqual(card_js_str, repr(card_js))
        self.assertEqual(card_qc_str, repr(card_qc))
        self.assertEqual(card_kh_str, repr(card_kh))
        self.assertEqual(card_ad_str, repr(card_ad))
        self.assertEqual(card_td_str, repr(card_td))

    # noinspection PyUnusedLocal
    def test_bad_card_string_rank_1(self):
        with self.assertRaises(ValueError) as context:
            card = Card("1S")

    # noinspection PyUnusedLocal
    def test_bad_card_string_rank_15(self):
        with self.assertRaises(ValueError) as context:
            card = Card("15S")

    # noinspection PyUnusedLocal
    def test_bad_card_string_suit(self):
        with self.assertRaises(ValueError) as context:
            card = Card("2T")

    # noinspection PyUnusedLocal
    def test_bad_card_string_too_long(self):
        with self.assertRaises(ValueError) as context:
            card = Card("2 of Spades")


if __name__ == '__main__':
    unittest.main()

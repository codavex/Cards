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
        test_cases = (
            ("2S", self.card_2s),
            ("JS", self.card_js),
            ("QC", self.card_qc),
            ("KH", self.card_kh),
            ("AD", self.card_ad)
        )

        for expected_repr, test_instance in test_cases:
            with self.subTest(f"{expected_repr} == repr({test_instance})"):
                self.assertEqual(expected_repr, repr(test_instance))

    def test_card_str(self):
        test_cases = (
            ("2S", self.card_2s),
            ("JS", self.card_js),
            ("QC", self.card_qc),
            ("KH", self.card_kh),
            ("AD", self.card_ad)
        )

        for expected_repr, test_instance in test_cases:
            with self.subTest(f"{expected_repr} == str({test_instance})"):
                self.assertEqual(expected_repr, str(test_instance))

    def test_card_gt(self):
        test_cases = (
            (self.card_ad, self.card_kh),
            (self.card_kh, self.card_qc),
            (self.card_qc, self.card_js),
            (self.card_js, self.card_2s),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} > {instance_b}"):
                self.assertTrue(instance_a > instance_b)

    def test_card_ge(self):
        test_cases = (
            (self.card_ad, self.card_ad),
            (self.card_ad, self.card_kh),
            (self.card_kh, self.card_kh),
            (self.card_kh, self.card_qc),
            (self.card_qc, self.card_qc),
            (self.card_qc, self.card_js),
            (self.card_js, self.card_js),
            (self.card_js, self.card_2s),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} >= {instance_b}"):
                self.assertTrue(instance_a >= instance_b)

    def test_card_lt(self):
        test_cases = (
            (self.card_2s, self.card_js),
            (self.card_js, self.card_qc),
            (self.card_qc, self.card_kh),
            (self.card_kh, self.card_ad),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} < {instance_b}"):
                self.assertTrue(instance_a < instance_b)

    def test_card_le(self):
        self.assertTrue(self.card_2s <= self.card_2s)
        self.assertTrue(self.card_2s <= self.card_js)
        self.assertTrue(self.card_js <= self.card_js)
        self.assertTrue(self.card_js <= self.card_qc)
        self.assertTrue(self.card_qc <= self.card_qc)
        self.assertTrue(self.card_qc <= self.card_kh)
        self.assertTrue(self.card_kh <= self.card_kh)
        self.assertTrue(self.card_kh <= self.card_ad)
        test_cases = (
            (self.card_2s, self.card_2s),
            (self.card_2s, self.card_js),
            (self.card_js, self.card_js),
            (self.card_js, self.card_qc),
            (self.card_qc, self.card_qc),
            (self.card_qc, self.card_kh),
            (self.card_kh, self.card_kh),
            (self.card_kh, self.card_ad),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} <= {instance_b}"):
                self.assertTrue(instance_a <= instance_b)

    def test_card_ne(self):
        test_cases = (
            (self.card_2s, self.card_js),
            (self.card_js, self.card_qc),
            (self.card_qc, self.card_kh),
            (self.card_kh, self.card_ad),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} != {instance_b}"):
                self.assertTrue(instance_a != instance_b)

    def test_card_eq(self):
        test_cases = (
            (self.card_2s, Card(Rank(2), Suit.D)),
            (self.card_js, Card(Rank(11), Suit.D)),
            (self.card_qc, Card(Rank(12), Suit.H)),
            (self.card_kh, Card(Rank(13), Suit.C)),
            (self.card_ad, Card(Rank(14), Suit.S)),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} == {instance_b}"):
                self.assertTrue(instance_a == instance_b)

    def test_construct_from_string(self):
        test_cases = ('2S', 'JS', 'QC', 'KH', 'AD', '10D')

        for init_str in test_cases:
            with self.subTest(f"Card(\"{init_str}\")"):
                self.assertTrue(init_str == repr(Card(init_str)))

    # noinspection PyUnusedLocal
    def test_bad_card_string_rank_1(self):
        with self.assertRaises(ValueError):
            card = Card("1S")

    # noinspection PyUnusedLocal
    def test_bad_card_string_rank_15(self):
        with self.assertRaises(ValueError):
            card = Card("15S")

    # noinspection PyUnusedLocal
    def test_bad_card_string_suit(self):
        with self.assertRaises(ValueError):
            card = Card("2T")

    # noinspection PyUnusedLocal
    def test_bad_card_string_too_long(self):
        with self.assertRaises(ValueError):
            card = Card("2 of Spades")


if __name__ == '__main__':
    unittest.main()

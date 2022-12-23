import unittest
from src.Card.Rank import Rank


# noinspection PyPep8Naming
class testRank(unittest.TestCase):

    def setUp(self):
        self.rank_2 = Rank(2)
        self.rank_j = Rank(11)
        self.rank_q = Rank(12)
        self.rank_k = Rank(13)
        self.rank_a = Rank(14)

    def test_rank_repr(self):
        test_cases = (
            ("2", self.rank_2),
            ("J", self.rank_j),
            ("Q", self.rank_q),
            ("K", self.rank_k),
            ("A", self.rank_a)
        )

        for expected_repr, test_instance in test_cases:
            with self.subTest(f"{expected_repr} == repr({test_instance})"):
                self.assertEqual(expected_repr, repr(test_instance))

    def test_rank_str(self):
        test_cases = (
            ("2", self.rank_2),
            ("Jack", self.rank_j),
            ("Queen", self.rank_q),
            ("King", self.rank_k),
            ("Ace", self.rank_a)
        )

        for expected_repr, test_instance in test_cases:
            with self.subTest(f"{expected_repr} == str({test_instance})"):
                self.assertEqual(expected_repr, str(test_instance))

    def test_rank_gt(self):
        self.assertTrue(self.rank_a > self.rank_k)
        self.assertTrue(self.rank_k > self.rank_q)
        self.assertTrue(self.rank_q > self.rank_j)
        self.assertTrue(self.rank_j > self.rank_2)

    def test_rank_ge(self):
        self.assertTrue(self.rank_a >= self.rank_a)
        self.assertTrue(self.rank_a >= self.rank_k)
        self.assertTrue(self.rank_k >= self.rank_k)
        self.assertTrue(self.rank_k >= self.rank_q)
        self.assertTrue(self.rank_q >= self.rank_q)
        self.assertTrue(self.rank_q >= self.rank_j)
        self.assertTrue(self.rank_j >= self.rank_j)
        self.assertTrue(self.rank_j >= self.rank_2)

    def test_rank_lt(self):
        self.assertTrue(self.rank_2 < self.rank_j)
        self.assertTrue(self.rank_j < self.rank_q)
        self.assertTrue(self.rank_q < self.rank_k)
        self.assertTrue(self.rank_k < self.rank_a)

    def test_rank_le(self):
        self.assertTrue(self.rank_2 <= self.rank_2)
        self.assertTrue(self.rank_2 <= self.rank_j)
        self.assertTrue(self.rank_j <= self.rank_j)
        self.assertTrue(self.rank_j <= self.rank_q)
        self.assertTrue(self.rank_q <= self.rank_q)
        self.assertTrue(self.rank_q <= self.rank_k)
        self.assertTrue(self.rank_k <= self.rank_k)
        self.assertTrue(self.rank_k <= self.rank_a)

    def test_rank_ne(self):
        self.assertTrue(self.rank_2 != self.rank_j)
        self.assertTrue(self.rank_j != self.rank_q)
        self.assertTrue(self.rank_q != self.rank_k)
        self.assertTrue(self.rank_k != self.rank_a)

    def test_rank_eq(self):
        my_rank_2 = Rank(2)
        my_rank_j = Rank(11)
        my_rank_q = Rank(12)
        my_rank_k = Rank(13)
        my_rank_a = Rank(14)

        self.assertTrue(self.rank_2 == my_rank_2)
        self.assertTrue(self.rank_j == my_rank_j)
        self.assertTrue(self.rank_q == my_rank_q)
        self.assertTrue(self.rank_k == my_rank_k)
        self.assertTrue(self.rank_a == my_rank_a)

    # noinspection PyUnusedLocal
    def test_bad_rank_1(self):
        with self.assertRaises(ValueError):
            rank = Rank(1)

    # noinspection PyUnusedLocal
    def test_bad_rank_15(self):
        with self.assertRaises(ValueError):
            rank = Rank(15)

    # noinspection PyTypeChecker,PyUnusedLocal
    def test_bad_rank_str(self):
        with self.assertRaises(ValueError):
            rank = Rank("2")


if __name__ == '__main__':
    unittest.main()

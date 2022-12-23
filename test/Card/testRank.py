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
        test_cases = (
            (self.rank_a, self.rank_k),
            (self.rank_k, self.rank_q),
            (self.rank_q, self.rank_j),
            (self.rank_j, self.rank_2),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} > {instance_b}"):
                self.assertTrue(instance_a > instance_b)

    def test_rank_ge(self):
        test_cases = (
            (self.rank_a, self.rank_a),
            (self.rank_a, self.rank_k),
            (self.rank_k, self.rank_k),
            (self.rank_k, self.rank_q),
            (self.rank_q, self.rank_q),
            (self.rank_q, self.rank_j),
            (self.rank_j, self.rank_j),
            (self.rank_j, self.rank_2),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} >= {instance_b}"):
                self.assertTrue(instance_a >= instance_b)

    def test_rank_lt(self):
        test_cases = (
            (self.rank_2, self.rank_j),
            (self.rank_j, self.rank_q),
            (self.rank_q, self.rank_k),
            (self.rank_k, self.rank_a),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} < {instance_b}"):
                self.assertTrue(instance_a < instance_b)

    def test_rank_le(self):
        test_cases = (
            (self.rank_2, self.rank_2),
            (self.rank_2, self.rank_j),
            (self.rank_j, self.rank_j),
            (self.rank_j, self.rank_q),
            (self.rank_q, self.rank_q),
            (self.rank_q, self.rank_k),
            (self.rank_k, self.rank_k),
            (self.rank_k, self.rank_a),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} <= {instance_b}"):
                self.assertTrue(instance_a <= instance_b)

    def test_rank_ne(self):
        test_cases = (
            (self.rank_2, self.rank_j),
            (self.rank_j, self.rank_q),
            (self.rank_q, self.rank_k),
            (self.rank_k, self.rank_a),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} != {instance_b}"):
                self.assertTrue(instance_a != instance_b)

    def test_rank_eq(self):
        test_cases = (
            (self.rank_2, Rank(2)),
            (self.rank_j, Rank(11)),
            (self.rank_q, Rank(12)),
            (self.rank_k, Rank(13)),
            (self.rank_a, Rank(14)),
        )

        for instance_a, instance_b in test_cases:
            with self.subTest(f"{instance_a} == {instance_b}"):
                self.assertTrue(instance_a == instance_b)

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

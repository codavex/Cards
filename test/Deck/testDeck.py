import unittest
from Deck import Deck


class testDeck(unittest.TestCase):

    def test_deck_size_1_a(self):
        deck = Deck()
        self.assertEqual(deck.size(), 52)

    def test_deck_size_1_b(self):
        deck = Deck(1)
        self.assertEqual(deck.size(), 52)

    def test_deck_size_2(self):
        deck = Deck(2)
        self.assertEqual(deck.size(), 52*2)

    def test_deck_size_3(self):
        deck = Deck(3)
        self.assertEqual(deck.size(), 52*3)

    def test_deck_str(self):
        deck = Deck()
        spades = "2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S, 10S, JS, QS, KS, AS, "
        clubs = "2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, JC, QC, KC, AC, "
        hearts = "2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H, 10H, JH, QH, KH, AH, "
        diamonds = "2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D, 10D, JD, QD, KD, AD"
        expected = "[" + spades + clubs + hearts + diamonds + "]"

        self.assertEqual(str(deck), expected)


if __name__ == '__main__':
    unittest.main()

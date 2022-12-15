import unittest
from src.Card.Card import Card
from src.Poker.TexasHoldem.Hand import Hand
from src.Poker.Rank import Rank


class testHand(unittest.TestCase):
    def test_hand_4oak(self):
        hole = Hand()
        community = Hand()

        hole.append(Card("AS"))
        hole.append(Card("AC"))

        community.append(Card("AH"))
        community.append(Card("AD"))
        community.append(Card("2D"))

        self.assertEqual(hole.rank(community), Rank.FOUR_OAK)


if __name__ == '__main__':
    unittest.main()

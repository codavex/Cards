import src.Poker.Hand


class Hand(src.Poker.Hand.Hand):

    def rank_with_board(self, board):
        combined = src.Poker.Hand.Hand()

        for card in list(self):
            combined.append(card)
        for card in board:
            combined.append(card)

        return combined.rank()

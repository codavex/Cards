from src.Card.Card import Card
from src.Card.Rank import Rank


class BlackjackHand:
    def __init__(self):
        self._hand = []

    def draw(self, c):
        self._hand.append(c)

    def cardScore(self, c):
        rank = c.get_rank()
        if rank == 14:
            return 1
        elif rank in [11, 12, 13]:
            return 10
        else:
            return rank

    def score(self):
        score = [0]
        for c in self._hand:
            for i in range(len(score)):
                score[i] += self.cardScore(c)
            if c.get_rank() == 14:
                duplicate = score.copy()
                for i in range(len(duplicate)):
                    duplicate[i] += 10
                score += duplicate
            score = [x for x in score if x <= 21]
        return set(score)

import src.Hand.Hand


class Hand(src.Hand.Hand.Hand):
    @staticmethod
    def card_score(card):
        rank = card.get_rank()
        if rank == 14:
            return 1
        elif rank in [11, 12, 13]:
            return 10
        else:
            return rank

    def score(self):
        score = [0]
        for card in self:
            for i in range(len(score)):
                score[i] += Hand.card_score(card)
            if card.get_rank() == 14:
                duplicate = score.copy()
                for i in range(len(duplicate)):
                    duplicate[i] += 10
                score += duplicate
            score = [x for x in score if x <= 21]
        return set(score)

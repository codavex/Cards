from src.Card.Card import Card


class Hand(list):
    def size(self):
        return len(self)

    def draw(self):
        return super().pop(0)

    def build_from_str(self, hand_as_str: str) -> object:
        # to build a hand from a string depicting a hand
        # eg "[AS, AV, AH, AD, kS]"
        self.clear()
        hand_as_str = hand_as_str.removeprefix("[")
        hand_as_str = hand_as_str.removesuffix("]")
        hand_as_str = hand_as_str.replace(" ", "")
        cards = hand_as_str.split(',')
        for card in cards:
            self.append(Card(card))
        return

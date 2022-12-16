class Hand(list):
    def size(self):
        return len(self)

    def draw(self):
        return super().pop(0)

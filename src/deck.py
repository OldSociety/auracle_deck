import random

class Deck: 
    def __init__(self, cards):
        self.cards = cards #list of card instances
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self, count=1):
        return [self.cards.pop() for _ in range(min(count, len(self.cards)))]
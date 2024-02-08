import random 

class Coin:
    def __init__(self, name, color, heads_meaning, tails_meaning):
        self.name = name
        self.color = color
        self.heads_meaning = heads_meaning
        self.tails_meaning = tails_meaning

    def flip(self):
        # Simulate flipping the coin, returning 'heads' or 'tails'
        return 'heads' if random.choice([True, False]) else 'tails'

    def display_info(self, result):
        print(f"Coin Name: {self.name}")
        print(f"Color: {self.color}")
        meaning = self.heads_meaning if result == 'heads' else self.tails_meaning
        print(f"Side: {result}, Meaning: {meaning}")

import random

class Coin: 
    def __init__(self, name, color, meanings):
        self.name = name
        self.color = color
        self.meanings = meanings
        
    def flip(self):
        return 'heads' if random.choice([True, False]) else 'tails'
    
def display_info(self):
    print(f"Coin Name: {self.name}")
    print(f"Color: {self.color}")
    print(f"Meanings: {self.meanings}")
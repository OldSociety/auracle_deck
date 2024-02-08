class Card:
    def __init__(self, name, meanings, dragon):
        self.name = name
        self.meanings = meanings
        self.dragon = dragon
        
    def display_info(self):
        print(f"Card Name: {self.name}")
        print(f"Meanings: {self.meanings}")
        print(f"Associated Dragon: {self.dragon}")
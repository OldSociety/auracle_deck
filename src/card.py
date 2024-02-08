class Card:
    def __init__(self, number, name, meanings, dragon):
        self.number = number
        self.name = name
        self.meanings = meanings
        self.dragon = dragon
        
    def display_info(self):
        print(f"Number: {self.number}")
        print(f"Card Name: {self.name}")
        print(f"Meanings: {self.meanings}")
        print(f"Associated Dragon: {self.dragon}")
from card import Card
from coin import Coin
from deck import Deck


# Cards
sun_card = Card("00","The Twin Suns", {"General": "Unity, Universal harmony, Divinity"}, "All Moons")

# Larimar Cards
anchor_card = Card("01","The Anchor", {"General": "Financial success through hard work, Hope for a better future"}, "Larimar")
ship_card = Card("02","The Ship", {"General": "Journeys, exploration of the unknown, and the wisdom gained through experience."}, "Larimar")
mountains_card = Card("03","The Moutains", {"General": "Great challenges, Greater perseverance."}, "Larimar")

# Nassenti Cards
forest_card = Card("04","The Forest", {"General": "Community, strength in unity and collective growth."}, "Nassenti")
clover_card = Card("05","The Clover", {"General": "Luck, minor fortune, and the magic of serendipity in the natural world."}, "Nassenti")
shephard_card = Card("06","The Shephard", {"General": "Guidance, care for others, and the nurturing aspect of nature."}, "Nassenti")

# Oth-Orleth Cards
bonfire_card = Card("07","The Bonfire", {"General": "Represents raw energy, destruction for renewal, and the passion that drives conflict and change."}, "Oth-orleth")
rapier_card = Card("08","The Rapier", {"General": " Symbolizes direct conflict, the cut of decision, and the vitality in defense or attack."}, "Oth-orleth")
storm_card = Card("09","The Storm", {"General": "Embodies the chaos and power within upheaval"}, "Oth-orleth")

# Pan-shi Cards
weeds_card = Card("10","The Weeds", {"General": "Survival, Deceit, Theft"}, "Pan-shi")
mirror_card = Card("11","The Broken Mirror", {"General": "Deception and the shattering of illusions"}, "Pan-shi")
mouse_card = Card("12","The Mouse", {"General": "Loss, theft, and the undermining of fortunes."}, "Pan-shi")

# Sen-shi Cards
wheat_card = Card("13","The Wheat", {"General": "Generosity, Nourishment, Need for intercooperation"}, "Sen-shi")
eye_card = Card("14","The Eye", {"General": "Insight, awareness, and the windows to the soul and beyond."}, "Sen-shi")
snake_card = Card("15","The Snake", {"General": "Growth, Life, the unending cycle of rebirth"}, "Sen-shi")

# Udreth-sol Cards
dove_card = Card("16","The Dove", {"General": "Peace after conflict, Meditation, Purity, quiet power of nature"}, "Udreth-sol")
book_card = Card("17","The Book", {"General": "Knowledge, Hidden secrets, and the potential that lies in learning and discovery."}, "Udreth-sol")
coffin_card = Card("18","The Coffin", {"General": "Endings, transitions, and the deep, transformative power of death."}, "Udreth-sol")

# Zyry Cards
wine_card = Card("19","The Wine", {"General": "Celebration, indulgence, or the intoxication that can lead to loss of control. It adds an element of celebration or caution, depending on its context in a reading."}, "Zyry")
lion_card = Card("20","The Lion", {"General": "Strength, courage, and leadership, but also the danger of unchecked power. It speaks to the nobility of spirit and the risks of sovereignty."}, "Zyry")
roses_card = Card("21","The Roses", {"General": "Beauty, the flowering of love or success, but with thorns that remind of the cost of desire."}, "Zyry")

# Initialize list of cards
cards_list = [
    sun_card, anchor_card, ship_card, mountains_card,
    forest_card, clover_card, shephard_card,
    bonfire_card, rapier_card, storm_card,
    weeds_card, mirror_card, mouse_card,
    wheat_card, eye_card, snake_card,
    dove_card, book_card, coffin_card,
    wine_card, lion_card, roses_card
]

# Initialize the Deck instance with the list of cards
deck = Deck(cards_list)

# Coins
larimar_coin = Coin("Larimar", "Green", 
                    heads_meaning="Wisdom, Depth, Intuition", 
                    tails_meaning="")
nassenti_coin = Coin("Nassenti", "Blue", 
                    heads_meaning="Growth, Nature, Healing", 
                    tails_meaning="")
oth_orleth_coin = Coin("Oth-Orleth", "Red", 
                    heads_meaning="Passion, Vitality", 
                    tails_meaning="Conflict")
sen_shi_pan_shi_coin = Coin("Sen-Shi/Pan-Shi", "Dual-Colored", 
                    heads_meaning="Light, Life (Sen-Shi)", 
                    tails_meaning="Debauchery, Trickery (Pan-Shi)")
udreth_sol_coin = Coin("Udreth-sol", "Silver", 
                    heads_meaning="Intuition, Potential, Subconscious", 
                    tails_meaning="Death")
zyry_coin = Coin("Zyry", "Gold", 
                    heads_meaning="Wealth, Success, Achievement", 
                    tails_meaning="")

def main():
    # Prompt for user's question
    input("What is your question for the Auracle Deck? (press enter to continue) ")
    
    # Shuffle the deck
    deck.shuffle()

    # Draw five cards
    drawn_cards = deck.draw(5)

    # Display the results
    positions = ["The Present or General Theme", "Past Influences", "The Future", "The Reason Behind the Question", "The Potential Within the Situation"]
    for position, card in zip(positions, drawn_cards):
        print(f"{position}: {card.name} - {card.meanings['General']}")

if __name__ == "__main__":
    main()
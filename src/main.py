from card import Card
from coin import Coin


# Cards
sun_card = Card("00","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")

# Larimar Cards
sun_card = Card("01","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("02","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("03","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")

# Nassenti Cards
sun_card = Card("04","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("05","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("06","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")

# Oth-Orleth Cards
sun_card = Card("07","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("08","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("09","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")

# Pan-shi Cards
sun_card = Card("10","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("11","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("12","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")

# Sen-shi Cards
sun_card = Card("13","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("14","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("15","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")

# Udreth-sol Cards
sun_card = Card("16","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("17","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("18","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")

# Zyry Cards
sun_card = Card("19","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("20","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")
sun_card = Card("21","The Twin Suns", {"General": "Unity, Duality, Harmony"}, "All Moons")

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

the_sun_card.display_info()
result = oth_orleth_coin.flip()
print(f"The Oth-Orleth coin landed on {result}. Meaning: {oth_orleth_coin.meanings[result]}")
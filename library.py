# 1.random library
import random 
coin = random.choice(["heads", "tails"])
print(coin)

 #from keyword use to import only specific function from library
from random import choice
coin = choice(["heads", "tails"])
print(coin)

# shuffle keyword use in random.
cards = ["king", "queen", "jack"]
random.shuffle(cards)
for card in cards:
    print(card)


# 2.statistics library
import statistics

print(statistics.mean([100,90]))
print(statistics.median([100,5]))
print(statistics.harmonic_mean([100, 5]))
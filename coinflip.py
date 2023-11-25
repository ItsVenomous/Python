import random

flips = 1
heads = 0
tails = 0

while flips <= 50:
    coin = random.randint(1, 2)
    flips += 1
    if coin == 1:
        print("Heads")
        heads += 1
    elif coin == 2:
        print("Tails")
        tails += 1

print("You got " + str(heads) + " heads and " + str(tails) + " tails!")

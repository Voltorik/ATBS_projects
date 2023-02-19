import random

numberOfStreaks = 0
CoinFlip = []
streak = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        CoinFlip.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(CoinFlip)):
        if i == 0:
            pass
        elif CoinFlip[i] == CoinFlip[i-1]:
            streak += 1

        if streak == 6:
            numberOfStreaks += 1

    CoinFlip = []

print('Chance of streak: %s%%' % (numberOfStreaks / 100))



# DPChange(money, Coins): Utilize dynamic programming to find the smallest amount of coins required to reach total.
# Input: int(money), list of int(Coins)
# Output: The lowest amount of coins required to reach money


import math

def DPChange(money, Coins):
    MinNumCoins = {0:0}
    for m in range(1,money+1):
        MinNumCoins[m] = math.inf
        for i in range(0,len(Coins)):
            # print(Coins[i])
            if m >= Coins[i]:
                # print(True)
                # print("Coin:",Coins[i], "m:", m)
                # print(MinNumCoins[m - Coins[i]] + 1)
                # print(MinNumCoins[m])
                if MinNumCoins[m - Coins[i]] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - Coins[i]] +1
    return MinNumCoins

print(DPChange(40, [50,25,20,10,5,1]))

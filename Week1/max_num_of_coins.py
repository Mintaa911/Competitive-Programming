def maxCoins(piles):
    piles.sort()
    steps = 1
    l,r = 0,int(len(piles)-1)
    maxCoins = 0
    
    while steps <= len(piles)/3:
        subPiles = []
        for i in range(3):
            if i % 2 == 0:
                subPiles.append(piles[r])
                r -= 1
            else:
                subPiles.append(piles[l])
                l += 1
        steps += 1
        maxCoins += subPiles[2]
    
    return maxCoins
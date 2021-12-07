import time
import re
import math
import sys
from collections import Counter


def fuelCount(base, pos, crabs=1):
    d = abs(base - pos)
    fc = int((d * (d + 1)) / 2)
    fc *= crabs
    return fc


def doIt(filename: str) -> None:
    with open(filename) as f:

        allCrabs = Counter(map(int, re.findall(r'\d+', f.readline())))
        minF = 0
        minLvl = 5
        maxLvl = max(allCrabs)
        for c in allCrabs:
            minF += fuelCount(minLvl, c, allCrabs[c])
        for l in range(maxLvl):
            fCost = 0
            for c in allCrabs:
                fCost += fuelCount(l, c, allCrabs[c])
                if fCost > minF:
                    break
            if fCost < minF:
                minF = fCost
        print(minF)


startTime = time.time()
doIt("day07/training.txt")
doIt("day07/input.txt")
endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")

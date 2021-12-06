import time
import re
import math


class fish:
    timer = 0

    def __init__(self, tmr=8) -> None:
        self.timer = tmr

    def cd(self) -> int:
        ret = 0
        self.timer -= 1
        if self.timer == -1:
            ret = 1
            self.timer = 6
        return ret

# This won't work for 256


def doPartOne():
    fsh = []
    fsh.append(fish(3))
    fsh.append(fish(4))
    fsh.append(fish(3))
    fsh.append(fish(1))
    fsh.append(fish(2))
    for i in range(18):
        numApp = 0
        for l in fsh:
            if l.cd():
                numApp += 1
        for j in range(numApp):
            fsh.append(fish())
    print(len(fsh))


def numSpawn(totFish, days):
    for i in range(days):
        n = totFish[0]
        for i in range(8):
            totFish[i] = totFish[i+1]
        totFish[6] += n
        totFish[8] = n
    return totFish


startTime = time.time()
with open("day06/input.txt") as f:

    #doPartOne()
    totFish = [0] * 9
    for l in list(map(int, re.findall(r'\d+', f.readline()))):
        totFish[l] += 1
    totFish = numSpawn(totFish, 256)
    print(sum(totFish))


endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")

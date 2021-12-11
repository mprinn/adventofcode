import time
import re
import math
import sys
from collections import Counter

def getNeighbours(x, y, maxX, maxY):
    ret = []
    if x > 0:
        ret.append([x - 1, y])
    if x < maxX - 1:
        ret.append([x + 1, y])
    if y > 0:
        ret.append([x, y - 1])
    if y < maxY - 1:
        ret.append([x, y + 1])
    if x > 0 and y > 0:
        ret.append([x - 1, y - 1])
    if x < maxX - 1 and y < maxY - 1:
        ret.append([x + 1, y + 1])
    if x > 0 and y < maxY - 1:
        ret.append([x - 1, y + 1])
    if x < maxX - 1 and y > 0:
        ret.append([x + 1, y - 1])
    return ret


def flash(octopii: list, octoFlash, i, j, maxX, maxY):
    if octopii[i][j] == 10 and octoFlash[i][j] == 0:
        octoFlash[i][j] = 1
        n = sorted(getNeighbours(i, j, maxX, maxY))
        
        for i, j in n:
            if octopii[i][j] < 10:
                octopii[i][j] +=1
                if octopii[i][j] == 10 :
                    flash(octopii, octoFlash, i, j, maxX, maxY)

def clearOctopii(octopii, alreadyFlashed, maxX, maxY):
    for i in range(maxX):
        for j in range(maxY):
            if octopii[i][j] >= 10:
                octopii[i][j] = 0
            alreadyFlashed[i][j] = 0

def step(octopii: list):
    maxX = len(octopii)
    maxY = len(octopii[0])
    alreadyFlashed = [[0 for y in range(maxY)] for x in range(maxX)]
    flashes = 0
    for i in range(maxX):
        for j in range(maxY):
            octopii[i][j] +=1
    for i in range(maxX):
        for j in range(maxY):
            flash(octopii, alreadyFlashed, i, j, maxX, maxY)
    for x in alreadyFlashed:
        flashes += sum(a for a in x)
    clearOctopii(octopii, alreadyFlashed, maxX, maxY)
    return flashes


def doIt(filename: str) -> None:

    octopii = []
    totF = 0
    with open(filename) as f:
        for l in f:
            octopii.append([int(x) for x in l.strip()])
    #part 1
    #for i in range(100):
    #    totF += step(octopii)
    #print(totF)

    #part 2
    steps = 1
    while 100 != step(octopii):
        steps+=1
    print(steps)

startTime = time.time()
#doIt("day11/check.txt")
doIt("day11/training.txt")
doIt("day11/input.txt")
endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")
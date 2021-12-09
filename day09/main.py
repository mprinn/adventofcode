import time
import re
import math
import sys
from collections import Counter


def getNeighbours(points, x, y, maxX, maxY):
    ret = []
    if x > 0:
        ret.append(points[x - 1][y])
    if x < maxX - 1:
        ret.append(points[x + 1][y])
    if y > 0:
        ret.append(points[x][y - 1])
    if y < maxY - 1:
        ret.append(points[x][y + 1])
    return ret


def findMins(levels):
    maxX = len(levels)
    maxY = len(levels[0])
    numLow = 0
    totDng = 0
    mins = []

    for i in range(maxX):
        for j in range(maxY):
            n = getNeighbours(levels, i, j, maxX, maxY)
            point = levels[i][j]
            if all(x > point for x in n):
                numLow += 1
                totDng += point
                mins.append([i, j])

    totDng += numLow
    return totDng, mins


#this is apparently called floodfilling
# https://en.wikipedia.org/wiki/Flood_fill


def getBasinsize(levels, min):
    i = min[0]
    j = min[1]
    if 0 <= i < len(levels) and 0 <= j < len(levels[i]) and levels[i][j] != 9:
        levels[i][j] = 9
        return (
            1
            + getBasinsize(levels, [i - 1, j])
            + getBasinsize(levels, [i + 1, j])
            + getBasinsize(levels, [i, j - 1])
            + getBasinsize(levels, [i, j + 1])
        )
    return 0


def findBasins(levels, mins):
    basins = []
    for min in mins:
        bSize = getBasinsize(levels, min)
        basins.append(bSize)
    basins.sort(reverse=True)
    print(
        f"basins 0 {basins[0]}, basin 1 {basins[1]}, basin 2 {basins[2]}, total = {basins[0] * basins[1] * basins[2]} ")


def doIt(filename: str) -> None:
    levels = []
    with open(filename) as f:
        for l in f:
            levels.append([int(x) for x in l.strip()])

    dngMins, mins = findMins(levels)
    print(dngMins)
    print(findBasins(levels, mins))


startTime = time.time()
#doIt("day09/check.txt")
doIt("day09/training.txt")
doIt("day09/input.txt")
endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")

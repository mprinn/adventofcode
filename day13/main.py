import time
import re
import math
import sys
import collections


def fold(page, h: str, num: int):
    loop = 0
    if 'x' in h:
        for i in range(len(page)):
            loop = 0
            for y in range(num-1, -1, -1):
                loop += 1
                if page[i][num + loop] == '#':
                    page[i][y] = '#'
            page[i] = page[i][:-num]
    else:
        for i in range(num-1, -1, -1):
            loop += 1
            for y in range(len(page[0])):
                if page[num + loop][y] == '#':
                    page[i][y] = '#'
        for i in range(num, len(page)):
            page.pop()

    return page


def countDots(page):
    numD = 0
    for i in range(len(page)):
        for j in range(len(page[0])):
            if page[i][j] == '#':
                numD += 1
    return numD


def doIt(filename: str) -> None:

    points = []
    folds = []

    with open(filename) as f:
        p1 = True
        for l in f:
            if l.isspace():
                p1 = False
                continue
            if p1 is True:
                points.append(list(map(int, l.strip().split(","))))
            else:
                folds.append(l.strip())

    maxX = 0
    maxY = 0
    for p in points:
        if p[0] > maxX:
            maxX = p[0] + 1
        if p[1] > maxY:
            maxY = p[1] + 1
    page = [['.' for y in range(1311)] for x in range(1311)]
    for p in points:
        page[p[1]][p[0]] = '#'

    for f in folds:
        dir, num = f.split('=')
        page = fold(page, dir, int(num))

    letters = [[['.' for y in range(4)] for x in range(6)] for j in range(8)]
    for i in range(8):
        for j in range(6):
            letters[i][j] = page[j][(i*5):(i*5)+4]


startTime = time.time()
#doIt("day13/check.txt")
#doIt("day13/training.txt")
doIt("day13/input.txt")
endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")

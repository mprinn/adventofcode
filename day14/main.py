import time
import re
import math
import sys
from collections import Counter


def getPairs(poly):
    outP = []
    for i in range(len(poly) - 1):
        outP.append(poly[i:i+2])
    return outP


def expand(poly, insertions):
    outP = poly[0]
    pairs = getPairs(poly)
    for p in pairs:
        outP = outP + insertions[p][1:]
    return outP


def part1(poly, insertions, chars):
    for i in range(10):
        poly = expand(poly, insertions)
        counter = Counter(poly)
        min = sys.maxsize
        max = 0
    for c in chars:
        if counter[c] > max:
            max = counter[c]
        if counter[c] < min:
            min = counter[c]
    print(max - min)


def part2(poly, insertions, chars):
    pairs = {}


def doIt(filename: str) -> None:

    with open(filename) as f:
        poly = f.readline().strip()
        chars = []
        f.readline()
        insertions = {}
        for l in f:
            p = l.strip().split(" -> ")
            insertions[p[0]] = p[0][0] + p[1] + p[0][1]
            chars.append(p[1])

        part1(poly, insertions, chars)
        part2(poly, insertions, chars)


startTime = time.perf_counter()
#doIt("day14/check.txt")
doIt("day14/training.txt")
#doIt("day14/input.txt")
endTime = time.perf_counter()
print(f"Process finished --- {endTime - startTime} seconds ---")

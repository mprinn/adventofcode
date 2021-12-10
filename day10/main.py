import time
import re
import math
import sys
from collections import Counter
import threading


def calcpoint(line, result, index):
    openers = ['(', '{', '<', '[']
    closers = {'(': ')', '{': '}', '<': '>', '[': ']'}
    part1Points = {')': 3,
                   ']': 57,
                   '}': 1197,
                   '>': 25137}

    part2Points = {')': 1,
                   ']': 2,
                   '}': 3,
                   '>': 4}

    nextClose = []
    score = 0
    invalid = False
    for x in line.strip():
        if x in openers:
            nextClose.append(closers[x])
        else:
            if x != nextClose[-1]:
                score += part1Points[x]
                invalid = True
                break
            else:
                nextClose.pop()

    if invalid is False:
        for n in reversed(nextClose):
            score *= 5
            score += part2Points[n]
    result[index] = [invalid, score]


def doIt(filename: str) -> None:
    totP1 = 0
    totP2 = []
    threads = list()
    results = [None] * 110

    with open(filename) as f:
        i = 0

        for l in f:
            x = threading.Thread(target=calcpoint,
                                 args=(l, results, i), daemon=True)
            threads.append(x)
            x.start()
            i += 1

        for t in threads:
            t.join()

    for r in results:
        if r is None:
            break
        inv, point = r[0], r[1]
        if inv is False:
            totP2.append(point)
        else:
            totP1 += point

    totP2.sort()
    middleIndex = int((len(totP2) - 1)/2)
    print(totP2[middleIndex])
    print(totP1)


startTime = time.time()
# doIt("day10/check.txt")
doIt("day10/training.txt")
doIt("day10/input.txt")
endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")

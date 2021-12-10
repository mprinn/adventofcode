import time
import re
import math
import sys
from collections import Counter


def doIt(filename: str) -> None:
    operations = []
    ops = {'(': 0, ')': 0, '{': 0, '}': 0, '<': 0, '>': 0, '[': 0, ']': 0, }
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
    totbadP = 0
    totP2 = []

    with open(filename) as f:
        for l in f:
            nextClose = []
            totCloseP = 0
            invalid = False
            operations.append([x for x in l.strip()])
            for x in l.strip():
                ops[x] += 1
                if x in openers:
                    nextClose.append(closers[x])
                else:
                    if x != nextClose[-1]:
                        totbadP += part1Points[x]
                        invalid = True
                        break
                    else:
                        nextClose.pop()

            if invalid is False:
                for n in reversed(nextClose):
                    totCloseP *= 5
                    totCloseP += part2Points[n]
                totP2.append(totCloseP)

    totP2.sort()

    middleIndex = int((len(totP2) - 1)/2)
    print(totP2[middleIndex])


startTime = time.time()
#doIt("day10/check.txt")
doIt("day10/training.txt")
doIt("day10/input.txt")
endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")

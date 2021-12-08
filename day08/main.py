import time
import re
import math
import sys
from collections import Counter


def countUniques(parts):
    ret = 0
    for p in parts[1].split():
        l = len(p)
        if l == 2 or l == 3 or l == 4 or l == 7:
            ret += 1

    return ret


def getVal(parts):

    signals = ["?"] * 10
    inputs = parts[0].split()
    g069 = [x for x in inputs if len(x) == 6]
    g235 = [x for x in inputs if len(x) == 5]

    signals[1] = sorted(next(x for x in inputs if len(x) == 2))
    signals[7] = sorted(next(x for x in inputs if len(x) == 3))
    signals[4] = sorted(next(x for x in inputs if len(x) == 4))
    signals[8] = sorted(next(x for x in inputs if len(x) == 7))
    signals[6] = sorted(
        next(x for x in inputs if len(x) == 6 and not (set(signals[1]).issubset(x))))

    for p in g069:
        if sorted(p) == signals[6]:
            g069.remove(p)

    for p in g235:
        if set(signals[1]).issubset(sorted(p)):
            signals[3] = sorted(p)
            g235.remove(p)

    for p in g069:
        if set(signals[4]).issubset(sorted(p)):
            signals[9] = sorted(p)
            g069.remove(p)
    signals[0] = sorted(g069[0])

    for p in g235:
        a = set(signals[9])
        b = set(p)
        c = a - b
        if len(c) == 1:
            signals[5] = sorted(p)
            g235.remove(p)
    signals[2] = sorted(g235[0])

    val = []
    for o in parts[1].split():
        val += [signals.index(x) for x in signals if x == sorted(o)]
    return getTotVal(val)


def getTotVal(individNums):
    out = 0
    for i in range(len(individNums)):
        out += individNums[i] * 10 ** (len(individNums) - i - 1)
    return out


def doIt(filename: str) -> None:
    with open(filename) as f:
        uniques = 0
        tot = 0
        for line in f:
            parts = line.strip().split(" | ")
            uniques += countUniques(parts)
            ival = getVal(parts)
            tot += ival
    print(uniques)
    print(tot)


startTime = time.time()
#doIt("day08/check.txt")
#doIt("day08/training.txt")
doIt("day08/input.txt")
endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")

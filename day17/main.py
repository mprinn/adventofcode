import time
import re
import math
import sys
import collections


def within(point, area):
    if (point[0] >= area[0][0] and point[0] <= area[0][1] and
            point[1] <= area[1][0] and point[1] >= area[1][1]):
        return True
    return False


def missedArea(point, area):
    if point[1] < area[1][1] or point[0] > area[0][1]:
        return True
    return False


def step(point, area, xvel, yvel):
    x = point[0] + xvel
    y = point[1] + yvel
    if xvel > 0:
        xvel -= 1
    elif xvel < 0:
        xvel += 1
    yvel -= 1
    return [x, y], xvel, yvel


def tests(area):
    print(within([25, -8], area))
    print(within([19, -8], area))
    print(missedArea([31, -8], area))
    print(missedArea([25, -19], area))

    print(missedArea([20, -8], area))
    print(missedArea([25, -2], area))


def getMaxY(point, area, xvel, yvel):
    maxY = 0
    while missedArea(point, area) is False:
        point, xvel, yvel = step(point, area, xvel, yvel)
        if point[1] > maxY:
            maxY = point[1]
        if within(point, area):
            return maxY
    return 0


def doIt(filename: str) -> None:

    points = []
    folds = []

    with open(filename) as f:
        l = f.readline()
        x, y = l.split(',')
        x = list(map(int, re.findall(r'[-\d]+', x)))
        y = list(map(int, re.findall(r'[-\d]+', y)))
        x.sort()
        y.sort(reverse=True)

        area = []
        area.append(x)
        area.append(y)

        maxY = 0
        numv = 0
        for xvel in range(-67, 200):
            for yvel in range(-67, 200):
                point = [0, 0]
                tmp = getMaxY(point, area, xvel, yvel)
                if tmp > maxY:
                    maxY = tmp
                if tmp != 0:
                    numv += 1
        print(maxY)
        print(numv)


startTime = time.time()
#doIt("day17/check.txt")
#doIt("day17/training.txt")
doIt("day17/input.txt")
endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")

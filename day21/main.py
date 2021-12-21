import time
import re


class detDie:
    roll = 1


def rollDet() -> int:
    ret = detDie.roll
    detDie.roll += 1
    if detDie.roll == 101:
        detDie.roll = 1
    return ret


def getDroll(det: bool = True) -> int:
    ret = 0
    ret += rollDet()
    ret += rollDet()
    ret += rollDet()
    return ret


def doIt(filename: str) -> None:

    detDie.roll = 1
    score = [0] * 2
    pos = [0] * 2

    with open(filename) as f:
        pos[0] = int(f.readline().split(': ')[1].strip())
        pos[1] = int(f.readline().split(': ')[1].strip())

    player = 0
    numRolls = 0
    dres = 0
    while (score[0] < 1000 and score[1] < 1000):
        dres = getDroll() % 10
        pos[player] = (pos[player] + dres)
        if pos[player] > 10:
            pos[player] = pos[player] % 10
        score[player] += pos[player]
        player += 1
        if player > 1:
            player = 0
        numRolls += 3
    print(dres, numRolls)
    print(numRolls * score[player])


startTime = time.time()
# doIt("day21/check.txt")
doIt("day21/training.txt")
doIt("day21/input.txt")
endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")

import re

class board():
    entries = list()
    marked = list()
    totMarked = 0
    unmarkedSum = 0
    xMarked = [0] * 5
    yMarked = [0] * 5
    haswon = 0

    def __init__(self):
        self.entries = [[0 for y in range(5)] for x in range(5)]
        self.marked = [[0 for y in range(5)] for x in range(5)]

    def populateBoard(self, vals):
        for x in range(5):
            for y in range(5):
                self.entries[x][y] = vals[x][y]
                self.unmarkedSum += vals[x][y]
        
    def checkVal(self, val):
        for x in range(5):
            for y in range(5):
                if self.entries[x][y] == val:
                    self.marked[x][y] = 1
                    self.totMarked += 1
                    self.unmarkedSum -= self.entries[x][y]
                    break
    
    def checkWinner(self):
        ret = 0
        if self.totMarked >= 5:
            for x in range(5):
                ysum = 0
                if sum(self.marked[x]) == 5 or sum([sub[x] for sub in self.marked]) == 5:
                    ret +=1
                    self.haswon = 1
                    break
        return ret

    def calcUnmarked(self):
        return self.unmarkedSum    


def readBoard(lines: list)->list:
    vals = [[0 for y in range(5)] for x in range(5)]
    for x in range(5):
        vals[x] = list(map(int, re.findall(r'\d+',lines[x])))
    return vals

import time
start_time = time.time()
with open("day04/input.txt") as f:
    lines = [line.rstrip() for line in f]

    bingos = list(map(int, re.findall(r'\d+',lines[0])))
    boards = []
    maxbrd = int((len(lines) - 1) / 6)
    for i in range(maxbrd):
        boards.append(board())
        boards[i].populateBoard(readBoard(lines[2+(i*6):7+(i*6)]))

    for i in range(5):
        chkVal = bingos.pop(0)
        for brd in range(maxbrd):
            boards[brd].checkVal(chkVal)

    for i in range(len(bingos)):
        chkVal = bingos.pop(0)
        for brd in range(maxbrd):
            if (boards[brd].haswon == 0):
                boards[brd].checkVal(chkVal)         
                if boards[brd].checkWinner():
                    val = boards[brd].calcUnmarked()
                    print(f"board {brd} winner, chkVal = {chkVal}, val = {val}, score = {val*chkVal}")

print("Process finished --- %s seconds ---" % (time.time() - start_time))
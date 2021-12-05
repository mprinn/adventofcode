import time
import re

class vents:
    points = []
    pointsCrossed = 0
    linesDrawn = 0
    def __init__(self) -> None:
        self.points = [[0 for y in range(1000)] for x in range(1000)]
    

    def populateLine(self, x1, y1, x2, y2):
        
        if x1 == x2:
            y = min(y1, y2)
            for i in range(abs(y2 - y1) + 1):
                self.points[y + i][x1] += 1
                if (self.points[y + i][x1] == 2):
                    self.pointsCrossed +=1
        elif y1 == y2:
            x = min(x1, x2)
            for i in range(abs(x2 - x1) + 1):
                self.points[y1][x + i] += 1
                if (self.points[y1][x + i] == 2):
                    self.pointsCrossed +=1
        else:
            x_step, dx = (1, 1) if x1 < x2 else (-1, -1)
            y_step, dy = (1, 1) if y1 < y2 else (-1, -1)
            xs = list(range(x1, x2 + dx, x_step))
            ys = list(range(y1, y2 + dy, y_step))
            for p in  list(zip(xs, ys)):
                self.points[p[1]][p[0]] +=1
                if (self.points[p[1]][p[0]] == 2):
                    self.pointsCrossed +=1

    def getPointsCrossed(self):
        return self.pointsCrossed

startTime = time.time()
with open("day05/input.txt") as f:
    v = vents()
    for l in  f.readlines():
        point = list(map(int, re.findall(r'\d+',l)))
        v.populateLine(point[0], point[1], point[2], point[3])
    print(v.getPointsCrossed())

endTime = time.time()
print(f"Process finished --- {endTime - startTime} seconds ---")
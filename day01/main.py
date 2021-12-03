import itertools as it


def window(lst, n):
    prevSum = 0
    numgt = -1
    for i in range(len(lst)-n+1):
        batch = lst[i:i+n]
        tot = sum(batch)
        if (tot > prevSum):
            numgt+=1
        prevSum = tot
    return  numgt

with open("input.txt") as f:
    lines = f.readlines()
    nums = list(map(int, lines))
    print(window(nums, 3))

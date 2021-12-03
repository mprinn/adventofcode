def getNums(entries: list, pos: int, val: int) -> list:
    retList = []
    for e in entries:
        if (e[pos] == val):
            retList.append(e)
    return retList

def calcMaxBits(lines: list) -> str :
    setBit = ""
    val = len(lines[0]) - 1
    sums = [0] * val
    for line in lines:
        bits = list(line.rstrip())
        index = 0
        for bit in bits:
            sums[index] += int(bit)
            index+=1

    for sum in sums:
        if sum >= len(lines) / 2:
            setBit += "1"
        else:
            setBit += "0"
    return setBit

def createInverseString(inString: str) -> str:
    outStr = ""
    for c in inString:
        if c == "0":
            outStr += "1"
        else:
            outStr += "0"
    return outStr

with open("input.txt") as f:
    lines = f.readlines()
    numBits = len(lines[0]) - 1
    gamma = calcMaxBits(lines)

    # get oxygen
    vals = lines
    o2 = gamma
    for i in range(numBits):
        vals = getNums(vals, i, o2[i])
        if (len(vals) == 1):
            break
        o2 = calcMaxBits(vals)
    o2 = vals[0]

    # get co2 scrubber
    vals = lines
    co2 = createInverseString(gamma)
    for i in range(numBits):
        vals = getNums(vals, i, co2[i])
        if (len(vals) == 1):
            break
        co2 = calcMaxBits(vals)
        co2 = createInverseString(co2)
    co2 = vals[0]


    print (int(o2,2))
    print (int(co2,2))
    print (int(o2,2) * int(co2,2))

    print(len(lines))

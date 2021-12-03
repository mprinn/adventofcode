
with open("input.txt") as f:
    lines = f.readlines()
    horizontal = 0
    subDepth = 0
    aim = 0
    for line in lines:
        cmd, depth = line.split(' ')
        if ("forward" == cmd):
            horizontal += int(depth)
            subDepth += aim * int(depth)
        elif ("down" == cmd):
            #subDepth += int(depth)
            aim += int(depth)
        else:
            #subDepth -= int(depth)
            aim -= int(depth)
    print(horizontal, subDepth)
    print(horizontal*subDepth)

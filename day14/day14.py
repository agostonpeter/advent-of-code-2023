def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    parsedData = []
    for x, line in enumerate(lines):
        line = line.strip()
        parsedData.append(line)

    return parsedData

file_path = "./day14/day14.txt"
# file_path = "./day14/day14_test.txt"

parsedInput = read_input(file_path)

def getTransposed(matrix):
    rotatedMatrix = ([[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))])
    return [''.join(row) for row in rotatedMatrix]
def printPattern(pattern):
    print("---------")
    for line in pattern:
        print(line)
    print("---------")
def getRotated(input):
    # clockwise
    return [''.join(row)[::-1] for row in zip(*input)]

def tiltPlatform(platform, orientation): # 0: north, 1: east
    preRotation = (orientation + 4 - 1) % 4
    # print(f"preRotation: {preRotation}")
    rotatedPlatform = platform
    for i in range(preRotation):
        rotatedPlatform = getRotated(rotatedPlatform)
    # print("rotated platform:")
    # printPattern(rotatedPlatform)
    newPlatform = []
    for line in rotatedPlatform:
        newLine = ""
        for linePart in line.split('#'):
            rocks = linePart.count('O')
            newLine += 'O' * rocks
            newLine += '.' * (len(linePart)-rocks)
            newLine += '#'
        newPlatform.append(newLine[:-1])
    # print("new platf")
    # printPattern(newPlatform)
    # print(f"afterRotation: {4-preRotation}")

    for i in range(4-preRotation):
        newPlatform = getRotated(newPlatform)
    # printPattern(newPlatform)
    return newPlatform

def getLoad(platform):
    transposedPlatform = getTransposed(platform)
    result = 0
    for line in transposedPlatform:
        rocks = [index+1 for index, char in enumerate(line[::-1]) if char == 'O']
        result += sum(rocks)
    return result

print("============== PART ONE ==============")
partOnePlatform = tiltPlatform(parsedInput, 0)
print(getLoad(partOnePlatform))

print("============== PART TWO ==============")



platform = parsedInput
# printPattern(platform)


seenPlatforms = []
cycle = 0
goal = 1000000000
# goal = 50
repetitionFound = False
while cycle < goal:
    # print(cycle)
    for tilt in range(4):
        # printPattern(platform)
        # print("tilt!")
        platform = tiltPlatform(platform, tilt)
        # printPattern(platform)
    # print(f"cycle: {cycle}, load: {getLoad(platform)}")
    if platform in seenPlatforms and not repetitionFound:
        before = seenPlatforms.index(platform)
        print(f"I've been here! Now: {cycle} before: {before}")
        # printPattern(platform)
        cycle = goal - ((goal - before) % (cycle - before))
        print(f"cycle set to {cycle}")
        cycle += 1
        repetitionFound = True
    else:
        seenPlatforms.append(platform)
        cycle += 1

print(getLoad(platform))
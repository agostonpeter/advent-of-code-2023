def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    parsedData = []
    pattern = []
    for x, line in enumerate(lines):
        line = line.strip()
        if line == "":
            parsedData.append(pattern)
            pattern = []
            continue
        pattern.append(line)
    parsedData.append(pattern)

    return parsedData


file_path = "./day13/day13.txt"
# file_path = "./day13/day13_test.txt"

patterns = read_input(file_path)

def getRotated(matrix):
    rotatedMatrix = ([[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))])
    return [''.join(row) for row in rotatedMatrix]
def isMirrored(top, bottom):
    for i, line in enumerate(top):
        if line != bottom[::-1][i]:
            return False
    return True
def splitForMirroring(pattern, mirrorLine):
    top = pattern[:mirrorLine]
    bottom = pattern[mirrorLine:]
    lengthDiff = len(top)-len(bottom)
    if lengthDiff > 0:
        return top[lengthDiff:], bottom
    elif lengthDiff < 0:
        return top, bottom[:lengthDiff]
    else:
        return top, bottom
def printPattern(pattern):
    print("---------")
    for line in pattern:
        print(line)
    print("---------")
    
# print(patterns)
# print(getRotated(patterns[0]))
def findPatternResult(pattern, originalResult = 0):
    # printPattern(pattern)
    for i, row in enumerate(pattern):
        if i==0:
            continue
        top, bottom = splitForMirroring(pattern, i)
        if isMirrored(top, bottom) and originalResult != 100 * i:
            return 100 * i

    rotatedPattern = getRotated(pattern)
    for i, column in enumerate(rotatedPattern):
        if i==0:
            continue
        top, bottom = splitForMirroring(rotatedPattern, i)
        if isMirrored(top, bottom) and originalResult != i:
            return  i
    
print("============== PART ONE ==============")
partOneResult = 0
# print(len(patterns)
for pattern in patterns:
    partOneResult += findPatternResult(pattern)

print(partOneResult)

print("============== PART TWO ==============")
def swapSmudge(pattern, i, j):
    if pattern[i][j] == "#":
        pattern[i] = pattern[i][:j] + "." + pattern[i][j+1:]
    else:
        pattern[i] = pattern[i][:j] + "#" + pattern[i][j+1:]
    return pattern

partTwoResult = 0
for pattern in patterns:
    originalResult = findPatternResult(pattern)
    foundNewResult = False
    for i, row in enumerate(pattern):
        for j, column in enumerate(row):
            swapSmudge(pattern, i, j)
            modifiedResult = findPatternResult(pattern, originalResult)
            if modifiedResult is not None:
                # print(f"Old result: {originalResult}, new result: {modifiedResult}")
                partTwoResult += modifiedResult
                foundNewResult = True
                break
            else:
                swapSmudge(pattern, i, j)
        if foundNewResult:
            break
    if not foundNewResult:
        print("NO new result :( ")
print(partTwoResult)
            

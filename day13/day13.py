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

# print(patterns)
# print(getRotated(patterns[0]))

print("============== PART ONE ==============")
partOneResult = 0
# print(len(patterns)
for pattern in patterns:
    # print(partOneResult)
    mirrorLineFound = False
    for i, row in enumerate(pattern):
        if i==0:
            continue
        top, bottom = splitForMirroring(pattern, i)
        if isMirrored(top, bottom):
            mirrorLineFound = True
            partOneResult += 100 * i
            break
    if mirrorLineFound:
        continue

    rotatedPattern = getRotated(pattern)
    for i, column in enumerate(rotatedPattern):
        if i==0:
            continue
        top, bottom = splitForMirroring(rotatedPattern, i)
        if isMirrored(top, bottom):
            partOneResult += i
            mirrorLineFound = True
            break
    if not mirrorLineFound:
        print("NOT FOUND!")

print(partOneResult)
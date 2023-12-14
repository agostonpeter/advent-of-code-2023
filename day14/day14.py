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

def getRotated(matrix):
    rotatedMatrix = ([[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))])
    return [''.join(row) for row in rotatedMatrix]
def printPattern(pattern):
    print("---------")
    for line in pattern:
        print(line)
    print("---------")

print("============== PART ONE ==============")
partOneResult = 0

platform = getRotated(parsedInput)

for line in platform:
    load = len(line)
    for linePart in line.split('#'):
        rocks = linePart.count('O')
        nextLoad = load - len(linePart) - 1
        for i in range(rocks):
            partOneResult += load
            load -=1
        load = nextLoad

print(partOneResult)
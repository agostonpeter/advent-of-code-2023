def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    parsedData = []
    maxX = -1
    maxY = -1
    for x, line in enumerate(lines):
        line = line.strip()
        for y, char in enumerate(line):
            if char == '#':
                parsedData.append([x,y])
                if x > maxX:
                    maxX = x
                if y > maxY:
                    maxY = y
    return parsedData, (maxX, maxY)

file_path = './day11/day11.txt'
# file_path = './day11/day11_test.txt'

galaxies, maximums = read_input(file_path)

# print(galaxies)
# print(maximums)

print("============== PART ONE ==============")
partOneResult = 0
xAll = set(range(maximums[0]+1))
yAll = set(range(maximums[1]+1))
xCoordinates = set([galaxy[0] for galaxy in galaxies])
yCoordinates = set([galaxy[1] for galaxy in galaxies])
emptyXs = xAll - xCoordinates
emptyYs = yAll - yCoordinates
# print(emptyXs)
# print(emptyYs)
def countSmallerIntegers(inputSet, n):
    return sum(1 for num in inputSet if num < n)
extendedGalaxies= []
for galaxy in galaxies:
    xExtend = countSmallerIntegers(emptyXs, galaxy[0])
    yExtend = countSmallerIntegers(emptyYs, galaxy[1])
    newGalaxy = (galaxy[0]+xExtend, galaxy[1]+yExtend)
    extendedGalaxies.append(newGalaxy)
# print(extendedGalaxies)
numberOfGalaxies = len(extendedGalaxies)
def distanceOfGalaxies(A, B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1])
for i in range(numberOfGalaxies):
    for j in range(i+1, numberOfGalaxies):
        partOneResult += distanceOfGalaxies(extendedGalaxies[i], extendedGalaxies[j])
print(partOneResult)
print("============== PART TWO ==============")
partTwoResult = 0
veryExtendedGalaxies = []
expansion = 1000000 - 1
for galaxy in galaxies:
    xExtend = countSmallerIntegers(emptyXs, galaxy[0]) * expansion
    yExtend = countSmallerIntegers(emptyYs, galaxy[1]) * expansion
    newGalaxy = (galaxy[0]+xExtend, galaxy[1]+yExtend)
    veryExtendedGalaxies.append(newGalaxy)
numberOfGalaxies = len(veryExtendedGalaxies)
for i in range(numberOfGalaxies):
    for j in range(i+1, numberOfGalaxies):
        partTwoResult += distanceOfGalaxies(veryExtendedGalaxies[i], veryExtendedGalaxies[j])
print(partTwoResult)
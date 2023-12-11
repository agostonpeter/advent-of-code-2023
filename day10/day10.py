#  y->
# x
# |
# v
# 
# (x,y)
# (i,j)

#          (-1,  0)
# ( 0, -1) ( x,  y) ( 0,  1)
#          ( 1,  0)

import sys

NextSteps = {
    "|": ((-1,  0), ( 1,  0)),
    "-": (( 0, -1), ( 0,  1)),
    "L": ((-1,  0), ( 0,  1)),
    "J": ((-1,  0), ( 0, -1)),
    "7": (( 0, -1), ( 1,  0)),
    "F": (( 0,  1), ( 1,  0)),
    "S": ((-1,  0), ( 1,  0), ( 0, -1), ( 0,  1)),
    ".": []
}

class Pipe:
    def __init__(self, inputData, location):
        self.pipe = inputData
        self.location = location
        self.isPartOfTheLargeContinuosLoopOfTheMysteriousAnimal = False
        self.distanceFromStart = -1
        self.isInside = False
    
    def nextLocation(self, previousLocation):
        if self.pipe == "S" or self.pipe == ".":
            raise Exception("Invalid pipe in next location method.")
        previousStep = (
            previousLocation[0]-self.location[0], 
            previousLocation[1]-self.location[1]
        )
        if previousStep not in NextSteps[self.pipe]:
            raise Exception("Something not good with previous step :thinking:")

        if NextSteps[self.pipe][0] == previousStep:
            nextStep = NextSteps[self.pipe][1]
        elif NextSteps[self.pipe][1] == previousStep:
            nextStep = NextSteps[self.pipe][0]
        nextLocation = (
            self.location[0]+nextStep[0],
            self.location[1]+nextStep[1]
        )
        return nextLocation
    def __str__(self):
        return self.pipe

    def printOnlyIfPartOfTheLargeContinuosLoopOfTheMysteriousAnimal(self):
        if self.isPartOfTheLargeContinuosLoopOfTheMysteriousAnimal:
            return self.pipe
        elif self.isInside:
            return 'X'
        else:
            return ' '


def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    parsedData = []
    startLocation = (0,0)
    for x, line in enumerate(lines):
        line = line.strip()
        pipeLine = []
        for y, char in enumerate(line):
            pipeLine.append(Pipe(char,(x,y)))
            if char == 'S':
                startLocation = (x,y)
        parsedData.append(pipeLine)
    return parsedData, startLocation

file_path = './day10/day10.txt'
# file_path = './day10/day10_test5.txt'

pipeMap, startLocation = read_input(file_path)

print(startLocation)

def getPipe(location):
    return pipeMap[location[0]][location[1]]

def getNextLocation(location, step):
    return (location[0] + step[0], location[1] + step[1])

def inverseStep(step):
    return (-step[0], -step[1])

def printPipeMap(onlyLoop = False, filePar = sys.stdout):
    for pipeLine in pipeMap:
        for pipe in pipeLine:
            if onlyLoop:
                print(pipe.printOnlyIfPartOfTheLargeContinuosLoopOfTheMysteriousAnimal(), end="", file=filePar)
            else:
                print(pipe, end="", file=filePar)
        print(file=filePar)

print("============== PART ONE ==============")
partOneResult = 0
loopPipes = []

# handle start position
nextLocation = None
distance = 0
currentLocation = startLocation
previousLocation = startLocation

while distance < 1000000:
    currentPipe = getPipe(currentLocation)
    assert isinstance(currentPipe, Pipe)

    # handle current
    currentPipe.isPartOfTheLargeContinuosLoopOfTheMysteriousAnimal = True
    currentPipe.distanceFromStart = distance
    loopPipes.append(currentPipe)

    # find next location
    if distance == 0:
        for nextStep in NextSteps['S']:
            nextLocation = getNextLocation(startLocation, nextStep)
            if inverseStep(nextStep) in NextSteps[getPipe(nextLocation).pipe]:
                break
    else:
        nextLocation = currentPipe.nextLocation(previousLocation)

    # get ready for next loop
    distance += 1
    previousLocation = currentLocation
    currentLocation = nextLocation

    if currentLocation == startLocation:
        break

with open('day10/output.txt', 'w') as file:   
    printPipeMap(True, file)
print(int(distance/2))

print("============== PART TWO ==============")
# change start pipe

startLocationNextSteps = []
for nextStep in NextSteps['S']:
    nextLocation = getNextLocation(startLocation, nextStep)
    if inverseStep(nextStep) in NextSteps[getPipe(nextLocation).pipe]:
        startLocationNextSteps.append(nextStep)
print(startLocationNextSteps)
for key in NextSteps:
    if all(s in NextSteps[key] for s in startLocationNextSteps):
        print(key)
        getPipe(startLocation).pipe = key
        break

partTwoResult = 0
for x, pipeLine in enumerate(pipeMap):
    inside = False
    loopFrom = 0 # 0: noloop, 1: top, -1: bottom
    for y, pipe in enumerate(pipeLine):
        assert isinstance(pipe, Pipe)
        if pipe.isPartOfTheLargeContinuosLoopOfTheMysteriousAnimal:
            if not loopFrom:
                if pipe.pipe == "|":
                    inside = not inside
                elif pipe.pipe == "L":
                    loopFrom = 1
                elif pipe.pipe == "F":
                    loopFrom = -1
                else:
                    raise Exception("Not |, L, or F")
            elif loopFrom == 1:
                if pipe.pipe == "-":
                    pass
                elif pipe.pipe == "J":
                    loopFrom = 0
                elif pipe.pipe == "7":
                    inside = not inside
                    loopFrom = 0
                else:
                    raise Exception("loopFrom 1 and Not -, J, or 7")
            elif loopFrom == -1:
                if pipe.pipe == "-":
                    pass
                elif pipe.pipe == "J":
                    inside = not inside
                    loopFrom = 0
                elif pipe.pipe == "7":
                    loopFrom = 0
                else:
                    raise Exception("loopFrom -1 and Not -, J, or 7")
            else:
                raise Exception("loopFrom not -1, 0, or 1")
        elif inside:
            partTwoResult+=1
            pipe.isInside = True
with open('day10/output.txt', 'w') as file:   
    printPipeMap(True, file)
print(partTwoResult)
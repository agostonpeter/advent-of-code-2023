NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Tile():
    maxX = 0
    maxY = 0

    def __init__(self, inputChar) -> None:
        self.char = inputChar
        self.energized = False
        self.beamHistory = [
            False,
            False,
            False,
            False
        ]
        if self.char == '.':
            self.outBeamHeadings = [
                [NORTH],
                [EAST],
                [SOUTH],
                [WEST]
            ]
        elif self.char == '|':
            self.outBeamHeadings = [
                [NORTH],
                [NORTH, SOUTH],
                [SOUTH],
                [NORTH, SOUTH]
            ]
        elif self.char == '-':
            self.outBeamHeadings = [
                [EAST, WEST],
                [EAST],
                [EAST, WEST],
                [WEST]
            ]
        elif self.char == '/':
            self.outBeamHeadings = [
                [EAST],
                [NORTH],
                [WEST],
                [SOUTH]
            ]
        elif self.char == '\\':
            self.outBeamHeadings = [
                [WEST],
                [SOUTH],
                [EAST],
                [NORTH]
            ]
        else:
            raise ValueError(f"Incorrect inputChar for Tile: {inputChar}")
    def __str__(self):
        if hasattr(self, "char") and self.energized:
            return self.char
        else:
            return '_'
    
    def hitWithBeam(self, inBeam):
        assert isinstance(inBeam, Beam)
        self.energized = True
        if not self.beamHistory[inBeam.heading]:
            self.beamHistory[inBeam.heading] = True
            beams = []
            for beamHeading in self.outBeamHeadings[inBeam.heading]:
                newBeam = Beam(getNextLocation(inBeam.entering, beamHeading), beamHeading)
                if 0 <= newBeam.entering[0] <= Tile.maxX and 0 <= newBeam.entering[1] <= Tile.maxY:
                    beams.append(newBeam)
            return beams
        else:
            return []

class Beam():
    def __init__(self, entering=[0,0], heading=EAST) -> None:
        self.entering = entering
        self.heading = heading
    def __str__(self) -> str:
        return f"{self.entering}, heading: {self.heading}"

def getNextLocation(location, heading):
    if heading == NORTH:
        return [location[0] - 1, location[1]]
    elif heading == EAST:
        return [location[0], location[1] + 1]
    elif heading == SOUTH:
        return [location[0] + 1, location[1]]
    elif heading == WEST:
        return [location[0], location[1] - 1]

def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    parsedData = []
    for x, line in enumerate(lines):
        line = line.strip()
        lineData = []
        for char in line:
            lineData.append(Tile(char))
        parsedData.append(lineData)
    Tile.maxX = len(parsedData) -1
    Tile.maxY = len(parsedData[0]) -1
    return parsedData

file_path = "./day16/day16.txt"
# file_path = "./day16/day16_test.txt"
def printMap(mirrorMap):
    for line in mirrorMap:
        for tile in line:
            print(tile, end='')
        print()
def printBeams(beams):
    for b, beam in enumerate(beams):
        print(f"{b}: {beam}, ", end='')
    print()
mirrorMap = read_input(file_path)

# printMap(mirrorMap)

print("============== PART ONE ==============")
beams = [Beam()]
# printBeams(beams)
while len(beams)>0:
    beam = beams.pop(0)
    x = beam.entering[0]
    y = beam.entering[1]
    tile = mirrorMap[x][y]
    assert isinstance(tile, Tile)
    beams += tile.hitWithBeam(beam)
    # printMap(mirrorMap)
    # printBeams(beams)
    # input()

partOneResult = 0
for line in mirrorMap:
    for tile in line:
        if tile.energized:
            partOneResult+=1
print(partOneResult)


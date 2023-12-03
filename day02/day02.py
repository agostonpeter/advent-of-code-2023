def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    parsed_data = []
    for line in lines:
        parts = line.strip().split(':')
        grabs = parts[1].strip().split(';')
        gameResult = []
        for grab in grabs:
            colorResults = grab.strip().split(',')
            grabResult = [0,0,0]
            for colorResult in colorResults:
                parsedColorResult = colorResult.strip().split(' ')
                if parsedColorResult[1] == "red":
                    grabResult[0] = int(parsedColorResult[0])
                elif parsedColorResult[1] == "green":
                    grabResult[1] = int(parsedColorResult[0])
                elif parsedColorResult[1] == "blue":
                    grabResult[2] = int(parsedColorResult[0])
            gameResult.append(grabResult)
        gameNumber = int(parts[0].split(' ')[1])
        parsed_data.append((gameNumber, gameResult))

    return parsed_data

file_path = './day02/day02.txt'
parsedInput = read_input(file_path)

print(parsedInput)

print("============== PART ONE ==============")
MAX_CUBES = (12, 13, 14)
partOneResult = 0
for game in parsedInput:
    goodGame = True
    for grab in game[1]:
        for i, color in enumerate(grab):
            if color > MAX_CUBES[i]:
                goodGame = False
                break
        if not goodGame:
            break
    if goodGame:
        partOneResult += game[0]
print(partOneResult)

print("============== PART TWO ==============")

partTwoResult = 0
for game in parsedInput:
    minCubes = [0,0,0]
    for grab in game[1]:
        for i, color in enumerate(grab):
            if color != 0 and color > minCubes[i]:
                minCubes[i] = color
    gameResult = minCubes[0] * minCubes[1] * minCubes[2]
    partTwoResult += gameResult
print(partTwoResult)
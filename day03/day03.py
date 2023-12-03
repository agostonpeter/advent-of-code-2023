import re


def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    lines = [line[:-1] for line in lines]
    parsed_data = []
    chars = []
    for line in lines:
        matches = [
            (int(match.group()), match.start()) for match in re.finditer(r"\d+", line)
        ]
        parsed_data.append(matches)
        for char in line:
            if not char.isdigit() and char != "." and char not in chars:
                chars.append(char)
    return lines, parsed_data, chars


file_path = "./day03/day03.txt"
rawInput, parsedInput, chars = read_input(file_path)
maxI = len(rawInput) - 1
maxJ = len(rawInput[0]) - 1
print("============== PART ONE ==============")
partOneResult = 0
possibleGears = {}
for i, linePartNumbers in enumerate(parsedInput):
    for partNumber in linePartNumbers:
        isPartNumber = False
        numberLength = len(str(partNumber[0]))
        numberJ = partNumber[1]
        for tmpI in range(i - 1, i + 1 + 1):
            for j in range(numberJ - 1, numberJ + numberLength + 1):
                if tmpI < 0 or tmpI > maxI:
                    break
                if j < 0 or j > maxJ:
                    continue

                # part One
                if rawInput[tmpI][j] in chars:
                    isPartNumber = True

                # part Two
                if rawInput[tmpI][j] == "*":
                    if (tmpI, j) in possibleGears:
                        possibleGears[(tmpI, j)].append(partNumber[0])
                    else:
                        possibleGears[(tmpI, j)] = [partNumber[0]]

        if isPartNumber:
            partOneResult += partNumber[0]

print(partOneResult)
print("============== PART TWO ==============")
partTwoResult = 0
for gear in possibleGears.values():
    if len(gear) == 2:
        partTwoResult += gear[0] * gear[1]

print(partTwoResult)

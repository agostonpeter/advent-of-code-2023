def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    for x, line in enumerate(lines):
        return line.strip().split(',')


file_path = "./day15/day15.txt"
# file_path = "./day15/day15_test.txt"

parsedInput = read_input(file_path)
# print(parsedInput)
print("============== PART ONE ==============")
def HASH(inputString, currentValue):
    for char in inputString:
        currentValue += ord(char)
        currentValue *= 17
        currentValue %= 256
    return currentValue


partOneResult = 0
for step in parsedInput:
    hashValue = HASH(step, 0)
    # print(f"{step} - {hashValue}")
    partOneResult += hashValue
print(partOneResult)
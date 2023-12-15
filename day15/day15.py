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
def HASH(inputString):
    currentValue = 0
    for char in inputString:
        currentValue += ord(char)
        currentValue *= 17
        currentValue %= 256
    return currentValue


partOneResult = 0
for step in parsedInput:
    hashValue = HASH(step)
    # print(f"{step} - {hashValue}")
    partOneResult += hashValue
print(partOneResult)

print("============== PART TWO ==============")
HASHMAP = [[[],[]] for _ in range(256)]
LABEL = 0
FOCAL = 1

def printHashMap():
    print("--->")
    for b, box in enumerate(HASHMAP):
        if len(box[LABEL]):
            print(f"Box {b}: ", end="")
            for i in range(len(box[LABEL])):
                print(f"[{box[LABEL][i]} {box[FOCAL][i]}]", end="")
            print()
    print("<---")
    

            

# printHashMap()
for step in parsedInput:
    if step.count('-'):
        isAdd = False
        label = step[:-1]
    else:
        isAdd = True
        splitStep = step.split('=')
        label = splitStep[0]
        focalLength = int(splitStep[1])
    boxNumber = HASH(label)
    box = HASHMAP[boxNumber]
    if isAdd:
        if label in box[LABEL]:
            index = box[LABEL].index(label)
            box[FOCAL][index] = focalLength
        else:
            box[LABEL].append(label)
            box[FOCAL].append(focalLength)
    else:
        if label in box[LABEL]:
            index = box[LABEL].index(label)
            box[LABEL].pop(index)
            box[FOCAL].pop(index)
    # printHashMap()

partTwoResult = 0
for b, box in enumerate(HASHMAP):
    for f, focalLength in enumerate(box[FOCAL]):
        focusingPower = (b+1)*(f+1)*focalLength
        # print(f"{box[LABEL][f]}= {focusingPower}")
        partTwoResult += focusingPower
print(partTwoResult)


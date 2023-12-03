f = open("./day01/day01.txt", "r")
result = 0

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]
for line in f:
    lineResult = ""
    lowestDigitIndex = 0
    lowChar = ""
    for i, char in enumerate(line):
        if char.isnumeric():
            lowestDigitIndex = i
            lowChar = str(char)
            break
    
    for i, number in enumerate(numbers):
        numberIndex = line.find(number)
        if numberIndex != -1 and numberIndex < lowestDigitIndex:
            lowChar = str(i+1)
            lowestDigitIndex = numberIndex
    

    highestDigitIndex = 0
    highChar = ""
    for i, char in enumerate(line):
        if char.isnumeric():
            highestDigitIndex = i
            highChar = str(char)
    
    for i, number in enumerate(numbers):
        print("searchign for " + number)
        numberIndex = -1
        line2 = line
        while line2.find(number) != -1:
            localIndex = line2.find(number)
            line2 = line2[localIndex+1:]
            numberIndex += localIndex+1
            print(line2)
            print(numberIndex)
        if numberIndex != -1 and numberIndex > highestDigitIndex:
            highChar = str(i+1)
            highestDigitIndex = numberIndex
    lineResult = int(lowChar + highChar)
    result += lineResult

    print(line)
    print(lineResult)
    print("======")

print(result)
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    parsed_data = []
    for line in lines:
        parts = line.strip().split(':')
        gameNumber = int(list(filter(None, parts[0].strip().split(' ')))[1])
        sets = parts[1].strip().split('|')
        winningNumbers = [int(set) for set in list(filter(None, sets[0].strip().split(' ')))]
        myNumbers = [int(set) for set in list(filter(None, sets[1].strip().split(' ')))]
        
        parsed_data.append((gameNumber, winningNumbers, myNumbers))

    return parsed_data

file_path = './day04/day04.txt'
# file_path = './day04/day04_test.txt'
parsedInput = read_input(file_path)

#print(parsedInput)

print("============== PART ONE ==============")
partOneResult = 0
cardPoints = []
for card in parsedInput:
    cardResult = 0
    numberOfWinningNumbers = 0
    for myNumber in card[2]:
        for winningNumber in card[1]:
            if myNumber == winningNumber:
                numberOfWinningNumbers += 1
                if cardResult == 0:
                    cardResult = 1
                else:
                    cardResult *= 2
    partOneResult += cardResult 
    cardPoints.append((numberOfWinningNumbers, cardResult))
print(partOneResult)

print("============== PART TWO ==============")
partTwoResult = 0
numberOfCards = [1] * len(cardPoints)
for i, cardPoint in enumerate(cardPoints):
    # print("======= " + str(i+1))
    partTwoResult += numberOfCards[i]
    for j in range(cardPoint[0]):
        # print("increasing number of " + str(i+1+j+1) + " by " + str(numberOfCards[i]))
        numberOfCards[i+1+j] += numberOfCards[i]
    # print(numberOfCards)
    
print(partTwoResult)
# print(numberOfCards)

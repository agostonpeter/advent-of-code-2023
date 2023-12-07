from enum import IntEnum

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    parsed_data = []
    for line in lines:
        parsed_data.append(line.strip().split(' '))
    return parsed_data

file_path = './day07/day07.txt'
# file_path = './day07/day07_test.txt'
parsedData = read_input(file_path)
# print(parsedData)
print("============== PART ONE ==============")
cardChars = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

class HandType(IntEnum):
    BIG_POKER = 6
    SMALL_POKER = 5
    FULL_HOUSE = 4
    DRILL = 3
    DOUBLE_PAIR = 2
    PAIR = 1
    HIGH_CARD = 0

class Hand:
    def __init__(self, inputData, isJoker):
        self.cards = []
        self.cardsStr = inputData[0]
        cardsSummed = {}
        for card in inputData[0]:
            if card.isdigit():
                cardValue = int(card)
            elif isJoker and card == 'J':
                cardValue = 1
            elif card in cardChars:
                cardValue = cardChars[card]
            else:
                raise ValueError("Invalid card value.")

            self.cards.append(cardValue)
            if cardValue in cardsSummed:
                cardsSummed[cardValue] += 1
            elif cardValue != 1:
                cardsSummed[cardValue] = 1
        cardsSummedValues = sorted(cardsSummed.values(), reverse=True)
        jokers = 0
        if isJoker:
            jokers = inputData[0].count('J')
        
        if jokers == 5 or cardsSummedValues[0] + jokers == 5:
            self.type = HandType.BIG_POKER
        elif cardsSummedValues[0] + jokers == 4:
            self.type = HandType.SMALL_POKER
        elif cardsSummedValues[0] + jokers == 3 and cardsSummedValues[1] == 2:
            self.type = HandType.FULL_HOUSE
        elif cardsSummedValues[0] + jokers == 3:
            self.type = HandType.DRILL
        elif cardsSummedValues[0] + jokers == 2 and cardsSummedValues[1] == 2:
            self.type = HandType.DOUBLE_PAIR
        elif cardsSummedValues[0] + jokers == 2:
            self.type = HandType.PAIR
        else:
            self.type = HandType.HIGH_CARD
        
        self.value = self.type
        for card in self.cards:
            self.value = (self.value << 4) + card
        self.bid = int(inputData[1])
    
    def __str__(self):
        return f"Cards: {self.cardsStr}, type: {self.type.name}, value: {self.value}, bid: {self.bid}"

hands = []
handsWithJokers = []
for data in parsedData:
    hand = Hand(data, False)
    handWithJokers = Hand(data, True)
    hands.append(hand)
    handsWithJokers.append(handWithJokers)
    # print(hand)

sortedHands = sorted(hands, key=lambda h: h.value)
sortedHandsWithJokers = sorted(handsWithJokers, key=lambda h: h.value)
numberOfHands = len(sortedHands)

partOneResult = 0
for i, hand in enumerate(sortedHands):
    # print(i)
    # print(hand)
    partOneResult += (i+1) * hand.bid
print(partOneResult)
print("============== PART TWO ==============")
partTwoResult = 0
for i, hand in enumerate(sortedHandsWithJokers):
    # print(i)
    # print(hand)
    partTwoResult += (i+1) * hand.bid
print(partTwoResult)
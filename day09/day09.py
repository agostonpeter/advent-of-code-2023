def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    parsedData = []
    for line in lines:
        numbers = line.strip().split(' ')
        data = [int(number) for number in numbers]
        parsedData.append(data)
    return parsedData

file_path = './day09/day09.txt'
file_path = './day09/day09_test.txt'
measurements = read_input(file_path)
# print(measurements)

print("============== PART ONE ==============")
partOneResult = 0
for measurement in measurements:
    sequence = measurement
    lastReadings = [sequence[-1]]
    while any(sequence):
        # print(sequence)
        newSequence = [] 
        for i, reading in enumerate(sequence[:-1]):
            newSequence.append(sequence[i+1]-reading)
        sequence = newSequence
        lastReadings.append(sequence[-1])
    prediction = sum(lastReadings)
    partOneResult += prediction
    # print(prediction)
print(partOneResult)


print("============== PART TWO ==============")
partTwoResult = 0
for measurement in measurements:
    sequence = measurement[::-1]
    lastReadings = [sequence[-1]]
    while any(sequence):
        newSequence = [] 
        for i, reading in enumerate(sequence[:-1]):
            newSequence.append(reading-sequence[i+1])
        sequence = newSequence
        lastReadings.append(sequence[-1])
    prediction = 0
    for reading in lastReadings[::-1]:
        prediction = reading - prediction
    partTwoResult += prediction
print(partTwoResult)
# v = s/t

# s = v * t
# T
# a = 1 m/s^2
# 0 <= t <= T
# s = a * t * (T-t)

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    parsed_data = []
    times = list(filter(None, lines[0].strip().split(' ')[1:]))
    distances = list(filter(None, lines[1].strip().split(' ')[1:]))
    times = [int(time) for time in times]
    distances = [int(distance) for distance in distances]
    return times, distances

file_path = './day06/day06.txt'
# file_path = './day06/day06_test.txt'
times, distances = read_input(file_path)

print(times)
print(distances)

print("============== PART ONE ==============")
partOneResult = 1
for i, time in enumerate(times):
    distance = distances[i]
    numberOfWaysOfWinning = 0
    for t in range(0, time):
        if t*(time-t) > distance:
            numberOfWaysOfWinning+=1
    print(str(i) + ": " + str(numberOfWaysOfWinning))
    partOneResult *= numberOfWaysOfWinning
print(partOneResult)

print("============== PART TWO ==============")
time2 = ""
for time in times:
    time2 += str(time)
time2 = int(time2)

distance2 = ""
for distance in distances:
    distance2 += str(distance)
distance2 = int(distance2)

partTwoResult = 0
print(time2)
print(distance2)
for t in range(0, time2):
    if t*(time2-t) > distance2:
        partTwoResult+=1
print(partTwoResult)

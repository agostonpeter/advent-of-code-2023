import sys
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    parsed_data = []
    mapData = []
    for line in lines:
        parts = line.strip().split(' ')
        if parts[0] == "":
            continue
        if parts[0] == "seeds:":
            parsed_data.append([int(part) for part in parts[1:]])
            continue
        if parts[1] == "map:":
            if len(mapData) > 0:
                parsed_data.append(mapData)
                mapData = []
            continue
        else:
            mapData.append([int(part) for part in parts])

    
    parsed_data.append(mapData)
    return parsed_data[0], parsed_data[1:]

file_path = './day05/day05.txt'
# file_path = './day05/day05_test.txt'
seeds, maps = read_input(file_path)

# print(seeds)
# print(maps)

print("============== PART ONE ==============")
locations = []
for seed in seeds:
    nextSource = seed
    for map in maps:
        for rangeData in map:
            if nextSource in range(rangeData[1], rangeData[1]+rangeData[2]):
                nextSource = rangeData[0] + nextSource - rangeData[1]
                break
    # print("seed " + str(seed) + " location is: " + str(nextSource))
    locations.append(nextSource)

print(min(locations))

print("============== PART TWO ==============")




def mergeRanges(rangeA, rangeB):
    startA, finishA, valuesA = rangeA
    startB, finishB, valueB = rangeB

    # Check if rangeA and rangeB intersect
    if startA <= finishB and finishA >= startB:
        # Calculate the intersection
        intersectionStart = max(startA, startB)
        intersectionFinish = min(finishA, finishB)
        # Use all values of rangeA and the value of rangeB
        mergedValues = valuesA + [valueB]
        # Create the new range
        mergedRange = [intersectionStart, intersectionFinish, mergedValues]

        if startA < intersectionStart:
            nonOverlappingBefore = [startA, intersectionStart - 1, valuesA]
        else:
            nonOverlappingBefore = []


        # Calculate the non-overlapping parts in rangeA
        if finishA > intersectionFinish:
            nonOverlappingAfter = [intersectionFinish + 1, finishA, valuesA]
        else:
            nonOverlappingAfter = []

        # Return the merged range and non-overlapping parts in rangeA
        return nonOverlappingBefore, mergedRange, nonOverlappingAfter
    else:
        return None, None, None
layers = []
for mapData in maps:
    layer = []
    for rangeData in mapData:
        layer.append([rangeData[1], rangeData[1]+rangeData[2], rangeData[0]-rangeData[1]])
    layers.append(layer)
# print(layers)
ranges = []
for s, seed in enumerate(seeds):
    if s%2 == 1:
        continue
    range = [seed, seed + seeds[s+1], []]
    ranges.append(range)
# print(ranges)
#ranges = [[55, 68, []], [79, 93, []]]
# layers = [[[98, 100, -48], [50, 98, 2]], [[15, 52, -15], [52, 54, -15], [0, 15, 39]], [[53, 61, -4], [11, 53, -11], [0, 7, 42], [7, 11, 50]]]

for l, layer in enumerate(layers):
    newRanges = []
    i=0
    while i< len(ranges):
        for layerRange in layer:
            found = False
            before, merged, after = mergeRanges(ranges[i], layerRange)
            if before:
                ranges += [before]
            if after:
                ranges += [after]
            if merged:
                newRanges += [merged]
                found = True
                break
        if not found:
            newRanges.append(ranges[i])
        i+=1

        #print(newRanges)
    #print(newRanges)
    for rangeData in newRanges:
        if len(rangeData[2]) == l:
            rangeData[2] += [0]
        rangeData[0] += rangeData[2][-1]
        rangeData[1] += rangeData[2][-1]
    #print(newRanges)
    ranges = newRanges
    print(str(l) + "-----")

closestSeed = sys.maxsize
for rangeData in ranges:
    if rangeData[0] < closestSeed:
        closestSeed = rangeData[0]

print(closestSeed)

# FAILED ATTEMPTS speedn't
# theMap = {}
# for map in (reversed(maps)):
#     print(map)
#     for rangeData in map:

#         for source in range(rangeData[1], rangeData[1]+rangeData[2]):
#             destination = rangeData[0] + source - rangeData[1]
#             if destination in theMap:
#                 theMap[source] = theMap.pop(destination)
#             else:
#                 theMap[source] = destination
# print(theMap)

# locations = []
# for seed in seeds:
#     locations.append(theMap[seed])
#     print(str(seed) + " to " + str(theMap[seed]))
# print(min(locations))

# locations = []
# for i, seed in enumerate(seeds):
#     if i%2 == 1:
#         continue
#     for j, multiSeed in enumerate(range(seed, seed + seeds[i+1])):
#         nextSource = multiSeed
#         for map in maps:
#             for rangeData in map:
#                 if nextSource in range(rangeData[1], rangeData[1]+rangeData[2]):
#                     nextSource = rangeData[0] + nextSource - rangeData[1]
#                     break
#         if j%1000 == 0:
#             print(float(j)/float(seeds[i+1]))
#         locations.append(nextSource)



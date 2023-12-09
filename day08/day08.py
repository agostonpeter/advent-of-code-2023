import math
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    nodes = {}
    instructions = lines[0].strip()
    for line in lines[2:]:
        data = line.strip().split('=')
        key = data[0].strip()
        values = data[1].strip()[1:-1].split(',')
        values = (values[0].strip(), values[1].strip())
        nodes[key]=values
    return nodes, instructions

file_path = './day08/day08.txt'
# file_path = './day08/day08_test2.txt'
nodes, instructions = read_input(file_path)
# print(instructions)
# print(nodes)
print("============== PART ONE ==============")

nextNode = 'AAA'
finishNode = 'ZZZ'
numberOfInstructions = len(instructions)
i = 0
while nextNode != finishNode and i<100000:
    nextInstruction = instructions[i%numberOfInstructions]
    if nextInstruction == 'L':
        nextNode = nodes[nextNode][0]
    elif nextInstruction == 'R':
        nextNode = nodes[nextNode][1]
    else:
        raise ValueError("Invalid instruction value. Only L or R allowed.")  
    i+=1
print(i)
print("============== PART TWO ==============")
nextNodes = []
finishNodes = []
for node in nodes:
    if node[2] == 'A':
        nextNodes.append(node)
    elif node[2] == 'Z':
        finishNodes.append(node)
numberOfInstructions = len(instructions)
nodeFinishes = []
for nextNode in nextNodes:
    i = 0
    while nextNode not in finishNodes and i<100000:
        nextInstruction = instructions[i%numberOfInstructions]
        if nextInstruction == 'L':
            nextNode = nodes[nextNode][0]
        elif nextInstruction == 'R':
            nextNode = nodes[nextNode][1]
        else:
            raise ValueError("Invalid instruction value. Only L or R allowed.")  
        i+=1
    # print(i)
    nodeFinishes.append(i)
# print(nodeFinishes)
print(math.lcm(*nodeFinishes))
# allFinished = False
# numberOfInstructions = len(instructions)
# i = 0
# while not allFinished and i<10000000:
#     nextInstruction = instructions[i%numberOfInstructions]
#     newNextNodes = []
#     for node in nextNodes:
#         if nextInstruction == 'L':
#             newNextNode = nodes[node][0]
#         elif nextInstruction == 'R':
#             newNextNode = nodes[node][1]
#         else:
#             raise ValueError("Invalid instruction value. Only L or R allowed.")
#         newNextNodes.append(newNextNode)
#     # print(newNextNodes)
#     finishedNodeCount = 0
#     for node in newNextNodes:
#         if node in finishNodes:
#             finishedNodeCount += 1
#     if finishedNodeCount == len(newNextNodes):
#         allFinished = True
#     nextNodes = newNextNodes
#     i+=1
# print(i)
# -----------------------
#   Advent of Code 2022
#   Day 5 Part 2
#   Author: James Hess
# -----------------------

beforeBreak = True
inputStacks = []
inputMoves = []
stacks = []
moves = []
output = ""

with open("Day5Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        if line.strip():
            if beforeBreak == True:
                inputStacks.append(line.replace("\n", ""))
            elif beforeBreak == False:
                inputMoves.append(line.strip())
        else:
            beforeBreak = False

# identify number of stacks
stackCount = int(inputStacks[-1].strip()[-1])

# initialize the stacks lists
for x in range(0, stackCount):
    stacks.append([])

# parse each row of the stacks input into the stacks lists, from bottom to top
for row in range(len(inputStacks) - 1, 0, -1):
    for column in range(0, stackCount):
        if inputStacks[row - 1][column * 4 + 1].strip():
            stacks[column].append(inputStacks[row - 1][column * 4 + 1])

# parse each move into moves list
for move in inputMoves:
    tempMove = [int(x) for x in move.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(",")]
    moves.append(tempMove)

# execute moves
for move in moves:
    for step in range(move[0],0,-1):
        tempItem = stacks[move[1] - 1][-step]  # identify the item that will be moved
        stacks[move[1]-1].pop(-step) # remove the item
        stacks[move[2]-1].append(tempItem) # add the item

# create output
for stack in stacks:
    output += stack[-1]
print(output)
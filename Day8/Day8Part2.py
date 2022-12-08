# -----------------------
#   Advent of Code 2022
#   Day 8 Part 2
#   Author: James Hess
# -----------------------

heights = []
scores = []

# create an array from the input file
with open("Day8Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        temp = []
        for item in line.strip():
            temp.append(item)
        heights.append(temp)

# initialize the visibility array
for row in heights:
    temp = []
    for item in row:
        temp.append(0)
    scores.append(temp)

# calculate scenic scores
for row in range(1,len(heights)-1):
    for column in range(1, len(heights[0])-1):
        leftTrees, rightTrees, upTrees, downTrees, totalScore = 0, 0, 0, 0, 0
        # calculate leftTree score
        for leftTree in range(column - 1, -1, -1):
            leftTrees += 1
            if heights[row][leftTree] >= heights[row][column]:
                break
        # calculate rightTree score
        for rightTree in range(column+1,len(heights[0])):
            rightTrees += 1
            if heights[row][rightTree] >= heights[row][column]:
                break
        # calculate upTree score
        for upTree in range(row-1,-1,-1):
            upTrees += 1
            if heights[upTree][column] >= heights[row][column]:
                break
        # calculate downTree score
        for downTree in range(row+1,len(heights)):
            downTrees += 1
            if heights[downTree][column] >= heights[row][column]:
                break
        # calculate and store totalscore
        totalScore = leftTrees * rightTrees * upTrees * downTrees
        scores[row][column] = totalScore

maxScore = 0
for row in scores:
    for item in row:
        if item > maxScore:
            maxScore = item
print(maxScore)
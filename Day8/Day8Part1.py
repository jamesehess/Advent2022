# -----------------------
#   Advent of Code 2022
#   Day 8 Part 1
#   Author: James Hess
# -----------------------

heights = []
visibility = []

# create an array from the input file
with open("Day8Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        temp = []
        for item in line.strip():
            temp.append(item)
        heights.append(temp)

# initialize the visibility array
for rowIndex, row in enumerate(heights):
    temp = []
    for itemIndex, item in enumerate(row):
        # edge rows are automatically True
        # top/bottom rows
        if rowIndex == 0 or rowIndex == len(heights)-1:
            temp.append(True)
        # left/right columns
        elif itemIndex == 0 or itemIndex == len(heights[0])-1:
            temp.append(True)
        else:
            temp.append(False)
    visibility.append(temp)

# test visibility of remaining tress
for row in range(1,len(heights)-1):
    for column in range(1, len(heights[0])-1):
        # test left visibility
        visible = True
        for leftTree in range(column-1,-1,-1):
            if heights[row][leftTree] >= heights[row][column]:
                visible = False
        if visible == True:
            visibility[row][column] = True
        # test right visibility
        visible = True
        for rightTree in range(column+1,len(heights[0])):
            if heights[row][rightTree] >= heights[row][column]:
                visible = False
        if visible == True:
            visibility[row][column] = True
        # test up visibility
        visible = True
        for upTree in range(row-1,-1,-1):
            if heights[upTree][column] >= heights[row][column]:
                visible = False
        if visible == True:
            visibility[row][column] = True
        # test down visibility
        visible = True
        for downTree in range(row+1,len(heights)):
            if heights[downTree][column] >= heights[row][column]:
                visible = False
        if visible == True:
            visibility[row][column] = True

# count number of visible trees
visibleCount = 0
for row in visibility:
    for item in row:
        if item == True:
            visibleCount +=1
print(visibleCount)
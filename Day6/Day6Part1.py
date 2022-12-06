# -----------------------
#   Advent of Code 2022
#   Day 6 Part 1
#   Author: James Hess
# -----------------------

input = ""
curIndex = 0
duplicates = True

with open("Day6Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        input = line.strip()

#input[index-4:index]
for index in range(4,len(input)+1):
    if duplicates == False:
        break
    curIndex = index
    subString = input[index-4:index]
    duplicates = False
    for char in subString:
        count = subString.count(char)
        if count > 1:
            duplicates = True

print(curIndex)
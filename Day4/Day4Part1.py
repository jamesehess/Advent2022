# -----------------------
#   Advent of Code 2022
#   Day 4 Part 1
#   Author: James Hess
# -----------------------

input = []
pairs = []
count = 0

with open("Day4Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        input.append(line.strip().split(","))

for pair in input:
    temp = []
    for set in pair:
        tempStr = set.split("-")
        tempInt = []
        # need to convert from string to integer for later comparison
        for item in tempStr:
            tempInt.append(int(item))
        temp.append(tempInt)
    pairs.append(temp)

# compare each pair
for pair in pairs:
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        count += 1
    elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        count += 1

print(count)
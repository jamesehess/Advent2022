# -----------------------
#   Advent of Code 2022
#   Day 3 Part 2
#   Author: James Hess
# -----------------------

input = []
commonItems = []
priorities = []

with open("Day3Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        input.append(line.strip())

groupCount = int(len(input)/3)

# identify common item in a group
for group in range(1,groupCount+1):
    ruck1 = input[(group-1)*3]
    ruck2 = input[(group-1)*3+1]
    ruck3 = input[(group-1)*3+2]
    for item in ruck1:
        found = ruck2.find(item)
        if found != -1:
            found = ruck3.find(item)
            if found != -1:
                commonItems.append(item)
                break

# identify priority of the common items
for item in commonItems:
    if item.isupper():
        priority = ord(item) - 38
    else:
        priority = ord(item) - 96
    priorities.append(priority)

print(sum(priorities))
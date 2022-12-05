# -----------------------
#   Advent of Code 2022
#   Day 3 Part 1
#   Author: James Hess
# -----------------------

input = []
commonItems = []
priorities = []

with open("Day3Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        input.append(line.strip())

# identify common items
for rucksack in input:
    lenRucksack = len(rucksack)
    compartment1 = rucksack[0:int(lenRucksack/2)]
    compartment2 = rucksack[int(lenRucksack/2):]
    for item in compartment1:
        if compartment2.find(item) != -1:
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
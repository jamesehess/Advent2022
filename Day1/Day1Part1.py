# -----------------------
#   Advent of Code 2022
#   Day 1 Part 1
#   Author: James Hess
# -----------------------

maxCalories = 0
inputs = []
calories = []

with open("Day1Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        inputs.append(line.strip())

calorieCount = 0
for input in inputs:
    if input == '':
        calories.append(calorieCount)
        calorieCount = 0
    else:
        calorieCount += int(input)
calories.append(calorieCount)

maxCalories = max(calories)
print(maxCalories)
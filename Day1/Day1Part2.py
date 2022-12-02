# -----------------------
#   Advent of Code 2022
#   Day 1 Part 2
#   Author: James Hess
# -----------------------

inputs = []
calories = []
sumCalories = 0


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

while len(calories) > 3:
    calories.remove(min(calories))

sumCalories = sum(calories)
print(sumCalories)
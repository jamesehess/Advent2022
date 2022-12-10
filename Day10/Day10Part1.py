# -----------------------
#   Advent of Code 2022
#   Day 10 Part 1
#   Author: James Hess
# -----------------------

commands = []
cycles = []
X = 1

with open("Day10Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        commands.append(line.strip())


for command in commands:
    cycles.append(X)
    if command.startswith("addx"):
        cycles.append(X)
        value = command.split()[1]
        X = X + int(value)

signal = 20 * cycles[19] + 60 * cycles[59] + 100 * cycles[99] + 140 * cycles[139] + 180 * cycles[179] + 220 * cycles[219]
print(signal)
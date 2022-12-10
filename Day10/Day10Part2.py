# -----------------------
#   Advent of Code 2022
#   Day 10 Part 2
#   Author: James Hess
# -----------------------

commands = []
cycles = []
X = 1

with open("Day10Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        commands.append(line.strip())

# initialize display
display = []
display_length = 40
for x in range(0, 6 * display_length):
    display.append(".")

# process commands into cycles
for command in commands:
    cycles.append(X)
    if command.startswith("addx"):
        cycles.append(X)
        value = command.split()[1]
        X = X + int(value)

# update display when cycle index and X position(+/-1) are the same
for idx, cycle in enumerate(cycles):
    if idx % 40 in range(cycle-1,cycle+2):
        display[idx] = "#"

# print display
for idx, pixel in enumerate(display):
    if idx % display_length == 0 :
        print("\n", end='')
    print(pixel, end='')

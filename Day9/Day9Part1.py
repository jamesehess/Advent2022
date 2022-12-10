# -----------------------
#   Advent of Code 2022
#   Day 9 Part 1
#   Author: James Hess
# -----------------------

inputs = []
head_position = [0,0]
tail_position = [0,0]
tail_positions = [[0,0]]


with open("Day9Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        inputs.append(line.strip().split())

def move_tail():
    if head_position[0] == tail_position[0] and head_position[1] > tail_position[1]:
        # move tail up
        tail_position[1] += 1
    elif head_position[0] == tail_position[0] and head_position[1] < tail_position[1]:
        # move tail down
        tail_position[1] -= 1
    elif head_position[1] == tail_position[1] and head_position[0] > tail_position[0]:
        # move tail right
        tail_position[0] += 1
    elif head_position[1] == tail_position[1] and head_position[0] < tail_position[0]:
        # move tail left
        tail_position[0] -= 1
    elif head_position[0] > tail_position[0] and head_position[1] > tail_position[1]:
        # move tail up-right
        tail_position[0] += 1
        tail_position[1] += 1
    elif head_position[0] > tail_position[0] and head_position[1] < tail_position[1]:
        # move tail down-right
        tail_position[0] += 1
        tail_position[1] -= 1
    elif head_position[0] < tail_position[0] and head_position[1] > tail_position[1]:
        # move tail up-left
        tail_position[0] -= 1
        tail_position[1] += 1
    elif head_position[0] < tail_position[0] and head_position[1] < tail_position[1]:
        # move tail down-left
        tail_position[0] -= 1
        tail_position[1] -= 1

def move_head(direction, velocity):
    for step in range(0,velocity):
        # move head
        if direction == "R":
            head_position[0] = head_position[0] + 1
        elif direction == "L":
            head_position[0] = head_position[0] - 1
        elif direction == "U":
            head_position[1] = head_position[1] + 1
        elif direction == "D":
            head_position[1] = head_position[1] - 1
        # see if we need to move tail
        if abs(head_position[0] - tail_position[0]) > 1 or abs(head_position[1] - tail_position[1]) > 1:
            # move tail
            move_tail()
            # record tail position
            if not tail_position in tail_positions:
                tail_positions.append(tail_position[:])

for input in inputs:
    move_head(input[0],int(input[1]))

print(len(tail_positions))
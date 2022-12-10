# -----------------------
#   Advent of Code 2022
#   Day 9 Part 2
#   Author: James Hess
# -----------------------

import numpy

inputs = []
tail_positions = [[0,0]]

with open("Day9Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        inputs.append(line.strip().split())

class knot:
    def __init__(self, parent=None, child=None):
        self.position = [0,0]
        self.parent = parent
        self.child = child

    def add_child(self, ch):
        self.child = ch

    def move(self, direction='', velocity=0):
        # if head then move
        if self.parent == None:
            for step in range(0, velocity):
                # move head
                if direction == "R":
                    self.position[0] = self.position[0] + 1
                elif direction == "L":
                    self.position[0] = self.position[0] - 1
                elif direction == "U":
                    self.position[1] = self.position[1] + 1
                elif direction == "D":
                    self.position[1] = self.position[1] - 1
                # update next knot
                self.child.move()

        # if tail and not adjacent, then move
        elif abs(self.position[0]-self.parent.position[0]) > 1 or abs(self.position[1]-self.parent.position[1]) > 1:
            xoff = numpy.sign(self.parent.position[0]-self.position[0])
            yoff = numpy.sign(self.parent.position[1]-self.position[1])
            self.position[0] = self.position[0] + xoff
            self.position[1] = self.position[1] + yoff
            if self.child:
                # update segments down rope
                self.child.move()
            else:
                # i'm the tail and need to update the tail position list
                if not self.position in tail_positions:
                    tail_positions.append(self.position[:])

head = knot()
parent_knot = head
for x in range(0,9):
    new_knot = knot(parent_knot)
    parent_knot.add_child(new_knot)
    parent_knot = new_knot

for input in inputs:
    head.move(input[0],int(input[1]))

print(len(tail_positions))
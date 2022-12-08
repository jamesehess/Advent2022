# -----------------------
#   Advent of Code 2022
#   Day 7 Part 2
#   Author: James Hess
# -----------------------

input = []

with open("Day7Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        input.append(line.strip())

class elfFile:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        parent.update_size(self.size)

class elfDir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def update_size(self, addSize):
        self.size += addSize
        if self.parent:
            self.parent.update_size(addSize)

    def add_directory(self, name):
        self.children.append(elfDir(name, self))

    def add_file(self, name, size):
        self.children.append(elfFile(name, size, self))

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child

root = elfDir("/", None)
currDir = None

# parse input into tree structure
for command in input:
    if command.startswith("$ cd"):
        target = command.split()[2]
        if target == "/":
            currDir = root
        elif target == "..":
            currDir = currDir.parent
        else:
            currDir = currDir.get_child(target)
    elif command.startswith("$ ls"):
        continue
    else:
        temp = command.split()
        if temp[0] == "dir":
            currDir.add_directory(temp[1])
        else:
            currDir.add_file(temp[1],int(temp[0]))

# function to recursively search the tree structure for directory's with size less than 100000
def find_directories(dir, limit, foundList):
    if dir.size > limit:
        foundList.append(dir.size)
    for child in dir.children:
        if isinstance(child, elfDir):
            find_directories(child, limit, foundList)
    return foundList

usedSpace = root.size
unusedSpace = 70000000 - usedSpace
neededSpace = 30000000 - unusedSpace

foundList = find_directories(root, neededSpace, [])
foundList.sort()
print(foundList[0])
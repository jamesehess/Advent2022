# -----------------------
#   Advent of Code 2022
#   Day 2 Part 2
#   Author: James Hess
# -----------------------

resultsList = [
    ['AX', 3],
    ['AY', 1],
    ['AZ', 2],
    ['BX', 1],
    ['BY', 2],
    ['BZ', 3],
    ['CX', 2],
    ['CY', 3],
    ['CZ', 1]
]

games = []
score = 0

with open("Day2Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        games.append(line.strip().replace(" ",""))

for game in games:
    #Determine my hand and score
    for result in resultsList:
        if result[0] == game:
            score += result[1]
            continue
    #Determine result score
    if game[1] == "X":
        score += 0
    elif game[1] == "Y":
        score += 3
    elif game[1] == "Z":
        score += 6

print(score)
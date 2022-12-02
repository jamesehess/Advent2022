# -----------------------
#   Advent of Code 2022
#   Day 2 Part 1
#   Author: James Hess
# -----------------------

resultsList = [
    ['AZ', 'Lose'],
    ['BX', 'Lose'],
    ['CY', 'Lose'],
    ['AX', 'Draw'],
    ['BY', 'Draw'],
    ['CZ', 'Draw'],
    ['AY', 'Win'],
    ['BZ', 'Win'],
    ['CX', 'Win']
]

games = []
score = 0

with open("Day2Input.txt") as file:
    lines = file.readlines()
    for line in lines:
        games.append(line.strip().replace(" ",""))

for game in games:
    #Determine game result
    for result in resultsList:
        if result[0] == game:
            gameResult = result[1]
            continue
    #Add shape score
    if game[1] == "X":
        score += 1
    elif game[1] == "Y":
        score += 2
    elif game[1] == "Z":
        score += 3
    #Add result score
    if gameResult == "Lose":
        score += 0
    elif gameResult == "Draw":
        score += 3
    elif gameResult == "Win":
        score += 6

print(score)
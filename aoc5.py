import math

with open('aoc5input.txt') as fobj:
    data = fobj.read()
    seats = data.split("\n")

id = []

for seat in seats:
    row = [0, 127]
    column = [0, 7]
    for letter in seat:
        if letter == "F":
            row[1] = math.floor(row[1] - ((row[1] - row[0]) / 2))
        if letter == "B":
            row[0] = math.ceil(row[0] + ((row[1] - row[0]) / 2))
        if letter == "L":
            column[1] = math.floor(column[1] - ((column[1] - column[0]) / 2))
        if letter == "R":
            column[0] = math.ceil(column[0] + ((column[1] - column[0]) / 2))
    row = row[0]
    column = column[0]
    id.append(row * 8 + column)

print(id)
print(max(id))
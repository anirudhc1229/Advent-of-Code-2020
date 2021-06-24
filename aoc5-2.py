import math

with open('aoc5input.txt') as fobj:
    data = fobj.read()
    seats = data.split("\n")

rows = []
columns = []


def decode_seat():
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
        rows.append(row[0])
        columns.append(column[0])

    found = find_seat()
    print(found)
    seat_id = found[0] * 8 + found[1]
    return seat_id


def find_seat():
    for row in range(1, 126, 1):
        if not (row in rows):
            for column in range(0, 7, 1):
                if not (column in columns):
                    return [row, column]


answer = decode_seat()
print(answer)

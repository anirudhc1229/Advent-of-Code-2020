with open('aoc3input.txt') as fobj:
    data = fobj.read()
    rows = data.split("\n")

for row in rows:
    current = row
    for x in range(1, 100, 1):
        current += row
    rows[rows.index(row)] = current

slope_x = [1, 3, 5, 7, 1]
slope_y = [1, 1, 1, 1, 2]
output = []
answer = 1

for slope in range(0, 5, 1):
    char = 0
    trees = 0
    for x in range(0, len(rows), slope_y[slope]):
        row = rows[x]
        if row[char] == "#":
            trees += 1
        char += slope_x[slope]
    output.append(trees)
    answer *= trees

print(output)
print(answer)

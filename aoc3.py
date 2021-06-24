with open('aoc3input.txt') as fobj:
    data = fobj.read()
    rows = data.split("\n")

for row in rows:
    current = row
    for x in range(1, 100, 1):
        current += row
    rows[rows.index(row)] = current

char = 0
trees = 0

for row in rows:
    if row[char] == "#":
        trees += 1
    char += 3

print(trees)

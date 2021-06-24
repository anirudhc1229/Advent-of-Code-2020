min = []
max = []
letter = []
password = []
output = []

with open('aoc2input.txt') as fobj:
    data = fobj.read()
    lines = data.split("\n")

for line in lines:
    min.append(int(line[0 : line.index("-")]))
    max.append(int(line[line.index("-") + 1 : line.index(" ")]))
    letter.append(line[line.index(" ") + 1 : line.index(":")])
    password.append(line[line.index(":") + 2 :])

for x in range(0, len(lines), 1):
    count = 0
    for char in password[x]:
        if char == letter[x]:
            count += 1
    if min[x] <= count <= max[x]:
        output.append(x)

answer = len(output)
print(answer)
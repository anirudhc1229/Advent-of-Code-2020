pos1 = []
pos2 = []
letter = []
password = []
output = []

with open('aoc2input.txt') as fobj:
    data = fobj.read()
    lines = data.split("\n")

for line in lines:
    pos1.append(int(line[0 : line.index("-")]))
    pos2.append(int(line[line.index("-") + 1 : line.index(" ")]))
    letter.append(line[line.index(" ") + 1 : line.index(":")])
    password.append(line[line.index(":") + 2 :])

for x in range(0, len(lines), 1):
    str = password[x]
    if (str[pos1[x] - 1] == letter[x]) ^ (str[pos2[x] - 1] == letter[x]):
        output.append(x)

answer = len(output)
print(answer)
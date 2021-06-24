numbers = []
got = False

with open('aoc1input.txt') as fobj:
    data = fobj.read()
    lines = data.split("\n")
    for x in lines:
        numbers.append(int(x))
    print(numbers)

def get_ans():
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if x + y + z == 2020:
                    print(x, y, z)
                    return x * y * z

answer = get_ans()
print(answer)
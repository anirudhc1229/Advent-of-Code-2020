with open('aoc4input.txt') as fobj:
    data = fobj.read()
    passports = data.split("\n\n")
    print(passports)

valid = []

for passport in passports:
    if passport.count(":") == 7:
        if not "cid" in passport:
            valid.append(passport)
    if passport.count(":") == 8:
        valid.append(passport)

print(valid)
print(len(valid))

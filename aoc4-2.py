with open('aoc4input.txt') as fobj:
    data = fobj.read()
    passports = data.split("\n\n")
    print(passports)


def check_valid():

    valid = []

    for passport in passports:
        if passport.count(":") == 7:
            if not "cid" in passport:
                if check_field(passport):
                    valid.append(passport)
        if passport.count(":") == 8:
            if check_field(passport):
                valid.append(passport)

    return [valid, len(valid)]


def check_field(passport):

    flatten = lambda t: [item for sublist in t for item in sublist]
    result = flatten(list(map(lambda x: x.split(), passport.splitlines())))

    print(result)

    for section in result:
        field = section[0 : 3]
        value = section[4 :]
        if field == "byr":
            if not 1920 <= int(value) <= 2002:
                return False
        if field == "iyr":
            if not 2010 <= int(value) <= 2020:
                return False
        if field == "eyr":
            if not 2020 <= int(value) <= 2030:
                return False
        if field == "hgt":
            if "cm" in value:
                if not 150 <= int(value[: -2]) <= 193:
                    return False
            elif "in" in value:
                if not 59 <= int(value[: -2]) <= 76:
                    return False
            else:
                return False
        if field == "hcl":
            if not ((value[0] == "#") and (len(value) == 7)):
                return False
        if field == "ecl":
            if not ((value == "amb") or (value == "blu") or (value == "brn") or (value == "gry") or (value == "grn") or (value == "hzl") or (value == "oth")):
                return False
        if field == "pid":
            if not ((len(value) == 9) and (is_int(value))):
                return False

    return True


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


output = check_valid()
print(output[0])
print(output[1])
f = open("input.txt", "r")
input_list = []
for i in f.read().split("\n\n"):
    if not i:
        continue
    input_list.append(i)

valid_passports = 0

for item in input_list:
    if 'byr' in item:
        if 'iyr' in item:
            if 'eyr' in item:
                if 'hgt' in item:
                    if 'hcl' in item:
                        if 'ecl' in item:
                            if 'pid' in item:
                                valid_passports += 1

print(valid_passports)

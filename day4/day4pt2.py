import re

f = open("input.txt", "r")
input_list = []
for i in f.read().split("\n\n"):
    if not i:
        continue
    input_list.append(i)

pid_pattern = re.compile("^[0-9]{9}$")
hcl_pattern = re.compile("^#[0-9a-f]{6}$")

valid_passports = 0
for item in input_list:
    my_map = {}
    for a_line in item.split("\n"):
        for an_entry in a_line.split(" "):
            key_value = an_entry.split(":")
            if len(key_value) != 2:  # account for trailing whitespace
                continue
            my_map[ key_value[0] ] = key_value[1]

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not (int(my_map.get('byr', 0)) >= 1920 and int(my_map.get('byr')) <= 2002):
        continue
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not (int(my_map.get('iyr', 0)) >= 2010 and int(my_map.get('iyr')) <= 2021):
        continue
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not (int(my_map.get('eyr', 0)) >= 2020 and int(my_map.get('eyr')) <= 2031):
        continue
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if len(my_map.get('hgt', '0qw')) < 3:
        continue
    number = int(my_map.get('hgt', '0qw')[0:-2])
    unit = my_map.get('hgt', '0qw')[-2:]
    if unit == 'cm':
        if number not in range(150, 194):
            continue
    elif unit == 'in':
       if number not in range(59, 77):
           continue
    else:
        continue
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not hcl_pattern.match(my_map.get('hcl', '')):
        continue
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if my_map.get('ecl', None) not in valid_ecl:
        continue
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not pid_pattern.match(my_map.get('pid', '')):
        continue        
    valid_passports += 1

print(valid_passports)

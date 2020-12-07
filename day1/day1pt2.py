# Read input file
f = open("input.txt", "r")
input_list = []
for i in f.read().split("\n"):
    if not i:
        continue
    input_list.append(int(i))

# For each digit read and put into a list, add to every other digit in the list and see if any sum equals 2020
for n in input_list:
    for y in input_list:
        for z in input_list:
            sum = (z + y + n)
            # If two uniquely valued integers added together equal 2020, multiply those ints
            if sum == 2020:
                product = (z * y * n)
                print(product)

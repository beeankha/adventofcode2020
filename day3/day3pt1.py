# Using the example input, which is much smaller, + answer, can help

# right 3, down 1 is the movement

# Start in upper left coner `.`

# Move as instructed and then determine if it's a . or a # (tree)
# += 1 whenever we hit a # and count how many of those were hit

# list of lists
f = open("input.txt", "r")
toboggan_slope = []
for line in f.read().split("\n"):
    if not line:
        continue
    toboggan_slope.append(list(line))
print(toboggan_slope)

x = 0
y = 0

tree = 0

while x < len(toboggan_slope):
    if y >= len(toboggan_slope[x]):
        y = y - len(toboggan_slope[x])
    # print(x, y, len(toboggan_slope[x]))
    print(toboggan_slope[x][y])
    if toboggan_slope[x][y] == '#':
        tree += 1
    x+=1
    y+=3

print(tree)

# print(toboggan_slope[0])
# print(toboggan_slope[0][0])
#
# print(toboggan_slope[1][3])
# print(toboggan_slope[x][y])

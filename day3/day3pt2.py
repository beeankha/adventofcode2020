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

x1 = 0  # down
y1 = 0  # right

tree1 = 0

while x1 < len(toboggan_slope):
    if y1 >= len(toboggan_slope[x1]):
        y1 = y1 - len(toboggan_slope[x1])
    print(toboggan_slope[x1][y1])
    if toboggan_slope[x1][y1] == '#':
        tree1 += 1
    x1+=1
    y1+=1

print(tree1)

x2 = 0  # down
y2 = 0  # right

tree2 = 0

while x2 < len(toboggan_slope):
    if y2 >= len(toboggan_slope[x2]):
        y2 = y2 - len(toboggan_slope[x2])
    print(toboggan_slope[x2][y2])
    if toboggan_slope[x2][y2] == '#':
        tree2 += 1
    x2+=1
    y2+=3

print(tree2)

x3 = 0  # down
y3 = 0  # right

tree3 = 0

while x3 < len(toboggan_slope):
    if y3 >= len(toboggan_slope[x3]):
        y3 = y3 - len(toboggan_slope[x3])
    print(toboggan_slope[x3][y3])
    if toboggan_slope[x3][y3] == '#':
        tree3 += 1
    x3+=1
    y3+=5

print(tree3)

x4 = 0  # down
y4 = 0  # right

tree4 = 0

while x4 < len(toboggan_slope):
    if y4 >= len(toboggan_slope[x4]):
        y4 = y4 - len(toboggan_slope[x4])
    print(toboggan_slope[x4][y4])
    if toboggan_slope[x4][y4] == '#':
        tree4 += 1
    x4+=1
    y4+=7

print(tree4)

x5 = 0  # down
y5 = 0  # right

tree5 = 0

while x5 < len(toboggan_slope):
    if y5 >= len(toboggan_slope[x5]):
        y5 = y5 - len(toboggan_slope[x5])
    print(toboggan_slope[x5][y5])
    if toboggan_slope[x5][y5] == '#':
        tree5 += 1
    x5+=2
    y5+=1

print(tree5)

product = tree1 * tree2 * tree3 * tree4 * tree5
print(product)

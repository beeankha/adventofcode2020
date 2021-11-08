# Read input file
input_list = []
with open("input.txt", "r") as f:
    for i in f.read().split(".\n"):
        if not i:
            continue
        input_list.append(i)

# Hash map 1: This color contains these colors
bag_rules_hash = {}
for bag_rules in input_list:
    top_level_color, contained_colors = bag_rules.split(" bags contain ")
    bag_rules_hash[top_level_color] = contained_colors

sgp = []

def bag_color_check(color):
    global sgp
    # Find all of the colors that directly contain our color
    for key in bag_rules_hash.keys():
        if color in bag_rules_hash[key]:
            if key not in sgp:
                sgp.append(key)
                bag_color_check(key)

result = bag_color_check('shiny gold')
print(sgp)
print(len(sgp))

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

color_cache = {}

def get_nested_count(color):
    global color_cache
    number_of_bags_inside_color = 0
    # Find the color in the hash
    if color in color_cache:
        return color_cache[color]
        
    if bag_rules_hash[color] == 'no other bags':
        color_cache[color] = 0
        return 0

    for colors in bag_rules_hash[color].split(", "):
        contained_bags, bag_color = colors.split(" ", 1)  # Split takes another argument, which is how many times to split the item
        bag_color = bag_color.split(" bag")[0]
        number_of_bags_inside_this_new_color = get_nested_count(bag_color)
        print("Number of bags inside a {} is {}".format(bag_color, (int(contained_bags) * number_of_bags_inside_this_new_color)))
        number_of_bags_inside_color += int(contained_bags) * ( number_of_bags_inside_this_new_color + 1 )
    color_cache[color] = number_of_bags_inside_color
    return number_of_bags_inside_color

total_bags = get_nested_count('shiny gold')
print(total_bags)

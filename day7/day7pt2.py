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

def get_nested_count(color):
    number_of_bags_inside_color = 0
    # Find the color in the hash
    if bag_rules_hash[color] == 'no other bags':
        return 0

    for colors in bag_rules_hash[color].split(", "):
        contained_bags, bag_color = colors.split(" ", 1)  # Split takes another argument, which is how many times to split the item
        bag_color = bag_color.split(" bag")[0]
        number_of_bags_inside_this_new_color = get_nested_count(bag_color)
        print("Number of bags inside a {} is {}".format(bag_color, (int(contained_bags) * number_of_bags_inside_this_new_color)))
        number_of_bags_inside_color += int(contained_bags) * ( number_of_bags_inside_this_new_color + 1 )
    return number_of_bags_inside_color

total_bags = get_nested_count('shiny gold')
print(total_bags)

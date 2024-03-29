# Read input, split on every blank line (every separate chunk is a group)
input_list = []
with open("input.txt", "r") as f:
    for i in f.read().split("\n\n"):
        if not i:
            continue
        input_list.append(i)

yes_answers = 0
for group_response in input_list:
    group_map = {}  # the hash map!
    # Create a hash map of just the first line of the group
    for individual_response in group_response.split("\n")[0]:
        for char in individual_response:
            group_map[char] = True
    # Create a hash map for subsequent lines of the group
    for rest_of_group in group_response.split("\n")[1:]:
        if rest_of_group:
            if len(group_map) > 0:
                existing_keys = list(group_map.keys())
                for key in existing_keys:
                    if key not in rest_of_group:
                        del group_map[key]
            
    # Take the number of those individual letters from each group and sum them
    yes_answers += len(group_map)

print(yes_answers)

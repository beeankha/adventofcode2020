# Read input, split on every blank line (every separate chunk is a group)
input_list = []
with open("input.txt", "r") as f:
    for i in f.read().split("\n\n"):
        if not i:
            continue
        input_list.append(i)

# Within each group, count how many different letters are listed
yes_answers = 0
for group_response in input_list:
    group_map = {} # the hash map!
    for individual_response in group_response.split("\n"):
        for char in individual_response:
            group_map[char] = "yes"
    # Take the number of those individual letters from each group and sum them
    yes_answers += len(group_map)

print(yes_answers)

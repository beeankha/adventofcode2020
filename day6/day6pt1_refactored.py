# Read input, split on every blank line (every separate chunk is a group)
# This now has an inner structure of lists within a list
with open("input.txt", "r") as f:
    input_list = [i.split() for i in f.read().split("\n\n") if i]

# Within each group, count how many different letters are listed
# Generator expression below!
yes_answers = sum(
    len({
        char
        for individual_response in group_response
        for char in individual_response
    })
    for group_response in input_list
)

# The example below shows another possible way to refactor!
# sum(
#     sum(
#         1 for char in lowercase_letters
#         if any(char in person for person in group)
#     )
#     for group in groups
# )

print(yes_answers)

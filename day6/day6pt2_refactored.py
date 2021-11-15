import functools

# Read input, split on every blank line (every separate chunk is a group)
# This now has an inner structure of lists within a list
with open("input.txt", "r") as f:
    input_list = [i.split() for i in f.read().split("\n\n") if i]

# Within each group, count how many different letters are listed
yes_answers = sum(
    len(functools.reduce(
        # lambda a, b: a.intersection(b) <--- is the explicit way to write this out
        lambda a, b: a & b,
        (set(individual_response) for individual_response in group_response[1:]),
        set(group_response[0])
    ))
    for group_response in input_list
)

# The example below shows another possible way to refactor!
# sum(
#     sum(
#         1 for char in lowercase_letters
#         if all(char in person for person in group)
#     )
#     for group in groups
# )

print(yes_answers)

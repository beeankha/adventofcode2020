# Read input file
input_list = []
with open("input.txt", "r") as f:
    for i in f.read().split("\n"):
        if not i:
            continue
        input_list.append(i)

# Need to have an int that starts at 0 and then increments every time acc is encountered,
# adding whatever that number is to the int value (also index += 1)
accumulator = 0

# The +x or -x digits could affect the index in either a list (in the cases of jmp)
# Need to use the index in order to figure out where to jump to for commands
index = 0

# Have a set for the indexes instead of a list
# If it's a list, it'll be O(n) due to scanning of the entire list (vs O(1) for
# a set, since those work like a hash map)
visited_indexes = set()

while index not in visited_indexes:
    instruction_type = input_list[index][:3]
    counter = input_list[index][4:]
    visited_indexes.add(index)  # Gotta "add" vs "append" because it's a set, not a list
    if instruction_type == 'nop':
        # nop = continue to the next step (so index += 1)
        index += 1
        continue
    elif instruction_type == 'acc':
        index += 1
        accumulator += int(counter)
    elif instruction_type == 'jmp':
        index += int(counter)
# Print out the accumulated value as soon as a previously-called command is hit!
print(accumulator)

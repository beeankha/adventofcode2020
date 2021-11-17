import itertools
import sys

# Read input file
with open("input.txt", "r") as f:
    input_list = [i for i in f.read().split("\n") if i]

# Turn everything in the list into an int
for i in range(0, len(input_list)):
    input_list[i] = int(input_list[i])

start_of_range = 0
end_of_range = 25  # This can't be '4' because the array indexing doesn't work like that
index_of_total = 25

while end_of_range < len(input_list):
    # Iterate through the list slice to see if there are any sums that add up to the target
    list_slice = input_list[start_of_range:end_of_range]
    target = input_list[index_of_total]
    result = [x for x in itertools.permutations(list_slice, r=2) if x[0] + x[1] == int(target)]
    if len(result) > 0:
        start_of_range += 1
        end_of_range += 1
        index_of_total += 1
    else:
        bad_number = target
        break

for x in range(0, len(input_list)):
    for y in range(x+2, len(input_list)):
        sum_of_x_to_y = sum(input_list[x:y])
        print("Sum of number {} is {}".format(input_list[x:y], sum_of_x_to_y))
        if sum_of_x_to_y < bad_number:
            # Already doing a range on y (inner loop) so no need to y += 1
            continue
        elif sum_of_x_to_y > bad_number:
            # Already doing a range (outer loop) so no need to x += 1
            break
        elif sum_of_x_to_y == bad_number:
            contiguous_list = input_list[x:y]
            contiguous_list.sort()
            encryption_number = contiguous_list[0] + contiguous_list[-1]
            print(encryption_number)
            sys.exit()

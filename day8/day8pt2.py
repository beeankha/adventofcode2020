import sys


# Read input file
input_list = []
with open("input.txt", "r") as f:
    for i in f.read().split("\n"):
        if not i:
            continue
        input_list.append(i)

def detect_infinite_loop(instructions):
    visited_indexes = []
    accumulator = 0
    index = 0
    infinite_loop = True

    while index not in visited_indexes:
        if index == len(instructions):
            infinite_loop = False
            break
        instruction_type = instructions[index][:3]
        counter = instructions[index][4:]
        visited_indexes.append(index)
        if instruction_type == 'nop':
            index += 1
            continue
        elif instruction_type == 'acc':
            index += 1
            accumulator += int(counter)
        elif instruction_type == 'jmp':
            index += int(counter)

    return accumulator, infinite_loop

# Look at each instruction; if it's jmp, change it to nop and vice versa; ignore if it's acc
for index in range(0,len(input_list)):
    instruction = input_list[index][:3]
    if instruction == 'acc':
        continue
    elif instruction == 'nop':
        input_list[index] = input_list[index].replace("nop", "jmp")
    elif instruction == 'jmp':
        input_list[index] = input_list[index].replace("jmp", "nop")

    # After changing it, run the detect_infinite_loop() function
    accumulator_value, was_infinite_loop = detect_infinite_loop(input_list)
    print(f"Changing {index} from {instruction} to {input_list[index][:3]} gave {accumulator_value}, {was_infinite_loop}")
    
    # If that returns True, do the switcheroo to the next instruction (if it's not acc)
    if was_infinite_loop is True:
        print("Setting instruction back")
        if instruction == 'nop':
            input_list[index] = input_list[index].replace("jmp", "nop")
        elif instruction == 'jmp':
            input_list[index] = input_list[index].replace("nop", "jmp")
        continue
    # If it's false, print the value of the accumulator
    else:
        print(accumulator_value)
        sys.exit(0)
            
print("Checked all instructions and did not win")

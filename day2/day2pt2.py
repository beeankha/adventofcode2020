# Read the input file
f = open("input.txt", "r")
# Have a variable represent number of correct passwords
num_correct_password = 0
for i in f.read().split("\n"):
    if not i:
        continue
    # Separate via `:` symbol into rule + password
    (rule, password) = i.split(": ")
    (unsplit_number, letter) = rule.split(" ")
    numbers = unsplit_number.split("-")
    first_number = int(numbers[0])
    second_number = int(numbers[1])
    print(numbers)
    if (password[first_number - 1] == letter) ^ (password[second_number - 1] == letter):
        num_correct_password += 1

# Print the answer
print(num_correct_password)

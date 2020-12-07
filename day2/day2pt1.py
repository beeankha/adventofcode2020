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
    if password.count(letter) in range(int(numbers[0]), int(numbers[1]) + 1):
        # Increment the number as more correct passwords are found
        num_correct_password += 1
    else:
        print(unsplit_number)
        print(letter)
        print(password)

# Print the answer
print(num_correct_password)

# Read the file

input_list = []
seat_values = [0]
with open("input.txt", "r") as f:
    for i in f.read().split("\n"):
        if not i:
            continue
        input_list.append(i)

for a_seat in input_list:
    # Search through the rows in 6 steps (128 possibilities) to determine row location
    # Search through the columns in 3 steps (8 possibilities) to determine column location
    # Multiply the row by 8 and then add the column number in order to get the seat's "value"
    # Determine which seat number has the highest value seat ID
    min_row_number = 0
    max_row_number = 127

    for row_id_char in a_seat[0:7]:
        mid_point = int((max_row_number - min_row_number + 1) / 2)
        if row_id_char == "F":
            max_row_number = max_row_number - mid_point
        elif row_id_char == "B":
            min_row_number = min_row_number + mid_point

    min_col_number = 0
    max_col_number = 7
    for col_id_char in a_seat[7:10]:
        mid_point = int((max_col_number - min_col_number + 1) / 2)
        if col_id_char == "L":
            max_col_number = max_col_number - mid_point
        elif col_id_char == "R":
            min_col_number = min_col_number + mid_point

    seat_value = int((max_row_number * 8) + max_col_number)
    if seat_value > seat_values[0]:
        seat_values.pop()
        seat_values.append(seat_value)

print(seat_values)

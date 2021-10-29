import sys

input_list = []
seat_ids = []

with open("input.txt", "r") as f:
    for i in f.read().split("\n"):
        if not i:
            continue
        input_list.append(i)

for a_seat in input_list:
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
    seat_ids.append(seat_value)

min_index = 0
seat_ids.sort()
for i in range(0, len(seat_ids)):
    if seat_ids[i] + 1 != seat_ids[i + 1]:
        my_seat = seat_ids[i] + 1
        print(f"This is your seat ID: {my_seat}")
        exit(0)

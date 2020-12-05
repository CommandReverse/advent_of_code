with open('/home/jelte/Desktop/programming/advent_of_code/2020/day_5', 'r') as file:
    d = file.readlines()

data = [i.strip('\n') for i in d]

def binary_search(lower, upper, choice):
    lower, upper = lower, upper
    c = (lower + upper) // 2
    print(lower, upper, c)
    if lower == upper:
        return [lower, upper]
    if choice == 'F' or choice == 'L':
        upper = c
        return [lower, upper]
    if choice == 'B' or choice == 'R':
        lower = c
        return [lower, upper]

def calc_seat_id(line):
    col_l, col_u = 0, 128
    row_l, row_u = 0, 8
    for letter in line:
        if letter == "F" or letter == "B":
            response_list = binary_search(col_l, col_u, letter)
            col_l, col_u = response_list
        if letter == "L" or letter == "R":
            response_list = binary_search(row_l, row_u, letter)
            row_l, row_u = response_list
        seat_id = 8 * col_l + row_l
    return seat_id

def part_1():
    highest = 0
    for line in data:
        seat_id = calc_seat_id(line)
        if seat_id > highest:
            highest = seat_id
    return highest

def part_2():
    sorted_ids = sorted([calc_seat_id(i) for i in data])
    first_id = sorted_ids[0]
    for i, seat_id in enumerate(sorted_ids):
        # Work out which id is missing
        if seat_id != i + first_id:
            return seat_id - 1

if __name__ == "__main__":
    print(part_2())
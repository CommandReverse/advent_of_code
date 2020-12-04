from operator import xor
total = 0
f = open("/home/jd/Desktop/Advent_of_code/2_input", "r")

for line in f.readlines():
    counter = 0
    r, sequence = line.split(":")
    sequence = sequence.strip(" ")
    t_range, letter = r.split(" ")
    lower, upper = t_range.split("-")
    if sequence[int(lower) - 1] == " ":
        print(sequence)
        print("oops")

    if xor(bool(sequence[int(lower) - 1] == letter), bool(sequence[int(upper) - 1] == letter)):
        total += 1

print(total)
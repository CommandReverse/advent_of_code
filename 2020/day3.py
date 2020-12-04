with open('day_3', 'r') as file:
    d = file.readlines()

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
MAP_WIDTH = len(d[0]) - 1

def check_trees(x, y):
    x_pos, trees = 0, 0 
    for line in d[::y]:
        if line[x_pos] == "#":
            trees += 1
        x_pos = (x_pos + x) % MAP_WIDTH
    return trees

def product(l):
    result = 1
    for item in l:
        result *= item
    return result


print(product([check_trees(*s) for s in SLOPES]))
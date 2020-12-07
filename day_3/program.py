import math
slope_map = open('input.txt').readlines()

slope_width = len(slope_map[0]) - 1

slope_params = [(1,1), (3,1), (5,1), (7,1), (1,2)]
results = []

for param in slope_params:
    tree_count = 0
    for i in range(len(slope_map)):
        if i % param[1] == 0:
            tree_count = tree_count + int(slope_map[i][(int(i * param[0] / param[1])) % slope_width] == '#')
    print(tree_count)
    results.append(tree_count)

print(math.prod(results))

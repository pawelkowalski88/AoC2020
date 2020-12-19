import itertools
file = open('input.txt')
lines = file.readlines()
file.close()

lines = [[[(0,0, x-1, y-1),v] for x,v in enumerate(l) if v != '\n'] for y,l in enumerate(lines)]
cubes = {x[0]:x[1] for x in list(itertools.chain(*lines))}


# print(cubes)
# print('neighbors', neighbors)

for i in range(6):
    neighbors = {}
    for c in cubes:
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                for z in [-1,0,1]:
                    for w in [-1,0,1]:
                        if cubes[c] == '#':
                            key = (c[0]+x, c[1]+y, c[2]+z, c[3]+w)
                            if key not in neighbors.keys():
                                neighbors[key] = 0
                            neighbors[key] += 1 
    new_cubes = {}
    for n in neighbors:
        if cubes.get(n, '.') == '.':
            val = '.'
            if neighbors[n] == 3:
                val = '#'
        else:
            val = '#'
            if neighbors[n] == 3 or neighbors[n] == 4:
                val = '#'
            else:
                val = '.'
        new_cubes[n] = val

    cubes = new_cubes

print(sum([1 for x in cubes.values() if x == '#']))
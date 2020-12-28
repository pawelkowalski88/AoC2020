import itertools, math
file = open('/Users/pawelkowalski/Projects/AoC2020/day_20/input.txt')
tiles_raw = file.read().split('\n\n')
file.close()
file = open('/Users/pawelkowalski/Projects/AoC2020/day_20/monster.txt')
monster = [l.rstrip('\n') for l in file.readlines()]
file.close()
tiles = {}
tiles_border_values = {}

print(monster)

for tile in tiles_raw:
    tiles_split = tile.split('\n')
    tiles[int(tiles_split[0].split(' ')[1].rstrip(':'))] = tiles_split[1:]

def calculate_tile_borders(tile):
    b_y = (''.join(['1' if t == '#' else '0' for t in tile[0]]), ''.join(['1' if t == '#' else '0' for t in tile[9]]))
    b_x = (''.join(['1' if t[0] == '#' else '0' for t in tile]), ''.join(['1' if t[9] == '#' else '0' for t in tile]))
    return [int(b, 2) for b in b_x],[int(b, 2) for b in b_y]

def get_dict_key(value):
    return min([value, int('{:010b}'.format(value)[::-1], 2)])

def rotate_tile(tile):
    temp = []
    
    for x in range(len(tile[0])):
        line = ''
        for t in tile[::-1]:
            line += t[x]
        temp.append(line)
    return temp

def flip_h(tile):
    return [t[::-1] for t in tile]

def flip_v(tile):
    return tile[::-1]

for t in tiles:
    b_x, b_y = calculate_tile_borders(tiles[t])
    for b in b_x:
        if get_dict_key(b) not in tiles_border_values.keys():
            tiles_border_values[get_dict_key(b)] = [t]
        else:
            tiles_border_values[get_dict_key(b)].append(t)
    for b in b_y:
        if get_dict_key(b) not in tiles_border_values.keys():
            tiles_border_values[get_dict_key(b)] = [t]
        else:
            tiles_border_values[get_dict_key(b)].append(t)

matching_borders = dict(filter(lambda x: len(x[1]) > 1, tiles_border_values.items()))
corners = {}
for m in matching_borders.values():
    for k in m:
        if k not in corners.keys():
            corners[k] = 0
        corners[k] += 1
corners = dict(filter(lambda x: x[1] == 2, corners.items()))


tiles_places = {}

first_corner = list(corners.keys())[0]
tiles_places[(0, 0)] = first_corner
p_x = p_y = 0
current_tile = first_corner
x, y = calculate_tile_borders(tiles[current_tile])
if get_dict_key(x[0]) in matching_borders.keys():
    tiles[current_tile] = flip_h(tiles[current_tile])
if get_dict_key(y[0]) in matching_borders.keys():
    tiles[current_tile] = flip_v(tiles[current_tile])

for i in range(len(tiles) -1):
    x, y = calculate_tile_borders(tiles[current_tile])
    if get_dict_key(x[1]) in matching_borders.keys():
        pair = matching_borders[get_dict_key(x[1])]
        p_x += 1
    else:
        current_tile = tiles_places[(0, p_y)]
        x, y = calculate_tile_borders(tiles[current_tile])
        if get_dict_key(y[1]) in matching_borders.keys():
            pair = matching_borders[get_dict_key(y[1])]
            p_y += 1
            p_x = 0
        else:
            pair = matching_borders[get_dict_key(y[0])]
            p_y += 1
            p_x = 0

    new_tile = list(filter(lambda x: not x == current_tile, pair))[0]
    x_n, y_n = calculate_tile_borders(tiles[new_tile])


    tiles_places[(p_x, p_y)] = new_tile

    if get_dict_key(x[1]) not in [get_dict_key(x) for x in x_n] and p_x != 0 or get_dict_key(y[1]) not in [get_dict_key(y) for y in y_n] and p_x == 0:
        tiles[new_tile] = rotate_tile(tiles[new_tile])
        x_n, y_n = calculate_tile_borders(tiles[new_tile])

    if not p_x == 0:
        if not get_dict_key(x[1]) == get_dict_key(x_n[0]):
            tiles[new_tile] = flip_h(tiles[new_tile])
            x_n, y_n = calculate_tile_borders(tiles[new_tile])
        
        if not x[1] == x_n[0]:
            tiles[new_tile] = flip_v(tiles[new_tile])

    else:
        if not get_dict_key(y[1]) == get_dict_key(y_n[0]):
            tiles[new_tile] = flip_v(tiles[new_tile])
            x_n, y_n = calculate_tile_borders(tiles[new_tile])
        
        if not y[1] == y_n[0]:
            tiles[new_tile] = flip_h(tiles[new_tile])

    current_tile = new_tile

print(tiles_places)

size = max([k[1] for k in tiles_places.keys()]) + 1
image = []
for i in range(size):
    for n in range(8):
        line = ''
        for j in range(size):
            line += tiles[tiles_places[(j,i)]][n + 1][1:9]
        image.append(line)


image = rotate_tile(image)
image = rotate_tile(image)
#image = flip_v(image)

for i in image:
    print(i)

first_row_sum = int(''.join(['1' if i == 'O' else '0' for i in monster[0]]), 2)
second_row_sum = int(''.join(['1' if i == 'O' else '0' for i in monster[1]]), 2)
third_row_sum = int(''.join(['1' if i == 'O' else '0' for i in monster[2]]), 2)

first = int(''.join(['1' if i == 'O' else '0' for i in monster[0]]), 2)
second = int(''.join(['1' if i == 'O' else '0' for i in monster[1]]), 2)
third = int(''.join(['1' if i == 'O' else '0' for i in monster[2]]), 2)
found = 0
for y in range(len(image) - len(monster) + 1):
    for x in range(len(image[0]) - len(monster[0]) + 1):
        first_image = int(''.join(['1' if i == '#' else '0' for i in image[y][x:x + len(monster[0])]]),2) 
        second_image = int(''.join(['1' if i == '#' else '0' for i in image[y+1][x:x + len(monster[1])]]),2) 
        third_image = int(''.join(['1' if i == '#' else '0' for i in image[y+2][x:x + len(monster[2])]]),2)
        first_row = first_image & first
        second_row = second_image & second
        third_row =  third_image & third

        if first_row_sum == first_row and second_row_sum == second_row and third_row_sum == third_row:
            found += 1
            print('found')
            for j in range(3):
                for i in range(len(monster[0])):
                    if monster[j][i] == 'O':
                        image[y + j] = image[y+j][:x+i] + 'O' + image[y+j][x+i+1:]
print(found)
for i in image:
    print(i)

print(sum([sum([1 if x == '#' else 0 for x in i])for i in image]))
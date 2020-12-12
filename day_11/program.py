import itertools

def count_seats_taken(seats, x, y):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0,0)]
    total_count = 0
    for dir in directions:
        step = 1
        while True:
            if 0 <= x + step * dir[0] < len(seats) and 0 <= y + step * dir[1] < len(seats[0]):
                if seats[x + step * dir[0]][y + step * dir[1]] == '#':
                    total_count += 1
                    break
                if seats[x + step * dir[0]][y + step * dir[1]] == 'L':
                    break
            else:
                break
            if dir == (0,0):
                break
            step += 1

    return total_count
    # sub_table = seats[max(0,x-1):min(x+1, len(seats))+1]
    # sub_table = [sub_row[max(0,y-1):min(y+1, len(seats[0]))+1] for sub_row in sub_table]
    # return sum([el == '#' for el in list(itertools.chain.from_iterable(sub_table))])


file = open('input.txt')
lines = [[y for y in x.rstrip('\n')] for x in file.readlines()]

while True:
    results = []
    for x in lines:
        temp = []
        for y in x:
            temp.append(y)
        results.append(temp)
    for x in range(0, len(lines)):
        for y in range(0, len(lines[0])):
            count = count_seats_taken(lines, x, y)
            if lines[x][y] == 'L' and count == 0:
                results[x][y] = '#'
                continue
            if lines[x][y] == '#' and count  > 5:
                results[x][y] = 'L'
                continue

    results_sum = sum([el == '#' for el in list(itertools.chain.from_iterable(results))])
    lines_sum = sum([el == '#' for el in list(itertools.chain.from_iterable(lines))])
    print(results_sum)
    lines_serialized = ''.join(list(itertools.chain.from_iterable(lines)))
    results_serialized = ''.join(list(itertools.chain.from_iterable(results)))

    if lines_serialized == results_serialized:
        break

    for line in results:
        print(''.join(line))

    lines = []

    for x in results:
        temp = []
        for y in x:
            temp.append(y)
        lines.append(temp)

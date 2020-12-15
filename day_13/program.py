import math

file = open('input.txt')
lines = file.readlines()
file.close()

arrival_time = int(lines[0])
bus_ids = list(filter(lambda x: x != 'x', lines[1].split(',')))
bus_ids_values = lines[1].split(',')
bus_ids_dict = {i:bus_ids_values[i] for i in range(0, len(bus_ids_values))}
print(bus_ids_dict)

def part1(arr_time, ids):
    dict_result = {id: int(arrival_time / int(id) + 1) * int(id) for id in bus_ids}
    result =  min(dict_result, key = lambda k: dict_result[k])
    print(int(result) * (dict_result[result]- arr_time))

def part2(bus_ids):
    filtered_bus_ids = dict(filter(lambda x: x[1] != 'x', list(bus_ids.items())))
    i = n = int(filtered_bus_ids[0])
    prev_1 = prev_2 = 0
    count = 2
    while True:
        if all([(n + int(x[0])) % int(x[1]) == 0 for x in list(filtered_bus_ids.items())[1:count]]):
            if len(filtered_bus_ids) == count:
                print(n)
                break
            print(n)
            if((prev_2 - prev_1) == (prev_1 - n)):
                i = n - prev_1
                count += 1
            prev_2 = prev_1
            prev_1 = n
        n += i
        
part1(arrival_time, bus_ids)
part2(bus_ids_dict)
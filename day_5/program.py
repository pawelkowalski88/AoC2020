file = open('input.txt')
lines = file.readlines()
file.close()

seat_ids = [int(''.join(['0' if x == 'F' or x == 'L' else '1' if x == 'B' or x == 'R' else '' for x in line]), 2) for line in lines]

print(max(seat_ids))
seat_ids.sort()

min_id = min(seat_ids)
max_id = max(seat_ids) 

for x in range(min_id, max_id):
    #print(test_set)
    if x not in seat_ids and x-1 in seat_ids and x+1 in seat_ids:
        print('your seat:')
        print(x)

#print(seat_ids)
import math

file = open('input.txt')
lines = [(x[0], int(x[1:])) for x in file.readlines()]
file.close()

direction_angle = 0
direction = [math.cos(direction_angle * math.pi / 180), math.sin(direction_angle * math.pi / 180)]
position = [0,0]
waypoint = [10, 1]

for x in lines:
    print(x)
    
    if x[0] == 'N':
        waypoint[1] += x[1]

    if x[0] == 'S':
        waypoint[1] -= x[1]
    
    if x[0] == 'E':
        waypoint[0] += x[1]

    if x[0] == 'W':
        waypoint[0] -= x[1]

    if x[0] == 'R':
        direction_angle = -x[1]
        temp_waypoint = [waypoint[0], waypoint[1]]
        waypoint[0] = int(temp_waypoint[0] * math.cos(direction_angle * math.pi / 180)) - int(temp_waypoint[1] * math.sin(direction_angle * math.pi / 180))
        waypoint[1] = int(temp_waypoint[0] * math.sin(direction_angle * math.pi / 180)) + int(temp_waypoint[1] * math.cos(direction_angle * math.pi / 180))
    
    if x[0] == 'L':
        direction_angle = x[1]
        temp_waypoint = [waypoint[0], waypoint[1]]
        waypoint[0] = int(temp_waypoint[0] * math.cos(direction_angle * math.pi / 180)) - int(temp_waypoint[1] * math.sin(direction_angle * math.pi / 180))
        waypoint[1] = int(temp_waypoint[0] * math.sin(direction_angle * math.pi / 180)) + int(temp_waypoint[1] * math.cos(direction_angle * math.pi / 180))

    if x[0] == 'F':
        position[0] += int(x[1] * waypoint[0])
        position[1] += int(x[1] * waypoint[1])
    print('p: ', position, ' w: ', waypoint)

print(sum([abs(x) for x in position]))

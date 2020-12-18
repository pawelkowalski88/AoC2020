lines = [11,0,1,10,5,19]

turns_count = {}
turns = []
turn = 1
last_num = 0

for i in lines:
    turns_count[i] = [1, turn, 0]
    last_num = i
    turn += 1

while turn <= 30000000:
    if turns_count[last_num][0] == 1:   
        last_num = 0     
    else:
        last_num = turn - 1 - turns_count[last_num][2]
    if (last_num not in turns_count.keys()):
        turns_count[last_num] = [0,0,0]
    turns_count[last_num][0] += 1
    turns_count[last_num][2] = turns_count[last_num][1]
    turns_count[last_num][1] = turn
    turn += 1
print(last_num)

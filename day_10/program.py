import math

def calculate_combinations(count):
    variants = [format(number, '#0'+str(count+2)+'b')[2:] for number in range(0, int(math.pow(2,count)))]
    variants_sum = [max(len(y) < 3 for y in x) for x in (v.split('1') for v in variants)]
    return sum(variants_sum)

file = open('input.txt')
numbers = [int(x) for x in file.readlines()]
file.close()

previous = 0
ones = 0
threes = 0
ones_in_a_row = []
row_ones = 0

numbers.sort()

for x in numbers:
    if x - previous == 1:
        ones = ones + 1
        row_ones = row_ones + 1
    if x - previous == 3:
        if(row_ones > 1):
            ones_in_a_row.append(row_ones - 1)
        row_ones = 0
        threes = threes + 1
    if x == numbers[len(numbers) - 1] and row_ones > 1:
        ones_in_a_row.append(row_ones - 1)
    previous = x

print(ones * (threes + 1))

print(math.prod([calculate_combinations(x) for x in ones_in_a_row]))
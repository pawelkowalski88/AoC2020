file = open('input.txt')
numbers = [int(x) for x in file.readlines()]
file.close()

print(numbers)
preamble = 25


for i in range(preamble, len(numbers)):
    desired = numbers[i]
    found = False
    for x in range(i-preamble-1, i):
        for y in range(i-preamble-1, i):
            if numbers[x] + numbers[y] == desired and x != y:
                found = True
                break
        if found:
            break
    if not found:
        print(i, 'Not Found: ', desired)
        break

for x in range(0, len(numbers)):
    result = 0
    found = False
    subset = []
    for y in range(x, len(numbers)):
        result = result + numbers[y]
        subset.append(numbers[y])
        if result == desired:
            print(min(subset) + max(subset))
            found = True
            break
        if result > desired:
            break
    if found:
        break
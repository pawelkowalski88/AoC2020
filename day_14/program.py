import re
file = open('input.txt')
lines = file.readlines()
file.close()

def part_1(input, m_and, m_or, params):
    input = (int(params[1]) & m_and) | m_or
    memory[int(params[0])] = input

def part_2(input, m_and, m_or, m_x, params):
    address = int(params[0]) | (m_and & m_or)
    results = []
    for mod_address in range(int(''.join(['1' for x in m_x if x == 'X']),2)+1):
        result = [x for x in format(address, '#037b')]
        print(mod_address)
        j = 0
        for i, x in enumerate(m_x):
            if x == 'X':
                result[i] = format(mod_address, '#037b')[len(result) + 1- j]
                print('j: ',j, result, format(mod_address, '#037b')[len(result)- j])
                j += 1
        results.append(int(''.join(result),2))
        for r in results:
            print(results)

def process(instruction, params, m_and, m_or, m_x):
    if instruction == 'mask':
        m_or = int(''.join(['0' if i == 'X' or i == '0' else '1' for i in params[1]]), 2)
        m_and = int(''.join(['1' if i == 'X' or i == '1' else '0' for i in params[1]]), 2)
        m_x = ''.join(['X' if i == 'X' else '0' for i in params[1]])
    if instruction == 'mem':
        #part_1(input, mask_and, mask_or, params)
        part_2(input, mask_and, mask_or, mask_x, params)
    return m_and, m_or, m_x

memory = {}
mask_and = mask_or = mask_x = 0

instructions = [re.match(r'([^\[\]\=]+)\[?(\d*)\]? = (.+)', x).groups() for x in lines]
print(instructions)

for i in instructions:
    mask_and, mask_or, mask_x = process(i[0], i[1:3], mask_and, mask_or, mask_x)

print(sum(memory.values()))
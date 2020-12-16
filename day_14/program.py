import re, itertools
file = open('input.txt')
lines = file.readlines()
file.close()

def part_1(m_and, m_or, params):
    value = (int(params[1]) & m_and) | m_or
    memory[int(params[0])] = value

def part_2(m_and, m_or, m_x, params):
    address = int(params[0])
    helper_mask = ''.join(['0' if x == 'X' else '1' for x in m_x])
    options = [(c,) if c != 'X' else ('0', '1') for c in m_x]
    results = [x for x in (''.join(o) for o in itertools.product(*options))]
    for r in results:
        addr = address & int(helper_mask,2)
        print(r, int(r,2), addr | int(r,2))
        memory[addr | int(r,2)] = int(params[1])

def process(instruction, params, m_and, m_or, m_x):
    if instruction == 'mask':
        m_or = int(''.join(['0' if i == 'X' or i == '0' else '1' for i in params[1]]), 2)
        m_and = int(''.join(['1' if i == 'X' or i == '1' else '0' for i in params[1]]), 2)
        m_x = ''.join(['X' if i == 'X' else str(i) for i in params[1]])
    if instruction == 'mem':
        part_1(mask_and, mask_or, params)
        part_2(mask_and, mask_or, mask_x, params)
    return m_and, m_or, m_x

memory = {}
mask_and = mask_or = mask_x = 0

instructions = [re.match(r'([^\[\]\=]+)\[?(\d*)\]? = (.+)', x).groups() for x in lines]

for i in instructions:
    mask_and, mask_or, mask_x = process(i[0], i[1:3], mask_and, mask_or, mask_x)

print(sum(memory.values()))
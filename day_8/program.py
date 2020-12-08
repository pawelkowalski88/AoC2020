import re

file = open('input.txt')
lines = file.readlines()
file.close()

instructions = [re.match(r'^(\w{3}) (\+?\-?\d*)', line).groups() for line in lines]
instructions = [(code, int(val), 0) for code, val in instructions]

pointer = 0
accumulator = 0
excecuted_instructions = set()

while pointer < len(instructions):
    print(pointer, accumulator, instructions[pointer])
    if pointer in excecuted_instructions:
        print('executed instruction once again:', pointer, accumulator)
        break
    excecuted_instructions.add(pointer)
    if instructions[pointer][0] == 'nop':
        pointer = pointer + 1
        continue
    if instructions[pointer][0] == 'jmp':
        pointer = pointer + instructions[pointer][1]
        continue
    if instructions[pointer][0] == 'acc':
        accumulator = accumulator + instructions[pointer][1]
        pointer = pointer + 1
        continue
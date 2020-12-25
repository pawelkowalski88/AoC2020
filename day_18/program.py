def parse_ex(exp):
    if(len(exp) == 0):
        return ''
    level = 0
    results = []
    window = 0
    for i,c in enumerate(exp):
        if c == '(':
            level += 1
        if c == ')':
            level -= 1
        if (c == '+' or c == '*') and level == 0:
            if i != 0:
                results.append(exp[window:i].rstrip(' ').lstrip(' '))
            results.append(exp[i])
            window = i+1
    results.append(exp[window:].lstrip(' '))
    return results

def calculate2(exp):
    parsed_ex = parse_ex(exp)
    if len(parsed_ex) == 1:
        return calculate2(parsed_ex[0][1:len(parsed_ex[0])-1])
    parentheses = {i:op for i, op in enumerate(parsed_ex) if '(' in op and ')' in op}
    for p in parentheses:
        parsed_ex[p] = calculate2(parentheses[p])
    while len(parsed_ex) > 1:
        ops = {i:op for i, op in enumerate(parsed_ex) if op == '+' or op == '*'}
        ops = {k:v for k,v in sorted(ops.items(), key=lambda x: x[1], reverse=True)}
        print(ops)
        key = list(ops.keys())[0]
        result = []
        calculated = int(parsed_ex[key-1]) + int(parsed_ex[key+1]) if parsed_ex[key] == '+' else int(parsed_ex[key-1]) * int(parsed_ex[key+1])
        for x in parsed_ex[:key-1]:
            result.append(x)
        result.append(str(calculated))
        for x in parsed_ex[key+2:]:
            result.append(x)
        parsed_ex = result
    return result[0]
file = open('input.txt')
lines = file.readlines()
file.close()

e = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
print(calculate2(e))

print(sum([int(calculate2(l.rstrip('\n'))) for l in lines]))
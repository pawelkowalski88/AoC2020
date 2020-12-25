import itertools
file = open('/Users/pawelkowalski/Projects/AoC2020/day_19/input.txt')
rules, messages = file.read().split('\n\n')
rules = {int(l.split(':')[0]): l.split(':')[1].rstrip('\n').lstrip(' ') for l in rules.split('\n')}
messages = [m for m in messages.split('\n')]

def solve_rule(_r):
    rule = rules[_r]
    
    if rule == '"b"' or rule == '"a"' or rule == 'b' or rule == 'a':
        return (rule.strip('"'),)

    if '|' in rule:
        sets = [r for r in rule.split('|')]
        res = [[''.join(o) for o in itertools.product(*[solve_rule(int(r)) for r in s.split(' ') if r != ''])] for s in sets]
        return tuple([item for subl in res for item in subl])

    res = [''.join(o) for o in itertools.product(*[solve_rule(int(r)) for r in rule.split(' ') if r != ''])]
    return (res)

rule_42 = solve_rule(42)
rule_31 = solve_rule(31)

max_rule_len = 0
rules = []

print(rule_42)
print(rule_31)
step = len(rule_42[0])

results = []
for message in messages:
    next_message = False
    print(message)
    for x in range(0, len(message), step):
        part = message[x:x+step]
        print(x, part)
        if x == 0 and part not in list(rule_42):
            next_message = True
            continue
        if x + step == len(message) and part not in list(rule_31):
            next_message = True
            continue
        if part not in list(rule_42) and part not in list(rule_31):
            next_message = True
            continue
    if next_message:
        continue
    results.append(message)

print(results)
print(len(results))
print(len(messages))
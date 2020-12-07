import re
import itertools

lines = open('input.txt').readlines()

def check_values(parameter, line):
    param = list(filter(lambda p: p[0] == parameter[0], line))[0]
    for check in parameter[1]:
        if not check(param[1]):
            return False

    return True

def check_param(p, line):
    return p[0] in map(lambda x: x[0], line) and check_values(p, line)

def validate_height(x):
    val, unit = re.match(r'(\d+)(\w+)',x).groups()
    if unit == 'in':
        if 59 <= int(val) <= 76:
            return True
    if unit == 'cm':
        if 150 <= int(val) <= 193:
            return True
    return False

def validate_haircolor(x):
    val = re.match(r'(#[0-9a-f]{6}$)', x)
    if val:
        return True
    return False

desired_params = [
    ('byr', [lambda x: 1920 <= int(x) <= 2002]), 
    ('iyr', [lambda x: 2010 <= int(x) <= 2020]), 
    ('eyr', [lambda x: 2020 <= int(x) <= 2030]), 
    ('hgt', [lambda x: validate_height(x)]), 
    ('hcl', [lambda x: validate_haircolor(x)]), 
    ('ecl', [lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]]), 
    ('pid', [lambda x: True if re.match(r'(^\d{9}$)', x) else False])
]
current_params = []
lines_read = []

for line in lines:
    if line != '\n':
        for group in re.finditer(r'(\S+:\S+)', line):
            name, value = re.match(r'(\w+):(\S+)', group.group()).groups()
            current_params.append((name, value))
    else:
        lines_read.append(current_params)
        current_params = []

lines_read.append(current_params)
    
print(sum(all(check_param(p, line) for p in desired_params) for line in lines_read))
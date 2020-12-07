import re

class PasswordWithPolicy():
    def __init__(self, min, max, letter, password):
        self.min = min
        self.max = max
        self.letter = letter
        self.password = password

def read_passwords():
    return open("input.txt").readlines()

def parse(input):
    pattern = re.compile(r"()\w+")
    parsed = re.finditer(pattern, input)
    return PasswordWithPolicy(next(parsed).group(), next(parsed).group(), next(parsed).group(), next(parsed).group())

def check_valid(password):
    return ((password.password[int(password.min) - 1] == password.letter) ^ (password.password[int(password.max) - 1] == password.letter))

passwords_raw = read_passwords()
passwords = map(lambda p: parse(p), passwords_raw)
valid = 0

for p in passwords:
    if check_valid(p):
        valid = valid + 1

print(valid)
    
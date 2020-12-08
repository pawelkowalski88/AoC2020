import re

def find_bag(items, name):
    results = [bag[0] for bag in list(filter(lambda x: name in [n[1] for n in x[1]], items))]
    if len(results) > 0:
        for r in results:
            for result in find_bag(items, r):
                results.append(result)
    return set(results)

def count_bags_inside(items, name, factor):
    results = []
    for bag, kids in list(filter(lambda x: x[0] == name, items)):
        for kid in kids:
            results.append((int(factor) * int(kid[0]), kid[1]))
    
    if len(results) > 0:
        for r in results:
            for result in count_bags_inside(items, r[1], r[0]):
                results.append(result)
    
    return set(results)

file = open('input.txt')
lines = file.readlines()
file.close()

bags = [(bag, kids.split(',') if kids != 'no other bags' else []) for bag, kids in (re.match(r'(.+)s contain (.+).$', line).groups() for line in lines)]
bags = [(bag, [re.match(r'\s*(\d+) (.+ bag)s?', kid).groups() for kid in kids]) for bag, kids in bags]

print(len(find_bag(bags, 'shiny gold bag')))
print(count_bags_inside(bags, 'shiny gold bag', 1))
print(sum([bag[0] for bag in count_bags_inside(bags, 'shiny gold bag', 1)]))
import itertools, math
file = open('input.txt')
rules, your_ticket, nearby_tickets = file.read().split('\n\n')
file.close()

nearby_tickets = [x.split(',') for x in nearby_tickets.split('\n')[1:]]
rules = [tuple(r.split(':')) for r in rules.split('\n')]
rules = {k : [tuple(x.split('-')) for x in v.split('or')] for k,v in rules}
your_ticket = [int(x) for x in your_ticket.split(':')[1].split(',')]

def check_rules(_t, _rule_set):
    return any(int(a) <= int(_t) <= int(b) for a,b in _rule_set)

def check_row(_n, _valid_tickets, _rule_set):
    return all(check_rules(v[_n], _rule_set) for v in _valid_tickets)

def part1(_tickets, _rules):
    rule_set = list(itertools.chain(*_rules.values()))
    results = [[t for t in your_ticket if not check_rules(t, rule_set)] 
            for your_ticket in _tickets]
    print(sum([int(x) for x in list(itertools.chain(*results))]))

def part2(_tickets, _rules):
    rule_set = list(itertools.chain(*_rules.values()))
    valid_tickets = [t for t in _tickets if all(check_rules(v, rule_set) for v in t)]
    results = {r[0] : set([n for n in range(len(_rules)) if check_row(n, valid_tickets, r[1])]) for r in rules.items()}
    results = {k:v for k,v in sorted(results.items(), key=lambda item: len(item[1]))}

    used_rows = set()
    for r in results:
        results[r] = results[r].difference(used_rows)
        used_rows = used_rows.union(results[r])
        results[r] = list(results[r])[0]

    print(math.prod([your_ticket[results[x]] for x in results if x.find('departure') != -1]))

part1(nearby_tickets, rules)
part2(nearby_tickets, rules)
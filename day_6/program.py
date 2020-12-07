file = open('input.txt')
lines = file.readlines()
file.close()

input_answers = ''.join(lines).split('\n\n')
input_answers = [[b for b in a.split('\n')] for a in input_answers]

results = []

for answer_set in input_answers:
    print(answer_set)
    intersection_set = set(answer_set[0])
    for answer in answer_set:
        intersection_set = intersection_set.intersection(answer)
    results.append(len(intersection_set))
    # intersection_set = intersection_set.intersection(answer_set)

print(input_answers)
print(sum(results))

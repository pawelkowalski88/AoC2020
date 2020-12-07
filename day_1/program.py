file_object = open('input.txt')
input_numbers = file_object.readlines()

terminate = False
for x in input_numbers:
    for y in input_numbers:
        for z in input_numbers:
            if int(x) + int(y) + int(z) == 2020:
                print(int(x) * int(y) * int(z))
                terminate = True
                break
        if terminate:
            break
    if terminate:
        break
filename = 'input'

f = open(filename, 'r')

cont = True
total = 0
values = set()
values.add(total)

while cont:
    for line in f:
        digit = int(line[1:])
        if line[0] == '+':
            total += digit
        else:
            total -= digit

        if total in values:
            print(total)
            cont = False
            break

        values.add(total)

    f = open(filename, 'r')




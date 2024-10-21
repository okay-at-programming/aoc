before = {}

for line in open('data', 'r'):
    l = line.split()

    char = l[7]
    char2 = l[1]
    if char not in before:
        before[char] = set()
    if char2 not in before:
        before[char2] = set()

    before[char].add(char2)

started = set()
completed = set()
count = len(before.keys())
t = 0
aord = ord('A') -1

workers = [(0, 0)]*5

while len(completed) < count:

    for w in range(len(workers)):
        if workers[w][0] == 0:
            if workers[w][1] != 0:
                completed.add(workers[w][1])
                workers[w] = (0, 0)

    possible = []

    for key, value in before.items():
        if key in started:
            continue

        if value <= completed:
            possible.append(key)

    possible.sort()
    workerstring = ''

    for w in range(len(workers)):
        if workers[w][0] == 0:
            if len(possible) > 0:
                char = possible.pop(0)
                started.add(char)
                workers[w] = (60 + ord(char) - aord, char)

        if workers[w][0] > 0:
            workers[w] = (workers[w][0] - 1, workers[w][1])

        workerstring += ' ' + str(workers[w][1]) + ' '

    print(t, workerstring, completed)

    t += 1


print(t)



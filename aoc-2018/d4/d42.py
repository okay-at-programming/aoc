filename = 'data'

rows = []
for line in open(filename, 'r'):
    rows.append(line)

rows.sort()

data = {}
lastguard = None
falls = None

for line in rows:
    splitline = line.split()

    minute = int(splitline[1][3:5])

    if splitline[2] == 'Guard':
        guard = splitline[3]
        if guard not in data:
            data[guard] = []

        lastguard = guard
        falls = None

    elif splitline[2] == 'falls':
        falls = minute
    elif splitline[2] == 'wakes':
        sleep = falls, minute
        data[lastguard].append(sleep)

mostsleepguard = None
mostsleepminute = 0
mostsleep = 0

for guard, sleeps in data.items():
    hour = [0]*60
    for sleep in sleeps:
        for i in range(sleep[0], sleep[1]):
            hour[i] += 1

    top = 0
    topminute = 0
    for minute, value in enumerate(hour):
        if value > top:
            topminute = minute
            top = value

    if top > mostsleep:
        mostsleep = top
        mostsleepminute = topminute
        mostsleepguard = guard

guardid = int(mostsleepguard[1:])
print(mostsleepguard, mostsleepminute)
print(guardid*mostsleepminute)

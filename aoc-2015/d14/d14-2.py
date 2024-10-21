from dataclasses import dataclass

total_time = 2503

@dataclass
class Reindeer:
    pace: int
    time: int
    rest: int
    dist: int = 0
    points: int = 0

racers = {}

for l in open('data'):
    r = l.split()[0]
    pace, time, rest = [int(i) for i in l.split() if i.isdigit()]

    racers[r] = Reindeer(pace, time, rest)


for t in range(total_time):

    for r in racers.values():
        if t % (r.time + r.rest) < r.time:
            r.dist += r.pace

    mr = max(racers.values(), key=lambda r: r.dist)

    for r in racers.values():
        if r.dist == mr.dist:
            r.points += 1

print(max(racers.values(), key=lambda r: r.points))


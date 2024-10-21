print(sum(sorted([sum([int(h) for h in j]) for j in [f.strip().split('\n') for f in open('data').read().split('\n\n')]])[-3:]))

analysis = {'children': 3,'cats': 7,'samoyeds': 2,'pomeranians':3,'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2,'perfumes': 1}

for l in open('data'):
    s = l.find(':')
    i = l[:s].split()[1]

    m = True

    for c in l[s+1:].strip().split(','):
        k = c.split(':')[0].strip()
        v = int(c.split(':')[1].strip())

        if analysis[k] != v:
            m = False

    if m:
        print(l)




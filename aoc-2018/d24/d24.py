immune, infection = open('data').read().split('\n\n')

class group:
    def __init__(self, units,hp,immune,weakness,ad,at,initiative,name,inf):
        self.units = units
        self.hp = hp
        self.immune = set(immune)
        self.weakness = set(weakness)
        self.ad = ad
        self.at = at
        self.initiative = initiative
        self.name = name
        self.inf = inf

    def effective_power(self):
        return self.units * self.ad

    def __repr__(self):
        return repr(f'{self.name} - {self.units}')

    def calc_damage(self,ep,at):
        if at in self.immune:
            return 0
        elif at in self.weakness:
            return 2*ep
        return ep

    def damage(self,ep,at):
        cd = self.calc_damage(ep,at)
        ul = cd//self.hp
        self.units = max(self.units-ul,0)

def parse_g(l,name,inf):
    units = int(l.split()[0])
    hp = int(l.split()[4])
    if 'immune' in l:
        s = l.index('immune') + 10
        e = l.index(';',s) if ';' in l[s:] else l.index(')')
        immune = l[s:e].split(', ')
    else:
        immune = []
    if 'weak' in l:
        s = l.index('weak') + 8
        e = l.index(';',s) if ';' in l[s:] else l.index(')')
        weakness = l[s:e].split(', ')
    else:
        weakness = []
    ad = int(l.split()[-6])
    at = l.split()[-5]
    initiative = int(l.split()[-1])
    print(l,units,hp,immune,weakness,ad,at,initiative,name,inf)
    return group(units,hp,immune,weakness,ad,at,initiative,name,inf)

def sort_gs(gs):
    ngs = []
    for g in gs:
        i = 0
        while i < len(ngs):
            if g.effective_power() < ngs[i].effective_power():
                i += 1
            elif g.effective_power() == ngs[i].effective_power() and g.initiative < ngs[i].initiative:
                i += 1
            else:
                break
        ngs.insert(i,g)
    return ngs

names = {}

immg = []
i = 1
for line in immune.strip().split('\n')[1:]:
    name = f'imm-{i}'
    g = parse_g(line.strip(),name,False)
    immg.append(g)
    names[name] = g
    i += 1

i = 1
infg = []
for line in infection.strip().split('\n')[1:]:
    name = f'inf-{i}'
    g = parse_g(line.strip(),name,True)
    infg.append(g)
    names[name] = g
    i += 1

while infg and immg:

    attack = {}
    for g in sort_gs(immg + infg):
        ts = immg if g.inf else infg
        ts = [t for t in ts if t.name not in attack.values()]
        if not ts:
            continue
        b = ts[0]
        bd = b.calc_damage(g.effective_power(),g.at)
        for t in ts[1:]:
            td = t.calc_damage(g.effective_power(),g.at)
            if td < bd:
                continue
            elif td == bd and t.effective_power() < b.effective_power():
                continue
            elif td == bd and t.effective_power() == b.effective_power() and t.initiative < b.initiative:
                continue
            b = t
            bd = td
        if bd > 0:
            attack[g.name] = b.name

    print(attack)

    attack_list = [names[x] for x in attack.keys()]

    for g in sorted(attack_list, key=lambda x: -x.initiative):
        t = names[attack[g.name]]
        t.damage(g.effective_power(),g.at)
        if g.effective_power() == 0:
            print(g.name,'limp')
        if t.effective_power() == 0:
            print(t.name,'dead')

    immg = [x for x in immg if x.units > 0]
    infg = [x for x in infg if x.units > 0]

    print()
    print(immg)
    print(infg)


print(sum([x.units for x in immg]) + sum([x.units for x in infg]))








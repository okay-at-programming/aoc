
def cast_int(i):
    try:
        return i.isdigit() or int(i)
    except ValueError:
        return False

ingredients = {}

for l in open('data'):
    n = l.split()[0][:-1]
    ds = [int(i) for i in l.replace(',', '').split() if cast_int(i)]
    ingredients[n] = tuple(ds)


def value(ratios):
    total = 1
    for i in range(4):
        qual = 0
        for ingredient, spoons in ratios.items():
            qual += ingredients[ingredient][i] * spoons
        total *= max(qual,0)
    return total

def perm(ratios, left):
    if left == 0:
        return value(ratios)
    l = []
    for ingredient in ingredients.keys():
        if ingredient in ratios:
            continue
        for i in range(1,left+1):
            nratios = dict(ratios)
            nratios[ingredient] = i
            l.append(perm(nratios, left-i))
    return max(l) if l else 0

print(perm({}, 100))


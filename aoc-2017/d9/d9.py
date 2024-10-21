test = ['{}', '{{{}}}', '{{},{}}', '{{{},{},{{}}}}', '{<a>,<a>,<a>,<a>}', '{{<ab>},{<ab>},{<ab>},{<ab>}}', '{{<!!>},{<!!>},{<!!>},{<!!>}}', '{{<a!>},{<a!>},{<a!>},{<ab>}}']

data = [open('data').read().strip()]

def garb(s,i):
    i += 1
    while True:
        if s[i] == '>':
            return i
        if s[i] == '!':
            i += 1
        i += 1

def group(s, i, v, sco):
    i += 1
    while True:
        if s[i] == '{':
            i,sco = group(s,i, v+1, sco)
        if s[i] == '}':
            return i+1, sco+v
        if s[i] == '!':
            i += 2
        if s[i] == '<':
            i = garb(s,i)
        i += 1


for c in data:
    s = group(c, 0, 1, 0)
    print(c, s[1])


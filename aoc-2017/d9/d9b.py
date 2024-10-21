test = ['{<>}','{<random characters>}','{<<<<>}','{<{!>}>}','{<!!>}','{<!!!>>}','{<{o"i!a,<{i<a>}']

data = [open('data').read().strip()]

def garb(s,i, sco):
    i += 1
    while True:
        if s[i] == '>':
            return i, sco
        if s[i] == '!':
            i += 1
        else:
            sco += 1
        i += 1

def group(s, i, sco):
    i += 1
    while i < len(s):
        if s[i] == '!':
            i += 2
        if s[i] == '<':
            i, sco = garb(s,i, sco)
        i += 1
    return sco


for c in data:
    s = group(c, 0, 0)
    print(c, s)


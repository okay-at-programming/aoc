scoreboard = [int(x) for x in '37']

i = '681901'
il = len(i)
c = [int(x) for x in i]
elfa = 0
elfb = 1

while True:
    newscore = scoreboard[elfa] + scoreboard[elfb]

    if newscore > 9:
        scoreboard.append(1)

    scoreboard.append(newscore%10)

    elfa = (elfa + 1 + scoreboard[elfa])%len(scoreboard)
    elfb = (elfb + 1 + scoreboard[elfb])%len(scoreboard)

    if c == scoreboard[-il:]:
        break

    if c == scoreboard[-il-1:-1]:
        il += 1
        break

print(len(scoreboard) - il)




scoreboard = [3, 7]

i = 681901
elfa = 0
elfb = 1
while len(scoreboard) < i + 10:
    newscore = scoreboard[elfa] + scoreboard[elfb]

    scoreboard.extend([int(x) for x in str(newscore)])

    elfa = (elfa + 1 + scoreboard[elfa])%len(scoreboard)
    elfb = (elfb + 1 + scoreboard[elfb])%len(scoreboard)

print(''.join([str(x) for x in scoreboard[-10:]]))




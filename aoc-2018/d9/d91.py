class node:
    def __init__(self, val):
        self.val = val
        self.ac = None
        self.cl = None

    def __str__(self):
        return str(self.val) + ' ac: ' + str(self.ac.val) + ' cl: ' + str(self.cl.val)

    def remove(self):
        self.ac.cl, self.cl.ac = self.cl, self.ac

    def insert(self, cl):
        clcl = self.cl
        cl.ac, cl.cl = self, clcl
        self.cl, clcl.ac = cl, cl


marble = node(0)
marble.ac = marble
marble.cl = marble

marblecount = 7132000
players = [0] * 459
currentplayer = 0

nextmarble = 1

while nextmarble <= marblecount:

    if nextmarble % 23 == 0:
        marble = marble.ac.ac.ac.ac.ac.ac.ac
        players[currentplayer] += marble.val + nextmarble
        marble = marble.cl
        marble.ac.remove()
    else:
        newmarble = node(nextmarble)
        marble.cl.insert(newmarble)
        marble = newmarble

    nextmarble += 1
    currentplayer = (currentplayer + 1) % len(players)

print(max(players))

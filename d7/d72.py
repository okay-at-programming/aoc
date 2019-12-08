mprog = [3,8,1001,8,10,8,105,1,0,0,21,38,55,64,81,106,187,268,349,430,99999,3,9,101,2,9,9,1002,9,2,9,101,5,9,9,4,9,99,3,9,102,2,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,3,9,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99]

class computer:
  def __init__(self, phase, program):
    self.phase = phase
    self.prog = [i for i in program]
    self.i = 0

  def comp(self, input):
    cont = True
    output = None
    while cont:
      rule = self.prog[self.i]
      opcode = rule%100

      if opcode == 99:
        cont = False
        break

      mode = int(rule/100)
      c = mode%10
      mode = int(mode/10)
      b = mode%10
      mode = int(mode/10)
      a = mode%10
      
      res = 0
      if opcode == 1:
        val1 = self.prog[self.i+1] if c else self.prog[self.prog[self.i+1]]
        val2 = self.prog[self.i+2] if b else self.prog[self.prog[self.i+2]]
        val3 = self.i+3 if a else self.prog[self.i+3]

        res = val1 + val2
        self.prog[val3] = res
        self.i += 4
      elif opcode == 2:
        val1 = self.prog[self.i+1] if c else self.prog[self.prog[self.i+1]]
        val2 = self.prog[self.i+2] if b else self.prog[self.prog[self.i+2]]
        val3 = self.i+3 if a else self.prog[self.i+3]

        res = val1 * val2
        self.prog[val3] = res
        self.i += 4
      elif opcode == 3:
        val1 = self.i+1 if c else self.prog[self.i+1]
        if self.phase is None:
          res = input
        else:
          res = self.phase
          self.phase = None
        self.prog[val1] = res
        self.i += 2
      elif opcode == 4:
        val1 = self.i+1 if c else self.prog[self.i+1]
        output = self.prog[val1]
        self.i += 2
        return None, output
      elif opcode == 5:
        val1 = self.prog[self.i+1] if c else self.prog[self.prog[self.i+1]]
        val2 = self.prog[self.i+2] if b else self.prog[self.prog[self.i+2]]

        if val1:
          self.i = val2
        else:
          self.i += 3
      elif opcode == 6:
        val1 = self.prog[self.i+1] if c else self.prog[self.prog[self.i+1]]
        val2 = self.prog[self.i+2] if b else self.prog[self.prog[self.i+2]]

        if not val1:
          self.i = val2
        else:
          self.i += 3
      elif opcode == 7:
        val1 = self.prog[self.i+1] if c else self.prog[self.prog[self.i+1]]
        val2 = self.prog[self.i+2] if b else self.prog[self.prog[self.i+2]]
        val3 = self.i+3 if a else self.prog[self.i+3]

        self.prog[val3] = 1 if val1 < val2 else 0
        self.i += 4
      elif opcode == 8:
        val1 = self.prog[self.i+1] if c else self.prog[self.prog[self.i+1]]
        val2 = self.prog[self.i+2] if b else self.prog[self.prog[self.i+2]]
        val3 = self.i+3 if a else self.prog[self.i+3]

        self.prog[val3] = 1 if val1 == val2 else 0
        self.i += 4
    
    if output is None:
      return input, None
    return output, None

max = 0
  
def perm(curr, next, ps):
  if len(next) == 0:
    ps.append(curr)
  else:
    for i in range(len(next)):
      newlist = next[:i] + next[i+1:]
      newcurr = [j for j in curr]
      newcurr.append(next[i])
      perm(newcurr, newlist, ps)

perms = []
perm([],[5,6,7,8,9], perms)

max = 0
for ps in perms:
  comps = []
  for p in ps:
    comps.append(computer(p, mprog))

  i = 0
  val = 0
  while True:
    c = comps[i]
    val = c.comp(val)
    if val[0] is None:
      val = val[1]
    else:
      val = val[0]
      if i == 4:
        print(val)
        break
    i = (i+1)%5

  if val > max:
    max = val

print(max)

# for p in perms:
  # carry = 0
  # for i in p:
    # carry = comp(i, carry)
    # if carry > max:
      # max = carry
# print(max)
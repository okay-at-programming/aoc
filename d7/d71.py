mprog = [3,8,1001,8,10,8,105,1,0,0,21,38,55,64,81,106,187,268,349,430,99999,3,9,101,2,9,9,1002,9,2,9,101,5,9,9,4,9,99,3,9,102,2,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,3,9,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99]


def comp(phase, input):
  prog = [i for i in mprog]

  i = 0
  cont = True
  output = None
  while cont:
    rule = prog[i]
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
      val1 = prog[i+1] if c else prog[prog[i+1]]
      val2 = prog[i+2] if b else prog[prog[i+2]]
      val3 = i+3 if a else prog[i+3]

      res = val1 + val2
      prog[val3] = res
      i += 4
    elif opcode == 2:
      val1 = prog[i+1] if c else prog[prog[i+1]]
      val2 = prog[i+2] if b else prog[prog[i+2]]
      val3 = i+3 if a else prog[i+3]

      res = val1 * val2
      prog[val3] = res
      i += 4
    elif opcode == 3:
      val1 = i+1 if c else prog[i+1]
      if phase is None:
        res = input
      else:
        res = phase
        phase = None
      prog[val1] = res
      i += 2
    elif opcode == 4:
      val1 = i+1 if c else prog[i+1]
      print('output:', str(prog[val1]))
      output = prog[val1]
      i += 2
    elif opcode == 5:
      val1 = prog[i+1] if c else prog[prog[i+1]]
      val2 = prog[i+2] if b else prog[prog[i+2]]

      if val1:
        i = val2
      else:
        i += 3
    elif opcode == 6:
      val1 = prog[i+1] if c else prog[prog[i+1]]
      val2 = prog[i+2] if b else prog[prog[i+2]]

      if not val1:
        i = val2
      else:
        i += 3
    elif opcode == 7:
      val1 = prog[i+1] if c else prog[prog[i+1]]
      val2 = prog[i+2] if b else prog[prog[i+2]]
      val3 = i+3 if a else prog[i+3]

      prog[val3] = 1 if val1 < val2 else 0
      i += 4
    elif opcode == 8:
      val1 = prog[i+1] if c else prog[prog[i+1]]
      val2 = prog[i+2] if b else prog[prog[i+2]]
      val3 = i+3 if a else prog[i+3]

      prog[val3] = 1 if val1 == val2 else 0
      i += 4
  
  return output

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
perm([],[0,1,2,3,4], perms)
      
for p in perms:
  carry = 0
  for i in p:
    carry = comp(i, carry)
    if carry > max:
      max = carry
print(max)
data = open('data.txt', 'r').read().strip().split(',')
mprog = [int(i) for i in data]

class computer:
  def __init__(self, program):
    self.program = [i for i in program]
    self.i = 0
    self.base = 0
    
  def getstate(self):
    return (self.i, self.program)
  
  def withstate(self, j):
    self.i = j[0]
    self.program = [k for k in j[1]]

  def comp(self, input):
    cont = True
    output = None
    while cont:
      rule = self.program[self.i]
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
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)
        val3 = self.val(self.i+3, a)
        
        res = self.prog(val1) + self.prog(val2)
        self.set(val3, res)
        self.i += 4
      elif opcode == 2:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)
        val3 = self.val(self.i+3, a)

        res = self.prog(val1) * self.prog(val2)
        self.set(val3, res)
        self.i += 4
      elif opcode == 3:
        val1 = self.val(self.i+1, c)
        self.set(val1, input)
        self.i += 2
      elif opcode == 4:
        val1 = self.val(self.i+1, c)
        output = self.prog(val1)
        self.i += 2
        return None, output
      elif opcode == 5:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)

        if self.prog(val1):
          self.i = self.prog(val2)
        else:
          self.i += 3
      elif opcode == 6:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)

        if not self.prog(val1):
          self.i = self.prog(val2)
        else:
          self.i += 3
      elif opcode == 7:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)
        val3 = self.val(self.i+3, a)

        self.set(val3, 1 if self.prog(val1) < self.prog(val2) else 0)
        self.i += 4
      elif opcode == 8:
        val1 = self.val(self.i+1, c)
        val2 = self.val(self.i+2, b)
        val3 = self.val(self.i+3, a)

        self.set(val3, 1 if self.prog(val1) == self.prog(val2) else 0)
        self.i += 4
      elif opcode == 9:
        val1 = self.val(self.i+1, c)
        print('base')
        self.base += self.prog(val1)
        self.i += 2
    
    if output is None:
      return input, None
    return output, None
    
  def val(self, j, a):
    val = j if a == 1 else self.prog(j)
    if a == 2:
      val += self.base
    return val
    
  def prog(self, j):
    if j < 0:
      print('error')
    while len(self.program) <= j:
      self.program.append(0)
    return self.program[j]
    
  def set(self, j, k):
    if j < 0:
      print('error')
    while len(self.program) <= j:
      self.program.append(0)
    self.program[j] = k


state = None
c = computer(mprog)
queue = []
visited = set()
queue.append((0,(0,mprog),(0,0),1))
while len(queue) > 0:
  s = queue.pop(0)
  
  if s[2] in visited:
      continue
  visited.add(s[2])
  if s[3] == 2:
    print('HERE', s[0])
    state = s[1]
    break
  elif s[3] == 0:
    continue
    
  x = s[2][0]
  y = s[2][1]
  
  for d in [4,2,3,1]:
    if d == 1:
      newpos = x,y-1
    elif d == 2:
      newpos = x,y+1
    elif d == 3:
      newpos = x-1,y
    elif d == 4:
      newpos = x+1,y
    else:
      print('error')
    c.withstate(s[1])
    out = c.comp(d)
    ns = c.getstate()
    queue.append((s[0]+1,ns,newpos,out[1]))

m = 0
queue = []
visited = set()
queue.append((0,state,(0,0),1))
while len(queue) > 0:
  s = queue.pop(0)
  
  if s[2] in visited:
      continue
  visited.add(s[2])
  if s[3] == 0:
    continue
    
  if s[0] > m:
    m = s[0]
  x = s[2][0]
  y = s[2][1]
  
  for d in [4,2,3,1]:
    if d == 1:
      newpos = x,y-1
    elif d == 2:
      newpos = x,y+1
    elif d == 3:
      newpos = x-1,y
    elif d == 4:
      newpos = x+1,y
    else:
      print('error')
    c.withstate(s[1])
    out = c.comp(d)
    ns = c.getstate()
    queue.append((s[0]+1,ns,newpos,out[1]))

print(m)
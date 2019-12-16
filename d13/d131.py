data = open('data.txt', 'r').read().strip().split(',')
mprog = [int(i) for i in data]

mprog[0] = 2

class computer:
  def __init__(self, phase, program):
    self.phase = phase
    self.program = [i for i in program]
    self.i = 0
    self.base = 0

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
        if self.phase is None:
          res = input
        else:
          res = self.phase
          self.phase = None
        self.set(val1, res)
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

score = 0
out = 1,1
c = computer(None,mprog)
ballx = 0
paddlex = 0
while out[1] is not None:
  joystick = 0
  if ballx < paddlex:
    joystick = -1
  elif ballx > paddlex:
    joystick = 1
  out = c.comp(joystick)
  x = out[1]
  out = c.comp(joystick)
  y = out[1]
  out = c.comp(joystick)
  id = out[1]
  
  if x == -1 and y == 0:
    score = id
  elif id == 3:
    paddlex = x
  elif id == 4:
    ballx = x

print(' ')
print('score:', score)
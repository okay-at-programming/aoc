mprog = [3,8,1005,8,319,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,28,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,51,2,1008,18,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,77,1,1006,8,10,1006,0,88,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,106,1006,0,47,2,5,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,135,2,105,3,10,2,1101,6,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,165,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,186,1,1009,11,10,1,9,3,10,2,1003,10,10,1,107,11,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,225,1006,0,25,1,1009,14,10,1,1008,3,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,257,1,1006,2,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,284,2,1004,7,10,1006,0,41,2,1106,17,10,1,104,3,10,101,1,9,9,1007,9,919,10,1005,10,15,99,109,641,104,0,104,1,21101,0,937108545948,1,21102,1,336,0,1105,1,440,21102,1,386577203612,1,21102,347,1,0,1105,1,440,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,21478178819,1,21102,1,394,0,1106,0,440,21102,21477985447,1,1,21101,405,0,0,1105,1,440,3,10,104,0,104,0,3,10,104,0,104,0,21101,984458351460,0,1,21101,428,0,0,1106,0,440,21101,709048034148,0,1,21102,439,1,0,1106,0,440,99,109,2,21201,-1,0,1,21101,0,40,2,21101,471,0,3,21102,461,1,0,1105,1,504,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,466,467,482,4,0,1001,466,1,466,108,4,466,10,1006,10,498,1101,0,0,466,109,-2,2105,1,0,0,109,4,2101,0,-1,503,1207,-3,0,10,1006,10,521,21101,0,0,-3,22102,1,-3,1,21201,-2,0,2,21102,1,1,3,21102,540,1,0,1106,0,545,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,568,2207,-4,-2,10,1006,10,568,22101,0,-4,-4,1105,1,636,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,587,1,0,1106,0,545,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,606,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,628,22101,0,-1,1,21101,628,0,0,105,1,503,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]

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

dirs = [(0,-1),(1,0),(0,1),(-1,0)]
pointer = 0,0
dir = 0
paint = {(0,0):1}
out = 1,1
c = computer(None,mprog)
while out[1] is not None:
# for inst in [(1,0),(0,0),(1,0),(1,0),(0,1),(1,0),(1,0)]:
  out = c.comp(paint.get(pointer,0))
  newpaint = out[1]
  out = c.comp(paint.get(pointer,0))
  newdir = out[1]
  paint[pointer] = newpaint
  
  if newdir == 0:
    dir = (dir-1)%4
  else:
    dir = (dir+1)%4
  pointer = pointer[0]+dirs[dir][0],pointer[1]+dirs[dir][1]

print(paint)
  
maxx = 0
maxy = 0
minx = 0
miny = 0
for p in paint:
  if p[0] > maxx:
    maxx = p[0]
  if p[1] > maxy:
    maxy = p[1]
  if p[0] < minx:
    minx = p[0]
  if p[1] < miny:
    miny = p[1]

for i in range(miny,maxy+1):
  row = ''
  for j in range(minx,maxx+1):
    row += 'X' if paint.get((j,i), 0) == 1 else ' '
  print(row)
  
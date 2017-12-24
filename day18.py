class machine(dict):
    def __init__(self, n, lines):
        self.set('p',n)
        self.lines = lines[:]
        self.i = 0
        self.stopped = False
        self.locked = False
        self.queue = []
        self.sent = 0
    def set(self,r1,r2):
        try:    i = int(r2)
        except: i = self.get(r2)
        self[r1] = i
    def get(self,r1):
        try:    
            i = self[r1]
        except: 
            try:
                i = int(r1)
            except:
                i = 0
        return i
    def run(self,m):
        if self.locked:
            if self.queue:  
                self.locked = False
            else:           
                print("locked")
                return
        line = self.lines[self.i].strip()
        op = line[:3]
        rs = line.split(' ')[1:]
        if op == "snd":
            print("sending " + str(self.get(rs[0])))
            m.queue.append(self.get(rs[0]))
            self.sent += 1
        elif op == "set":
            self.set(rs[0],rs[1])
        elif op == "add":
            self.set(rs[0],self.get(rs[0])+self.get(rs[1]))
        elif op == "mul":
            self.set(rs[0],self.get(rs[0])*self.get(rs[1]))
        elif op == "mod":
            self.set(rs[0],self.get(rs[0])%self.get(rs[1]))
        elif op == "rcv":
            if self.queue:
                a = self.queue.pop(0)
                self.set(rs[0],a)
                print("receiving " + str(self.get(a)))
            else:
                self.locked = True
                self.i -= 1
        elif op == "jgz":
            if self.get(rs[0]) > 0:
                self.i += self.get(rs[1]) - 1
        self.i += 1
        if self.i >= len(self.lines):
            self.stopped = True

lines = open("day18.data","r").readlines()
m0 = machine(0,lines)
m1 = machine(1,lines)

while not m0.stopped or not m1.stopped:
    print("m0 running")
    m0.run(m1)
    print("m1 running")
    m1.run(m0)
    if m0.locked and m1.locked:
        break

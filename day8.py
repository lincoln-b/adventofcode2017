class Registry(object):
    def __init__(self):
        self.registers = {}
    def inc(self,x,y):
        self.registers[x] = self.get(x) + y
    def dec(self,x,y):
        self.registers[x] = self.get(x) - y
    def get(self,x):
        if x in self.registers:
            return self.registers[x]
        else:
            return 0

registry = Registry()

class Condition(object):
    def __init__(self, register="", constant=0, operator=""):
        self.register = register
        self.constant = constant
        self.operator = operator
    def isTrue(self):
        global registry
        if self.operator == "<":
            return registry.get(self.register) < self.constant
        elif self.operator == "<=":
            return registry.get(self.register) <= self.constant
        elif self.operator == "==":
            return registry.get(self.register) == self.constant
        elif self.operator == "!=":
            return registry.get(self.register) != self.constant
        elif self.operator == ">":
            return registry.get(self.register) > self.constant
        elif self.operator == ">=":
            return registry.get(self.register) >= self.constant

class Instruction(object):
    def __init__(self, condition=Condition(), register="", command="", operand=0):
        self.condition = condition
        self.register = register
        self.command = command
        self.operand = operand
    def execute(self):
        global registry
        if self.condition.isTrue():
            if self.command == "inc":
                registry.inc(self.register, self.operand)
            elif self.command == "dec":
                registry.dec(self.register, self.operand)

instructions = []
with open("day8.data") as f:
    for line in f:
        arr = line.split()
        if not arr:
            continue
        register1, command, operand, nop, register2, operator, constant = arr
        instructions.append(Instruction(Condition(register2,int(constant),operator),register1,command,int(operand)))

mostmax = 0
for instruction in instructions:
    instruction.execute()
    temp = max(registry.registers.values())
    if temp > mostmax:
        mostmax = temp


maxval = 0
maxregister = ""
for reg, val in registry.registers.iteritems():
    if val > maxval:
            maxval = val
            maxregister = reg

print "Max: " + maxregister + ": " + str(maxval)
print "Most max: " + str(mostmax)

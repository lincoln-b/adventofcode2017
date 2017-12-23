with open("day12.data", "r") as f:
    connections = [x.strip() for x in f.readlines()]

class Program(object):
    def __init__(self, id, connected):
        global programs
        self.id = int(id)
        self.connected = connected

programs = {}

for connection in connections:
    id, connected = connection.split(' <-> ')
    connected = connected.split(', ')
    programs[id] = Program(id, connected)

def getgroup(program, group):
    if program.id in group:
        return group
    group.add(program.id)
    for c in program.connected:
        group = group.union(getgroup(programs[c], group))
    return group

groups = []
for program in programs.values():
    group = getgroup(program, set())
    if group not in groups:
        groups.append(group)


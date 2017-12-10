class prog(object):
    
    name = ""
    weight = 0
    children  = []

    def __str__(self):
        return "[" + ",".join([self.name, str(self.weight), str(self.children)]) + "]"

    def __init__(self,name,weight,children):
        self.name = name
        self.weight = weight
        self.children = children

progs = []
with open("day7.data") as f:
    for line in f:
        arr = line.split()
        if not arr:
            continue
        name = arr[0]
        weight = int(arr[1][1:-1])
        children = []
        if len(arr) > 2:
            children = [x.replace(",","") for x in arr[3:]]
        progs.append(prog(name,weight,children))

for prog in progs:
    for prog2 in progs:
        if prog2.name in prog.children:
            prog.children[prog.children.index(prog2.name)] = prog2

root = [x for x in progs if x.name == 'azqje'][0]

def childw(node):
    if not node.children:
        node.childweight = 0
        return node.weight
    w = 0
    for child in node.children:
        w += childw(child)
    node.childweight = w
    return node.weight + w

childw(root)

def check(node):
    for i in range(0,len(node.children)):
        print str(i) + ": " +  node.children[i].name + "\t" + str(node.children[i].weight + node.children[i].childweight)

f = open("day11.data", "r")
directions = f.readline().strip().split(",")

class Hex(object):
    def __init__(self):
        self.is_marked = False
        self.nodes = {}
        self.x = 0
        self.y = 0
        self.z = 0
        self.nodes['n'] = None
        self.nodes['ne'] = None
        self.nodes['se'] = None
        self.nodes['s'] = None
        self.nodes['sw'] = None
        self.nodes['nw'] = None
    def direct(self, code):
        if self.nodes[code] is None:
            node = Hex()
            self.nodes[code] = node
            if code == 'n':
                node.nodes['s'] = self
                if self.nodes['nw']:
                    self.nodes['nw'].nodes['ne'] = node
                    node.nodes['sw'] = self.nodes['nw']
                if self.nodes['ne']:
                    self.nodes['ne'].nodes['nw'] = node
                    node.nodes['se'] = self.nodes['ne']
            elif code == 'ne':
                node.nodes['sw'] = self
                if self.nodes['n']:
                    self.nodes['n'].nodes['se'] = node
                    node.nodes['nw'] = self.nodes['n']
                if self.nodes['se']:
                    self.nodes['se'].nodes['n'] = node
                    node.nodes['s'] = self.nodes['se']
            elif code == 'se':
                node.nodes['nw'] = self
                if self.nodes['ne']:
                    self.nodes['ne'].nodes['s'] = node
                    node.nodes['n'] = self.nodes['ne']
                if self.nodes['s']:
                    self.nodes['s'].nodes['ne'] = node
                    node.nodes['sw'] = self.nodes['s']
            elif code == 's':
                node.nodes['n'] = self
                if self.nodes['se']:
                    self.nodes['se'].nodes['sw'] = node
                    node.nodes['ne'] = self.nodes['se']
                if self.nodes['sw']:
                    self.nodes['sw'].nodes['se'] = node
                    node.nodes['nw'] = self.nodes['sw']
            elif code == 'sw':
                node.nodes['ne'] = self
                if self.nodes['nw']:
                    self.nodes['nw'].nodes['s'] = node
                    node.nodes['n'] = self.nodes['nw']
                if self.nodes['s']:
                    self.nodes['s'].nodes['nw'] = node
                    node.nodes['se'] = self.nodes['s']
            elif code == 'nw':
                node.nodes['se'] = self
                if self.nodes['n']:
                    self.nodes['n'].nodes['sw'] = node
                    node.nodes['ne'] = self.nodes['n']
                if self.nodes['sw']:
                    self.nodes['sw'].nodes['n'] = node
                    node.nodes['s'] = self.nodes['sw']
            return node
        else:
            return self.nodes[code]

direct_x = {'n':0,'ne':1,'se':1,'s':0,'sw':-1,'nw':-1}
direct_y = {'n':1,'ne':0,'se':-1,'s':-1,'sw':0,'nw':1}
direct_z = {'n':-1,'ne':-1,'se':0,'s':1,'sw':1,'nw':0}
head = Hex()
node = head
distances = []
for code in directions:
    new_x = node.x + direct_x[code]
    new_y = node.y + direct_y[code]
    new_z = node.z + direct_z[code]
    node = node.direct(code)
    node.x = new_x
    node.y = new_y
    node.z = new_z
    distances.append((abs(node.x) + abs(node.y) + abs(node.z))/2)
tail = node
print (abs(tail.x) + abs(tail.y) + abs(tail.z))/2
print max(distances)

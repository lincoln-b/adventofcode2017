def rotate(x):
    return [list(x) for x in zip(*x[::-1])]

def flip(x):
    return x[::-1]

class Rule(object):
    def __init__(self,line):
        a,b = line.split(' => ')
        self.to_pattern = [list(x) for x in b.split('/')]
        x = [list(x) for x in a.split('/')]
        self.from_patterns = [x, rotate(x), rotate(rotate(x)), rotate(rotate(rotate(x)))]
        self.from_patterns += [flip(x) for x in self.from_patterns]
    def match(self,square):
        if square in self.from_patterns:
            return self.to_pattern
        else:
            return False

art = [['.','#','.'],['.','.','#'],['#','#','#']]
rules = []
with open('day21.data') as f:
    for line in f:
        rules.append(Rule(line.strip()))

for _ in range(18):
    if len(art) % 2 == 0:
        new_art = [[] for _ in range(len(art)*3/2)]
        for i in range(0,len(art),2):
            for j in range(0,len(art),2):
                for rule in rules:
                    out = rule.match([x[j:j+2] for x in art[i:i+2]])
                    if out:
                        for k in range(i*3/2,i*3/2+3):
                            new_art[k] += out[k-(i*3/2)]
    elif len(art) % 3 == 0:
        new_art = [[] for _ in range(len(art)*4/3)]
        for i in range(0,len(art),3):
            for j in range(0,len(art),3):
                for rule in rules:
                    out = rule.match([x[j:j+3] for x in art[i:i+3]])
                    if out:
                        for k in range(i*4/3,i*4/3+4):
                            new_art[k] += out[k-(i*4/3)]
    art = new_art

    count = 0
    for line in art:
        for pix in line:
            if pix == '#':
                count += 1
    print count

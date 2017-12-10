s = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11".split()
puz = [int(x) for x in s]

import copy

def redistribute(m):
    mem = copy.copy(m)
    i = mem.index(max(m))
    blocks = mem[i]
    mem[i] = 0
    i += 1
    while blocks > 0:
        if i >= len(mem):
            i = 0
        mem[i] += 1
        i += 1
        blocks -= 1
    return mem

def unloop(mem):
    s = [str(mem)]
    steps = 0
    while 1:
        mem = redistribute(mem)
        steps += 1
        if str(mem) in s:
            return steps - s.index(str(mem))
        s.append(str(mem))
    return steps

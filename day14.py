from copy import copy
position = 0
skip = 0
size = 256
numbers = range(size)
def hash(lengths):
    global position, skip, numbers
    for length in lengths:
        if position + length < size:
            numbers[position:position+length] = numbers[position:position+length][::-1]
        else:
            pieces = copy(numbers[position:]) + copy(numbers[:position + length - size])
            pieces.reverse()
            numbers[position:] = pieces[:size - position]
            numbers[:position + length - size] = pieces[size - position:]
        position += length + skip
        while position >= size:
            position -= size
        skip += 1

def knot(puz):
    global numbers,position,skip,size
    position = 0
    skip = 0
    numbers = range(size)
    lengths = [ord(x) for x in puz] + [17, 31, 73, 47, 23]
    for i in range(64):
        hash(lengths)
    dense = []
    for i in range(16):
        xor = numbers[i*16]
        for num in numbers[i*16 + 1:(i+1)*16]:
            xor = xor ^ num
        dense.append(xor)
    str = ""
    for i in dense:
        str += format(i,'02x')
    return str

puz = "ugkiagan-"

#puz = "flqrgnkx-"
grid = []
for i in range(128):
    hashcode = knot(puz + str(i))
    grid.append([])
    for c in hashcode:
        b = bin(int(c,16))[2:].zfill(4)
        grid[i].append(int(b[0]))
        grid[i].append(int(b[1]))
        grid[i].append(int(b[2]))
        grid[i].append(int(b[3]))

def group(i,j):
    global grid
    if i < 0 or j < 0 or i > 127 or j > 127 or grid[i][j] == 2 or grid[i][j] == 0:
        return False
    grid[i][j] = 2
    group(i-1,j)
    group(i+1,j)
    group(i,j-1)
    group(i,j+1)
    return True

numgroups = 0
for i in range(128):
    for j in range(128):
        if group(i,j):
            numgroups += 1

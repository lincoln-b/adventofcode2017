from copy import copy

# PART 1

#lengths = [183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88]
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

# PART 2

puz = "183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88"

def knot(puz):
    global numbers
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

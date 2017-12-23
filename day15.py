def gen_a(x):
    return x * 16807 % 2147483647
def gen_b(x):
    return x * 48271 % 2147483647

a = [gen_a(618)]
b = [gen_b(814)]

def bin32(x):
    return bin(x)[2:].zfill(32)

def judge():
    global a,b
    a_temp = gen_a(a[-1])
    while not a_temp % 4 == 0:
        a_temp = gen_a(a_temp)
    a.append(a_temp)
    b_temp = gen_b(b[-1])
    while not b_temp % 8 == 0:
        b_temp = gen_b(b_temp)
    b.append(b_temp)
    return bin32(a[-1])[16:] == bin32(b[-1])[16:]

count = 0
for i in range(5000000):
    if judge():
        count += 1

print count

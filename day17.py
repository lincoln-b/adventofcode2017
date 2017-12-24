buf = [0]
pos = 0
ins = 359
#for val in range(1,2018):
#    pos = (ins+pos)%len(buf)+1
#    buf.insert(pos,val)
#print buf[pos+1]
for val in range(1,50000001):
    pos = (ins+pos)%val+1
    if pos == 1:
        n = val
print n


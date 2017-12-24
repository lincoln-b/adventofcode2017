instructions = open("day16.data","r").readlines()[0].strip().split(",")
programs = list('abcdefghijklmnop')

def spin(x):
    global programs
    programs = programs[-x:] + programs[:-x]

def exchange(x,y):
    global programs
    temp = programs[x]
    programs[x] = programs[y]
    programs[y] = temp

def partner(a,b):
    global programs
    exchange(programs.index(a),programs.index(b))

def dance():
    global programs,instructions
    for instruction in instructions:
        if instruction[0] == 's':
            spin(int(instruction[1:]))
        elif instruction[0] == 'x':
            x,y = instruction[1:].split("/")
            exchange(int(x),int(y))
        elif instruction[0] == 'p':
            partner(instruction[1],instruction[3])

dance() 
count = 1
while not programs == list('abcdefghijklmnop'):
    dance()
    count += 1

print "Found cycle after dancing " + str(count) + " times."

programs = list('abcdefghijklmnop')
for i in range(1000000000 % count):
    dance()

print ''.join(programs)

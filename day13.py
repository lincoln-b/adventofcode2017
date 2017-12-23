import itertools

# copied this one from reddit. My solution worked on the first part but involved too much copying and spun for more than a day without solving the second part.

f = open("day13.data", "r")
lines = [line.split(': ') for line in f]

heights = {int(pos): int(height) for pos, height in lines}

def scanner(height, time):
    offset = time % ((height - 1) * 2)

    return 2 * (height - 1) - offset if offset > height - 1 else offset

part1 = sum(pos * heights[pos] for pos in heights if scanner(heights[pos], pos) == 0)

part2 = next(wait for wait in itertools.count() if not any(scanner(heights[pos], wait + pos) == 0 for pos in heights))


#from copy import deepcopy
#
#with open("day13.data") as f:
#    lines = f.readlines()
#layers = {}
#for line in lines:
#    d, r = [int(x) for x in line.split(": ")]
#    layers[d] = {'d': 1, 'r': [None for x in range(r)]}
#    layers[d]['r'][0] = 'S'
#layerscopy = deepcopy(layers)
#
#seconds = 0
#
#def nextsecond():
#    global layers, seconds
#    seconds += 1
#    for d in layers.keys():
#        direction = layers[d]['d']
#        i = layers[d]['r'].index('S')
#        layers[d]['r'][i] = None
#        if i == len(layers[d]['r'])-1 and direction == 1:
#            direction = -1
#        elif i == 0 and direction == -1:
#            direction = 1
#        i += direction
#        layers[d]['d'] = direction
#        layers[d]['r'][i] = 'S'
#
#def tracker():
#    global layers
#    caught = []
#    for i in range(sorted(layers.keys())[-1]+1):
#        if i in layers and layers[i]['r'][0] is not None:
#            print "caught on layer " + str(i)
#            caught.append(i*len(layers[i]['r']))
#        nextsecond()
#    return caught
#
#def stalker(s):
#    global layers, layerscopy
#    layers = deepcopy(layerscopy)
#    for i in range(s):
#        nextsecond()
#    for i in range(sorted(layers.keys())[-1]+1):
#        if i in layers and layers[i]['r'][0] is not None:
#            return False
#        nextsecond()
#    return True

#i = 0
#while True:
#    print i,
#    if stalker(i):
#        print "Got through at " + str(i)
#        break
#    i += 1

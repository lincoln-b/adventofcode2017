from collections import defaultdict

class particle(object):
    def __init__(self,dat,num):
        d = dat.split(", ")
        self.p_x,self.p_y,self.p_z = [int(x) for x in d[0][3:-1].split(",")]
        self.v_x,self.v_y,self.v_z = [int(x) for x in d[1][3:-1].split(",")]
        self.a_x,self.a_y,self.a_z = [int(x) for x in d[2][3:-1].split(",")]
        self.num = num
    def __eq__(self,other):
        return self.p_x == other.p_x and self.p_y == other.p_y and self.p_z == other.p_z
    def update(self):
        self.v_x += self.a_x
        self.v_y += self.a_y
        self.v_z += self.a_z
        self.p_x += self.v_x
        self.p_y += self.v_y
        self.p_z += self.v_z
    def distance(self):
        return abs(self.p_z) + abs(self.p_y) + abs(self.p_x)
    def key(self):
        return ",".join([str(self.p_x),str(self.p_y),str(self.p_z)])

particles = {}
with open("day20.data") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        p = particle(lines[i].strip(),i)
        particles[i] = p

for _ in range(1000):
    new_particles = defaultdict(list)
    for i,p in particles.iteritems():
        p.update()
        new_particles[p.key()].append(i)
    for k,v in new_particles.iteritems():
        if len(v) > 1:
            for i in v:
                del particles[i]

#l = len(particles)
#for _ in range(10):
#    i = 0
#    while i < range(l):
#        if particles[i].alive:
#            particles[i].update()
#            j = 0
#            while j < range(l):
#                if not i == j and particles[i].collides(particles[j]):
#                    particles[i].alive = False
#                    particles[j].alive = False
        

#min_dist = particles[0].distance()
#min_dist_i = 0
#for i in range(len(particles)):
#    if particles[i].distance() < min_dist:
#        min_dist = particles[i].distance()
#        min_dist_i = i

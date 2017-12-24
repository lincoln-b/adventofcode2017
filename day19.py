class Grid(list):
    def __getitem__(self,key):
        try:
            return super(Grid,self).__getitem__(key)
        except IndexError:
            return Grid(" ")
    def __eq__(self,other):
        if other == " " and len(self) == 1 and self[0] == " ":
            return True
        else:
            return self == other

grid = Grid([Grid(x) for x in Grid(open("day19.data","r").readlines())])
y = 0
x = grid[0].index("|")
direction = "down"
path = []
steps = 0

while True:

    steps += 1

    if direction == "down":
        y += 1
    elif direction == "up":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    
    if grid[y][x] == " ":
        break
    elif grid[y][x] == "+":
        if direction == "down" or direction == "up":
            if not grid[y][x+1] == " ":
                direction = "right"
            elif not grid[y][x-1] == " ":
                direction = "left"
        elif direction == "right" or direction == "left":
            if not grid[y+1][x] == " ":
                direction = "down"
            elif not grid[y-1][x] == " ":
                direction = "up"
    elif not grid[y][x] == "|" and not grid[y][x] == "-":
        path.append(grid[y][x])

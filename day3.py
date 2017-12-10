# PART TWO

class SpiralNode(object):
    """

    Neighbor positions are as follows:
        0 -> right
        1 -> top right
        2 -> top
        3 -> top left
        4 -> left
        5 -> bottom left
        6 -> bottom
        7 -> bottom right

    """
    def __init__(self):
        self.value = 0
        self.neighbors = [None, None, None, None, None, None, None, None]
    
    def updateValue(self):
        self.value = 0
        for neighbor in self.neighbors:
            if neighbor is not None:
                self.value = self.value + neighbor.value
    
    def setNeighbor(self, index, neighbor):
        self.neighbors[index] = neighbor


def spiral(value):
    start = SpiralNode()
    start.value = 1
    return __spiral(buildNode(start,0), 1, value).value

"""
Directions are as follows:
    0 -> right
    1 -> up
    2 -> left
    3 -> down
"""
def __spiral(lastNode, rowNumber, value):
    for i in range(2 * rowNumber - 1):
        lastNode = buildNode(lastNode,1)
        if lastNode.value > value:
            return lastNode
    for i in range(2 * rowNumber):
        lastNode = buildNode(lastNode,2)
        if lastNode.value > value:
            return lastNode
    for i in range(2 * rowNumber):
        lastNode = buildNode(lastNode,3)
        if lastNode.value > value:
            return lastNode
    for i in range(2 * rowNumber + 1):
        lastNode = buildNode(lastNode,0)
        if lastNode.value > value:
            return lastNode
    return __spiral(lastNode, rowNumber + 1, value)

def buildNode(lastNode, direction):
    newNode = SpiralNode()

    # set the node's neighbors depending on direction
    
    # right
    if direction == 0:
        lastNode.setNeighbor(0,newNode)
        # left neighbor
        newNode.setNeighbor(4,lastNode)
        # top left neighbor
        topLeft = lastNode.neighbors[2]
        if topLeft is not None:
            newNode.setNeighbor(3,lastNode.neighbors[2])
            # top neighbor
            top = topLeft.neighbors[0]
            if top is not None:
                newNode.setNeighbor(2,top)
                # top right neighbor
                topRight = top.neighbors[0]
                if topRight is not None:
                    newNode.setNeighbor(1,topRight)

    # top
    elif direction == 1:
        lastNode.setNeighbor(2,newNode)
        # bottom neighbor
        newNode.setNeighbor(6,lastNode)
        # bottom left neighbor
        bottomLeft = lastNode.neighbors[4]
        if bottomLeft is not None:
            newNode.setNeighbor(5,bottomLeft)
            # left neighbor
            left = bottomLeft.neighbors[2]
            if left is not None:
                newNode.setNeighbor(4,left)
                # top left neighbor
                topLeft = left.neighbors[2]
                if topLeft is not None:
                    newNode.setNeighbor(3,topLeft)

    # left
    elif direction == 2:
        lastNode.setNeighbor(4,newNode)
        # right neighbor
        newNode.setNeighbor(0,lastNode)
        # bottom right neighbor
        bottomRight = lastNode.neighbors[6]
        if bottomRight is not None:
            newNode.setNeighbor(7,bottomRight)
            # bottom neighbor
            bottom = bottomRight.neighbors[4]
            if bottom is not None:
                newNode.setNeighbor(6,bottom)
                # bottom left neighbor
                bottomLeft = bottom.neighbors[4]
                if bottomLeft is not None:
                    newNode.setNeighbor(5,bottomLeft)

    # down
    elif direction == 3:
        lastNode.setNeighbor(6,newNode)
        # top neighbor
        newNode.setNeighbor(2,lastNode)
        # top right neighbor
        topRight = lastNode.neighbors[0]
        if topRight is not None:
            newNode.setNeighbor(1,topRight)
            # right neighbor
            right = topRight.neighbors[6]
            if right is not None:
                newNode.setNeighbor(0,right)
                # bottom right neighbor
                bottomRight = right.neighbors[6]
                if bottomRight is not None:
                    newNode.setNeighbor(7,bottomRight)

    # check the node's value
    newNode.updateValue()
    return newNode

# PART ONE

def manhattan(x):
    row = 0
    while x > ((2*row+1)**2):
        row = row + 1
    return __manhattan(x, row)

def __manhattan(x, row):
    
    #base case
    if x == 1:
        return 0
    
    #calculate the corners and sides of this row
    lowest = (2*row-1)**2 + 1
    highest = (2*row+1)**2
    corners = [highest-6*row, highest-4*row, highest-2*row, highest]

    #recur depending on location
    
    #one above the bottom right corner
    if x == lowest:
        return 1 + __manhattan(x-1, row-1)
    #corner case
    if x in corners:
        m = (3 - corners.index(x)) * 2
        return 2 + __manhattan(x - 8*row + m, row-1)

    #right side
    if x < corners[0]:
        return 1 + __manhattan(x - 8*row + 7, row-1)
    #top side
    if x < corners[1]:
        return 1 + __manhattan(x - 8*row + 5, row-1)
    #left side
    if x < corners[2]:
        return 1 + __manhattan(x - 8*row + 3, row-1)
    #bottom side
    if x < corners[3]:
        return 1 + __manhattan(x - 8*row + 1, row-1)

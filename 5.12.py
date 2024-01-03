import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from random import choice
from itertools import product

def allQ():
    return list(product(allStates(), allActions()))

def allStates():
   return list(product(product(np.arange(n), np.arange(m)), product(np.arange(6), np.arange(6)))) 

def allActions():
    return list(product(np.arange(-1,2), np.arange(-1,2)))

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def allValidActions(i):
    velocityx, velocityy = i[0][1][1], i[0][1][0]
    return list(filter(lambda a: (0<a[0]+velocityy <= 5 and 0<=a[1]+velocityx<=5) or (0<=a[0]+velocityy<=5 and 0<a[1]+velocityx<=5)))


class environment:

    def __init__(self, dy, dx, y, x, map, startingPos):
        self.dy=dy
        self.dx=dx
        self.y=y
        self.x=x
        self.map = map
        self.startingPos = startingPos

    def state(self):
        return ((self.y, self.x), (self.dy, self.dx))        

    def move(self):
        oldY = self.y
        oldX = self.x
        self.y -= self.dy
        self.x += self.dx
        finished = self.projectedPath(oldY, oldX)
        try:
            if finished == True:
                return 1
            elif finished == False:
                self.y, self.x = raceTrack[self.y, self.x]
                return 0
        except:
            return 0

    #checks to make sure projeceted path is all within bounds
    def projectedPath(self, oldY, oldX):
        deltaX = self.dx/(self.dx+self.dy+0.0000001)
        deltaY = self.dy/(self.dx+self.dy+0.0000001)
        for i in range(self.dx+self.dy):
            oldX += deltaX
            oldY -= deltaY
            pos = raceTrack[round(oldY), round(oldX)]
            if pos == 1:
                pass
            elif pos == 2:
                return True
            elif pos in StartingPos:
                self.dy, self.dx = 0,0
                return False
            



    def Action(self, ndy, ndx):
        self.dx += ndx
        self.dy += ndy

        self.dx = clamp(self.dx, 1, 5)
        self.dy = clamp(self.dy, 1, 5)



def newStart():
    new = choice(StartingPos)
    return new

#creating a map for car
raceTrack = defaultdict(newStart)
StartingPos = []
n, m = (0, 0)
with open("IntroToRL/map.txt","r") as f:
    content = f.read()
    n = len(content.split("\n"))
    for i, line in enumerate(content.split("\n")):
        m = len(line)
        #Creating a map where ./1 is road, */2 is finnish line and 0 is starting line
        for j, c in enumerate(line):
            if c == ".":
                raceTrack[(i,j)] = 1
            elif c == "*":
                raceTrack[(i,j)] = 2
            
            elif c == "0":
                raceTrack[(i,j)] = 1
                StartingPos.append((i,j))


#filters away actions from q
def targetPolicyFilter(q, i):
    key, value = q
    if key[0] == i:
        return True
    else:
        return False

def main():
    q = {}    
    C = {}
    newq = {}
    targetPolicy = {}
    for i in allQ():
        q[i] = 0.0
        C[i] = 0.0

    for i in allStates():
        newq = {}
        for a in allActions():
            newq = q(i, a)
        








if __name__ == "__main__":
    main()
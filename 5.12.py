import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from random import choice
from itertools import product

def allStates():
   return list(product(product(np.arange(n), np.arange(m)), product(np.arange(6), np.arange(6)))) 

def allActions():
    return list(np.product(np.arange(-1,2), np.arange(-1,2)))

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

class environment:

    def __init__(self, dy, dx, y, x, map, startingPos):
        self.dy=dy
        self.dx=dx
        self.y=y
        self.x=x
        self.map = map
        self.startingPos = startingPos

        
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




def main():
    pata = environment(1, 1, 2, 23, raceTrack, StartingPos)
    pata.move()
    pata.move()
    print(allStates())
    




if __name__ == "__main__":
    main()
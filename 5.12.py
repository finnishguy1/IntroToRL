import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from random import choice

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

class environment:

    def __init__(self, dy, dx, y, x, map, startingPos):
        self.dy=dy
        self.dx=dx
        self.y=y
        self.x=x
        self.finish = False
        self.map = map
        self.startingPos = startingPos




    def isWithinBound(self):
        return True if raceTrack[(self.y, self.x)] == 1 else False

    def end(self):
        return self.finish
        
    def move(self):
        self.y -= self.dy
        self.x += self.dx
        inside = self.isWithinBound()
        print(self.y, self.x)
        if inside == True:
            print("Your in")
            return((self.y, self.x))
        elif self.x >= n and self.y <= m:
            print("you win")
        else:
            print("you lose") #reset y and x to a random starting pos, yaya



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
    pata = environment(1, 1, 0, 25, raceTrack, StartingPos)
    pata.move()
    pata.move()

    




if __name__ == "__main__":
    main()

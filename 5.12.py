import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from random import choice, randint
from itertools import product
from functools import lru_cache
@lru_cache
def allQ():
    return list(product(allStates(), allActions()))

@lru_cache
def allStates():
   return list(product(product(np.arange(n), np.arange(m)), product(np.arange(6), np.arange(6)))) 

@lru_cache
def allActions():
    return list(product(np.arange(-1,2), np.arange(-1,2)))

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def allValidActions(i):
    velocityx, velocityy = i[1][1], i[1][0]
    return list(filter(lambda a: (0<a[0]+velocityy <= 5 and 0<=a[1]+velocityx<=5) or (0<=a[0]+velocityy<=5 and 0<a[1]+velocityx<=5), allActions()))


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
            else:
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




def newStart():
    new = choice(StartingPos)
    return new

#creating a map for car
raceTrack = defaultdict(newStart)
StartingPos = []
n, m = (0, 0)
with open("map.txt","r") as f:
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

    b = {}
    for i in allStates():
        newA = []
        for a in allValidActions(i):
            newA.append(a)
        b[i] = newA
    C = {}    
    iterations = 0
    gamma = 1
    q = {}    
    newq = {}
    targetPolicy = {}
    for i in allQ():
        q[i] = 0.0
        C[i] = 0.0

    for i in allStates():
        newq = {}
        for a in allValidActions(i):
            newq[i,a] = q[i, a]
        targetPolicy[i] = max(newq, key=newq.get)[1]

    while iterations < 10000:
        y,x = StartingPos[randint(0, len(StartingPos)-1)]
        game = environment(0,0, y,x,raceTrack, StartingPos)
        G = 0
        W = 1.0
        R = -1
        #s for state, a for action and r for reward
        sar = []
        playing = True
        while playing:
            state = game.state()
            action = choice(b[state])
            game.Action(action[0], action[1])
            ret = game.move()
            sar.append((state, action, -1))
            if ret == 1:
                playing = False
        

        for val in reversed(sar):
            if W > 10000:
                break
            G = gamma*G + val[2]
            C[(val[0],val[1])] += W  
            q[(val[0],val[1])] += W/C[(val[0],val[1])] * (G-q[(val[0],val[1])])
            newq = {}
            for a in allValidActions(val[0]):
                newq[(val[0], val[1])] = q[(val[0],val[1])]
            targetPolicy[val[0]] = max(newq, key=newq.get)[1]
            if val[1] == targetPolicy[val[0]]:
                W *= len(b[state])
                print("yay")
            else:
                break

        print(iterations)
        iterations += 1 
    

    y,x = StartingPos[randint(0, len(StartingPos)-1)]
    print(y,x)
    game = environment(0,0, y,x,raceTrack, StartingPos)
    playing = True
    while playing:
        state = game.state()
        action = targetPolicy[state]
        print(state)
        print(action)
        game.Action(action[0], action[1])
        ret = game.move()
        if ret == 1:
            playing = False

    for Q in allQ():
        if Q[0][0] in StartingPos and Q[0][1] == (0,0):
            print(f"{Q} : {q[Q]} ")

        








if __name__ == "__main__":
    main()
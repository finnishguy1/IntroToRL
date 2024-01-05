import numpy as np
from typing import Tuple, List
from itertools import product


def allActions():
        l = list(product(np.arange(-1,2), np.arange(-1,2)))
        l.remove((0,0))
        return(l)


def clamp(n, maxn, minn):
        return max(min(n, maxn), minn)

class windyGrid:
        def __init__(self, height: int, width:int, y, x, goal: Tuple, wind: List):
                self.height = height
                self.width = width
                self.y, self.x = y, x
                self.startingPos = (y,x)
                self.goal = goal
                self.grid = np.array(wind)
        
        def allStates(self):
                return list(product(np.arange(0, self.height), np.arange(0, self.width)))


        def getState(self):
                return (self.y, self.x)

        def move(self, movement):
                y, x = movement
                self.y -= y
                self.x += x
                self.y = clamp(self.y , self.height-1, 0)
                self.x = clamp(self.x, self.width-1, 0)
                ret = self.win()
                if ret:
                        return 1
                self.y -= self.grid[self.x]
                self.y = clamp(self.y, self.height-1, 0)
                ret = self.win()
                if ret:
                        return 1
                else:
                        return 0

        def reset(self):
                self.y, self.x = self.startingPos

        def win(self):
                if (self.y, self.x) == self.goal:
                        return True
                else:
                        return False






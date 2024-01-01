import numpy as np
import pickle
import matplotlib.pyplot as plt


class environment:

    def __init__(self, dy, dx, y, x, map):
        self.dy=dy
        self.dx=dx
        self.y=y
        self.x=x
        self.wall = map #2d array of map, 0 for ground, 1 for wall, 2 for goal

    def clamp(n, minn, maxn):
        return max(min(maxn, n), minn)
        
    def move(self):
        self.y += self.dy
        self.x += self.dx
        print(self.y)
        try:
            self.wall[self.y][self.x]  #fix to restart to start line 
            
        
        except:
            print("not walid wallah")

    def PolicyUpdate(self, ndy, ndx):
        pass


map = np.array([[0 for i in range(10)], 
               [0 for i in range(10)],
               [0 for i in range(10)]])

def main():
    pata = environment(1, 1, 0, 0, map)
    pata.move()
    pata.move()
    print(map[0][1])




if __name__ == "__main__":
    main()

import environment
import random


def main():
        epsilon = 0.1
        alpha = 0.5
        gamma = 1
        wind = [0,0,0,1,1,1,2,2,1,0]
        q = {}
        env = environment.windyGrid(8, 10, 3,0 , (3,7), wind)
        reward = -1
        action = 0
        i= 0
        for s in env.allStates():
                for a in environment.allActions():
                        q[(s,a)] = 0
        




       

        while i < 1000:
                playing = True
                actionnr = 0
                actionlist = []
                oldstate = env.getState()

                if random.random() < epsilon:
                        action = random.choice(environment.allActions())
                        actionlist.append(action)
                else:
                        newq = {}
                        for a in environment.allActions():
                                newq[(oldstate, a)] = q[(oldstate, a)]
                        action = max(newq, key=newq.get)[1]
                        actionlist.append(action)

                
                while playing:
                        oldstate = env.getState() 
                        ret = env.move(actionlist[actionnr])
                        state = env.getState()

                        if random.random() < epsilon:
                                action = random.choice(environment.allActions())
                                actionlist.append(action)
                        else:
                                newq = {}
                                for a in environment.allActions():
                                        newq[(state, a)] = q[(state, a)]
                                action = max(newq, key=newq.get)[1]
                                actionlist.append(action)
                        
                        q[(oldstate, actionlist[actionnr])] += alpha*(-1+gamma*q[(state, actionlist[actionnr+1])]-q[oldstate, actionlist[actionnr]] )
                        actionnr += 1
                        if ret == 1:
                                playing = False
                                env.reset()
                                
                        
                i += 1
                print(i)
        
        
        playing = True
        actionnr = 0
        actionlist = []
        oldstate = env.getState()

       
        newq = {}
        for a in environment.allActions():
                newq[(oldstate, a)] = q[(oldstate, a)]
        action = max(newq, key=newq.get)[1]
        actionlist.append(action)

        
        while playing:
                oldstate = env.getState() 
                ret = env.move(actionlist[actionnr])
                state = env.getState()
                 
                newq = {}
                for a in environment.allActions():
                        newq[(state, a)] = q[(state, a)]
                action = max(newq, key=newq.get)[1]
                actionlist.append(action)
                
                q[(oldstate, actionlist[actionnr])] += alpha*(-1+gamma*q[(state, actionlist[actionnr+1])]-q[oldstate, actionlist[actionnr]] )
                actionnr += 1
                print(oldstate)
                if ret == 1:
                        playing = False


main()
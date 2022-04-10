import numpy as np
import random 
import matplotlib.pyplot as plt

start = np.array([30,30])
goal = np.array([80,60])
obstacle = np.array(([60,70], [40,60], [50,10], [70,45]))
# Functions
#####
def plot(Start, goal, obstacle):
    plt.xlabel('')
    plt.ylabel('')

    #PLotting the start point
    plt.plot(start[0], start[1], marker="o", markersize=18, markeredgecolor="Black", markerfacecolor="Black", label = 'Start')

    # Plotting the goal point
    plt.plot(goal[0], goal[1], marker="o", markersize=18, markeredgecolor="green", markerfacecolor="green", label = 'goal')
    node = [(12,8),(30,30), (47,21),(13,12),(9,14), (27,8)]
    for i in node:
        plt.plot(i[0], i[1], marker="o", markersize=18, markeredgecolor="green", markerfacecolor="pink")

    # Plotting obstacles 
    for i in obstacle:
        plt.plot(i[0], i[1], marker= 'o', markersize=35, markeredgecolor= "red", markerfacecolor = "red")
    plt.legend(loc ='upper left')    
     
    #Limits of the graph    
    plt.xlim(0,90)
    plt.ylim(0,90)
    
    return plt.show()

class RRT: 
    
    def __init__(self, start, goal, obstacle, max_length= 20, iterations =5):
        self.start = start
        self.goal = goal 
        self.obstacle = obstacle
        self.max_length = max_length
        self.iterations = iterations
        self.node_list = [start]
        self.mock_list = [start]
        self.dist_list = []
        self.plist = []
        
        
    def execute(self):
        start = np.array([30,30])
        goal = np.array([80,60])
        obstacle = np.array(([60,70], [40,60], [50,10], [70,45]))
        
        self.mock_list =[start]
        self.node_list = [start]
        self.plist = []
        for i in range(self.iterations):
            for r in range(4):
                rrt_random = rrt.rand_sample_node()
            rrt_eval = rrt.node_eval(20, start )
            rrt_coll = rrt.collision(start,self.node_list,obstacle)
            rrt_dist = rrt.distance()
            rrt_nearest = rrt.nearest_node()
          
            start = rrt_nearest
        return rrt_nearest
            
        if rrt_random == goal:
            print("Solution reached")
            print("""
            
            
            
            
            
    
            
            """)
        
           
    def rand_sample_node(self):
        self.nodex = np.random.randint(10,90, size = (1))
        self.nodey = np.random.randint(10,90, size = (1))
        self.node_list = [self.start]
        new_node = (self.nodex, self.nodey)

        NEW_NODE = np.concatenate((self.nodex, self.nodey))
        self.mock_list.append(NEW_NODE)
        
        return self.mock_list
        
  
    
    def node_eval(self, max_length, start):
        for i in range(len(self.mock_list)):
            self.crit = np.sqrt((self.mock_list[i][0]- self.mock_list[0][0])**2 + (self.mock_list[i][1] - self.mock_list[0][1])**2)
            if self.crit <= max_length:
                            print("Its fine")
                            #self.node_list.append(self.mock_list[i])
            else:
                print("Not good",self.mock_list[i])
                
               
        return self.mock_list
   
    
    def distance(self):
        #for i in self.node_list:
            for m in range(1,len(self.mock_list)):
                self.distx = (self.mock_list[m][0] - self.mock_list[0][0])**2
                self.disty = (self.mock_list[m][1] - self.mock_list[0][1])**2
                final_dist = np.sqrt(self.distx + self.disty)
                self.dist_list.append(final_dist)
               
            return self.dist_list
        
        
    def nearest_node(self):
        #min_dist = self.dist_list.index(min(dist_list))
        least_distance = self.dist_list.index(min(self.dist_list))
        print(" The new node has the index: ", least_distance + 1) 
        if least_distance<= self.max_length:
            print(' The new added node is: ', self.mock_list[least_distance ])  
        else:
            print("NAHHH")
        return self.mock_list[least_distance]
    
 
    def collision(self, node1, node2, obstacle):
        for o in obstacle:
           
           for l in self.mock_list:
                if l[0]<=o[0]+5 or l[0]>=o[0]+5:
                    self.node_list.append(l)
                    print(self.mock_list)
                    print(".........................")
                  
                 
                else:
                    print("WARNING: Collision")
                       
            
        
# Execute the algorithm 
plot = plot(start, goal, obstacle)
for f in range(10):
    rrt = RRT(start= start, goal = goal, obstacle = obstacle, max_length=20, iterations =1)
    rrt_ex = rrt.execute()

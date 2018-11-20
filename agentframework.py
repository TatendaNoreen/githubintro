#create agent class
import random

class Agent(): 

    def __init__(self, environment):
        self.environment = environment
        self.store = 0 
        self.x =random.randint(0,99)
        self.y =random.randint(0,99)
        pass

    def eat(self): # can you make it eat what is left?
       if self.environment[self.y][self.x] > 10: #eat 10 at every move
        self.environment[self.y][self.x] -= 10
        self.store += 10
    
    def move (self): #move the agents
        if random.random() < 0.5:
            self.x = ( self.x + 1) % 100
        else:
            self.x = ( self.x - 1) % 100
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100 
            
            







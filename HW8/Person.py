'''
Ryan Prashad
11/25/18
this file holds the class definition of a person

in main program:
check if person.stopped == False before moving them
call the should_stop function on the person BEFORE calling the move fuction
because you shouldnt move again if youre already out:

person.should_stop()
if person.stopped == False:
    person.move()
    
can make a list of person instances and univerese instances:
for u in universelist:
    if person.cu == u:
        #put in codes here to check for stop, rewards, and other portals
        #and also collisions 
'''
import math

class Person(object):
    '''
    
    this class takes in these parameters:
    name,radius,home_universe,x,y,dx,dy,current_universe,rewards
    
    '''
    def __init__(self, name, radius, x, y, dx, dy, home_universe, \
                 stopped = False, points = 0, reward = []):
        '''
        inits the person as per homework instructions
        '''
        self.name = name
        self.radius = radius 
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.hu = home_universe
        self.rewards = reward.copy()
        
        self.points = points
        self.cu = home_universe
        self.stopped = stopped
    
    def __str__(self):
        '''
        prints info on the current person
        '''
        return '{} of {} in universe {}\n    at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points'.format(self.name, self.hu, self.cu, self.x, self.y, self.dx, self.dy, len(self.rewards), self.points)
        
    def should_stop(self):
        '''
        checking self.stopped in the main program loop could throw 
        off the simulation setup number by +1 because you check for stopped the
        turn after the invalid move was made
        MAYBE????
        '''
        if (self.x >= 1000 or self.y >= 1000) or\
            (self.x <= 0 or self.y <= 0): # maybe need to add <= on both these lines
            self.stopped = True 
            return True
            
        if abs(self.dx) < 10 or abs(self.dy) < 10:
            self.stopped = True
            return True
        return False
    
    def move(self):
        '''
        adds dx or dy to x or y
        '''
        self.x = self.x + self.dx
        self.y = self.y + self.dy
    
    def reward_check(self, reward):
        '''
        checks if the person can pick up a single reward
        reward input is taken as a list: [x,y,points,name]
        adjusts dx and dy and adds up the points
        
        IN THE MAIN PROGRAM MAKE SURE TO POP THIS REWARD FROM THE REWARD
        LIST OF LISTS FOR THE UNIVERSE WE ITERATE THROUGH NOW
        
        returns true if a reward is found, false if not
        '''
        if math.sqrt((self.x-reward[0])**2+(self.y-reward[1])**2) <= self.radius:
            
            self.rewards.append(reward) #add to reward list of lists for person
            self.points += reward[2] #add points
            #print('alert1')
            self.dx = self.dx - (len(self.rewards) % 2) * (len(self.rewards) / 6) * self.dx
            
            self.dy = self.dy - ((len(self.rewards) + 1 ) % 2 ) * (len(self.rewards) / 6) * self.dy
            
            return True
        else:
            return False

    def portal_check(self, portal):
        '''
        input of portal (list) should be:
        from_x,from_y,to_name,to_x,to_y
        '''
        if math.sqrt((self.x - portal[0]) ** 2 + (self.y - portal[1]) ** 2)\
           <= self.radius:
            self.x = portal[3]
            self.y = portal[4]
            self.cu = portal[2]
            return True
        else:
            return False
        
    def crash(self, person1):
        '''
        takes person input as a instance of the person class, a person object!
        
        returns the rewards that need to go back as a 2-tuple of 
        lists describing the rewards (if a crash occurs)
        '''
        if math.sqrt((self.x - person1.x) ** 2 + (self.y - person1.y) ** 2)\
            <= self.radius + person1.radius:
            if len(self.rewards) > 0:
                a = self.rewards.pop(0)
                self.points -= a[2]
            else:
                a = []
            
            if len(person1.rewards) > 0:
                b = person1.rewards.pop(0)
                person1.points -= b[2]
            else:
                b = []
                            
            n = len(self.rewards)
            #print('alert2', self, '\n', person1)
            if n != 0 or len(a) != 0:             
                self.dx = -(self.dx + (n%2)* (n/6)*self.dx)
                self.dy = -(self.dy + ((n+1)%2)* (n/6)*self.dy)

            m = len(person1.rewards)
            if m != 0 or len(b) != 0:
                person1.dx = -(person1.dx + (m%2)* (m/6)*person1.dx)
                person1.dy = -(person1.dy + ((m+1)%2)* (m/6)*person1.dy)
                
            return (a,b)
        else:
            return False
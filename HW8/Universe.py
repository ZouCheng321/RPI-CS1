'''
Ryan Prashad
11/25/18
this program holds the universe class
'''

class Universe(object):
    '''
    this class holds information about seperate universes
    object is as follows:
    name(string), rewards(list of lists), portals(list of lists)
    rewards - x,y,points,name
    portals - from_x,from_y,to_name,to_x,to_y
    ^^^ from is the location of the portal in this universe
    individuals - name,radius,x,y,dx,dy
    '''
    def __init__(self, name, rew, portals, individuals):
        '''
        assign rewards portals and the name
        self.rewards is a list of lists with format:
        rewards - x,y,points,name,universename
        self.portals is a list of lists with format:
        portals - from_x,from_y,to_name,to_x,to_y
        '''
        self.name = name
        self.rew = rew
        self.portals = portals
        self.individuals = individuals
        for r in range(len(self.rew)):
            self.rew[r].append(name)
            
    def __str__(self):
        '''
        prints the universe in the correct format
        '''
        bigstring = ''
        bigstring += 'Universe: {} ({} rewards and {} portals)\n'.format\
              (self.name, len(self.rew), len(self.portals))
        
        bigstring += 'Rewards:\n'
        
        if len(self.rew) == 0:
            bigstring += 'None\n'
        else:
            for reward in self.rew:
                bigstring += 'at ({},{}) for {} points: {}\n'.format\
                      (reward[0], reward[1], reward[2], reward[3])
                
        bigstring += 'Portals:\n'
        
        if len(self.portals) == 0:
            bigstring += 'None\n'
        else:
            for portal in self.portals:
                #bigstring += 'at ({},{}) to ({},{}) in Universe {}'.\
                      #format(portal[0], portal[1] ,portal[3] ,\
                             #portal[4] ,portal[2])
                bigstring += '{}:({},{}) -> {}:({},{})\n'.\
                      format(self.name, portal[0], portal[1] ,portal[2] ,\
                             portal[3] ,portal[4])                
        return bigstring

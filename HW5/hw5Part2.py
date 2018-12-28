'''
Ryan Prashad
10/29/18
part 2 hw5, making the trainer wander in a grid
'''
import random

def move_trainer():
    '''
    This function chooses a random direction and value
    '''
    directions = ['N', 'E', 'S', 'W']
    return (random.choice(directions), random.random())
    
def throw_pokeball(num_false, num_true):
    '''
    this function chooses a random true/false
    '''
    flist = [False] * num_false
    tlist = [True] * num_true
    real = flist + tlist
    return random.choice(real)

def outofboard(size, location):
    '''
    this function returns true or false depending on if
    the trainer is out of bounds or not
    '''
    if location[0] >= (size - 1):
        return False
    elif location[0] <= 0:
        return False
    
    if location[1] >= (size - 1):
        return False
    elif location[1] <= 0:
        return False
    
    return True
    
gsize = int(input('Enter the integer grid size => '))
print(gsize)
prob = input('Enter a probability (0.0 - 1.0) => ')
print(prob)
prob = float(prob)
seed_value = 10*gsize + gsize
random.seed(seed_value)

trainer = [gsize//2, gsize//2] # horizontal,vertical
pokemon = [0,0] # [seen, captured]
turn = 1
pokelist = [3, 1] #num_false, num_true

while True:
    if outofboard(gsize, trainer) == False:
        print('Trainer left the field at turn {}, location ({}, {}).'.format\
              (turn - 1, trainer[0], trainer[1]))
        print('{} pokemon were seen, {} of which were captured.'.format\
              (pokemon[0], pokemon[1]))
        break        
    
    moves = move_trainer()
    if moves[0] == 'N':
        trainer[0] -= 1
    elif moves[0] == 'S':
        trainer[0] += 1 
    elif moves[0] == 'E':
        trainer[1] += 1
    elif moves[0] == 'W':
        trainer[1] -= 1   
        
    if moves[1] <= prob:
        print('Saw a pokemon at turn {}, location ({}, {})'.format\
              (turn, trainer[0], trainer[1]))        
        caught = throw_pokeball(pokelist[0], pokelist[1])
        if caught == True:
            print('Caught it!')
            pokelist[1] += 1
            pokemon[0] += 1 
            pokemon[1] += 1
        elif caught == False:
            print('Missed ...')
            pokemon[0] += 1
            
    turn += 1
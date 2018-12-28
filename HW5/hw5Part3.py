'''
Ryan Prashad
10/29/18
this part runs stats on the functions from part2
'''
import random

def move_trainer():
    '''
    This function chooses a random direction and value
    '''
    directions = ['N', 'E', 'S', 'W']
    #a = random.choice(directions)
    #b = random.random()
    return (random.choice(directions), random.random())
    
def throw_pokeball(num_false, num_true):
    '''
    this function chooses a random true/false
    '''
    flist = [False] * num_false
    tlist = [True] * num_true
    real = flist + tlist
    #c = random.choice(real)
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

def run_one_simulation(grid, probs):
    '''
    runs a sim and keeps track of pokemon cought on each
    space in the grid vs number seen but missed. prob = probability a pokemon
    can be seed at each turn
    will return number of turns needed to reach grid edge
    '''
    trainer = [grid//2, grid//2] # horizontal,vertical
    turn = 1
    pokelist = [3, 1] #num_false, num_true 
    
    while True:     
        if outofboard(grid, trainer) == False:
            #print('new')
            return turn - 1
        
        moves = move_trainer()
        if moves[0] == 'N':
            trainer[0] -= 1
        elif moves[0] == 'S':
            trainer[0] += 1 
        elif moves[0] == 'E':
            trainer[1] += 1
        elif moves[0] == 'W':
            trainer[1] -= 1
            
        if moves[1] <= probs:  
            caught = throw_pokeball(pokelist[0], pokelist[1])
            if caught == True:
                #print(trainer, 'caught')
                count_grid[trainer[0]][trainer[1]] += 1
                pokelist[1] += 1
            else:
                #print(trainer, 'miss')
                count_grid[trainer[0]][trainer[1]] -= 1
        turn += 1          

gsize = int(input('Enter the integer grid size => '))
print(gsize)
prob = input('Enter a probability (0.0 - 1.0) => ')
print(prob)
prob = float(prob)
sims = int(input('Enter the number of simulations to run => '))
print(sims)

seed_value = 10*gsize + gsize
random.seed(seed_value)

turns = []
count_grid = []

for i in range(gsize):
    count_grid.append( [0]*gsize )
print('')  

for x in range(sims):
    turns.append(run_one_simulation(gsize, prob))
    
for x in range(len(count_grid)):
    printstr = ''
    for y in range(len(count_grid[x])):
        printstr += ('{:5d}'.format(int(count_grid[x][y])))
    print(printstr)
 
maxs = []
mins = []
for x in count_grid:
    maxs.append(max(x))
    mins.append(min(x))

print('Average number of turns in a simulation was {:.2f}'.format\
      (sum(turns)/len(turns)))
print('Maximum number of turns was {} in simulation {}'.format\
      (max(turns), turns.index(max(turns)) + 1))
print('Minimum number of turns was {} in simulation {}'.format\
      (min(turns), turns.index(min(turns)) + 1))
print('Best net missed pokemon versus caught pokemon is {}'.format\
      (max(maxs)))
print('Worst net missed pokemon versus caught pokemon is {}'.format\
      (min(mins)))

#print(turns)
#print(count_grid)
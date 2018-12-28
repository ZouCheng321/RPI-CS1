'''
Ryan Prashad
10/29/18
part 1 of homework 5, random testing
'''
import random

def move_trainer():
    '''
    This function chooses a random direction and value
    '''
    directions = ['N', 'E', 'S', 'W']
    a = random.choice(directions)
    b = random.random()
    print('Directions: {}'.format(directions))
    print('Selected {}, value {:0.2f}'.format(a, b))
    
def throw_pokeball(num_false, num_true):
    '''
    this function chooses a random true/false
    '''
    flist = [False] * num_false
    tlist = [True] * num_true
    real = flist + tlist
    c = random.choice(real)
    print('Booleans: {}'.format(real))
    print('Selected {}'.format(c))

if __name__ == '__main__':
    grds = input('Enter the integer grid size => ')
    print(grds)
    grds = int(grds)
    fal = input('Enter the integer number of Falses => ')
    print(fal)
    fal = int(fal)
    tru = input('Enter the integer number of Trues => ')
    print(tru)
    tru = int(tru)
    seed = 11 * grds
    random.seed(seed)
    print('Setting seed to {}'.format(seed))
    move_trainer()
    move_trainer()
    move_trainer()
    move_trainer()
    move_trainer()
    throw_pokeball(fal, tru)
    throw_pokeball(fal, tru)
    throw_pokeball(fal, tru)
    throw_pokeball(fal, tru)
    throw_pokeball(fal, tru)
    
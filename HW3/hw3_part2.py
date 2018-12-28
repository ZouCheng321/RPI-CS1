'''
Ryan Prashad
10/9/18
This program moves and fights other pokemon based on user inputs
'''

def move_pokemon(pos, direction, steps):
    '''
    this function moves a tuple object based on certain params
    '''
    direction = direction.upper()
    if direction == 'N':
        a = [pos[0] - steps, pos[1]]
        if a[0] <= 0:
            a[0] =0
        return a[0], a[1] 
    elif direction == 'E':
        a = [pos[0], pos[1] + steps]
        if a[1] >= 150:
            a[1] = 150
        return a[0], a[1] 
    elif direction == 'S':
        a = [pos[0] + steps, pos[1]]
        if a[0] >= 150:
            a[0] = 150
        return a[0], a[1] 
    elif direction == 'W':
        a = [pos[0], pos[1] - steps]
        if a[1] <= 0:
            a[1] =0       
        return a[0], a[1]
    else:
        return pos[0], pos[1]
        
    
turns = input('How many turns? => ')
print(turns)
turns = int(turns)
name = input('What is the name of your pikachu? => ')
print(name)
often = input('How often do we see a Pokemon (turns)? => ')
print(often)
often = int(often)
print('')
position = (75, 75)
print('Starting simulation, turn 1 {} at {}'.format(name, position))
i = 0
turnCount = 0
b = ''
record = []

while i < turns:
    for x in range(0, often):
        b = input('What direction does {} walk? => '.format(name))
        print(b)
        b = b.upper()
        position = move_pokemon(position, b, 5)
        i += 1
    if (i % often) == 0: 
        print('Turn {}, {} at {}'.format(i, name, position))
        fight = input('What type of pokemon do you meet (W)ater, (G)round? => ')
        print(fight)
        fight = fight.upper()
        if fight == 'W':
            position = move_pokemon(position, b, 1)
            print('{} wins and moves to {}'.format(name, position))
            record.append('Win')
        elif fight == 'G':
            if b == 'N':
                position = move_pokemon(position, 'S', 10)
                print('{} runs away to {}'.format(name, position))
                record.append('Lose')
            if b == 'S':
                position = move_pokemon(position, 'N', 10)
                print('{} runs away to {}'.format(name, position))
                record.append('Lose')
            if b == 'E':
                position = move_pokemon(position, 'W', 10)
                print('{} runs away to {}'.format(name, position))
                record.append('Lose')
            if b == 'W':
                position = move_pokemon(position, 'E', 10)
                print('{} runs away to {}'.format(name, position))
                record.append('Lose')
        else:
            record.append('No Pokemon')
print('{} ends up at {}, Record: {}'.format(name, position, record))
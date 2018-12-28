'''
Ryan Prashad
10/9/18
This program validates a dart board, and then calculates the point value of a thrown dart
'''
def coterminal_converter(angle):
    '''
    this function converts angles above 360 into ones between 360 and 0
    also converts negative angles into ones between 360 and 0
    '''
    if angle > 360:
        turns = angle // 360
        return angle - (360 * turns)
    elif angle < 0:
        turns = abs(angle // 360)
        return angle + (360 * turns)
    else:
        return angle
    
def is_board_valid(config):
    '''
    This function determines if the parameters of a board are valid
    '''
    tests = 0
    
    for x in config:
        if x <= 0:
            return False
        else:
            tests += 1
            
    if config[2] < config[1]:
        return False
    else:
        tests += 1 
        
    if (config[4] - config[3]) <= config[2]:
        return False
    else:
        tests += 1
        
    if config[4] >= (config[6] - config[5]):
        return False
    else:
        tests += 1 
    
    if config[6] >= config[0]:
        return False
    else:
        tests += 1

    if tests >= 5:
        return True

def get_score(config, polar_position):
    '''
    This function determines the score of a dart thrown to the board
    '''
    wireangles = []
    shiftedlist = [4, 3, 2, 1]
    buffer = []
    done = False
    i = 9
    
    for x in range(5,21):
        buffer.append(x)
    buffer.reverse()
    shiftedlist = shiftedlist + buffer
    
    if polar_position[0] < (config[1] / 2):
        print('This throw scored 50.')
        done = True
    elif polar_position[0] < (config[2] / 2 ):
        print('This throw scored 25.')
        done = True
    elif polar_position[0] == (config[1] / 2):
        print('This throw scored 0.')
        done = True
    elif polar_position[0] == (config[2] / 2):
        print('This throw scored 0')
        done = True
    #exception handler
    for x in range (9, 352): #start iteration from beginning of 4th 'slice'
        if x == i:
            wireangles.append(x)
            i += 18
    if wireangles.count(polar_position[1]) != 0:
        print('This throw scored 0.')
        done = True
    #handles inner/outer wires for triple and double
    if (config[4] - config[3]) == polar_position[0]:
        print('This throw scored 0.')
        done = True
    elif config[4] == polar_position[0]:
        print('This throw scored 0.')
        done = True
    elif (config[6] - config[5]) == polar_position[0]:
        print('This throw scored 0.')
        done = True
    elif config[6] == polar_position[0]:
        print('This throw scored 0.')
        done = True
    #handles if position is out of board
    if polar_position[0] > config[0]:
        print('This throw scored 0.')
        done = True
    if done == False:
        if polar_position[0] > (config[4] - config[3]) and \
           polar_position[0] < config[4]:
            a = polar_position[1] // 18
            print('This throw scored {}.'.format(3 * shiftedlist[int(a)]))
        elif polar_position[0] > (config[6] - config[5]) and \
             polar_position[0] < config[6]:
            a = polar_position[1] // 18
            print('This throw scored {}.'.format(2 * shiftedlist[int(a)]))
        else:
            a = polar_position[1] // 18
            print('This throw scored {}.'.format(shiftedlist[int(a)]))
    
print('Please enter dart board parameters below.')
board_diameter = input('Board diameter => ')
print(board_diameter)
board_diameter = float(board_diameter)
inner_bulls_diameter = input('Inner bull\'s eye diameter => ')
print(inner_bulls_diameter)
inner_bulls_diameter = float(inner_bulls_diameter)
outer_bulls_diameter = input('Outer bull\'s eye diameter => ')
print(outer_bulls_diameter)
outer_bulls_diameter = float(outer_bulls_diameter)
triple_ring_width = input('Triple ring width => ')
print(triple_ring_width)
triple_ring_width = float(triple_ring_width)
triple_ring_distance = input('Distance from the center to the outside edge of\
 the triple ring => ')
print(triple_ring_distance)
triple_ring_distance = float(triple_ring_distance)
double_ring_width = input('Double ring width => ')
print(double_ring_width)
double_ring_width = float(double_ring_width)
double_ring_distance = input('Distance from the center to the outside edge of\
 the double ring => ')
print(double_ring_distance)
double_ring_distance = float(double_ring_distance)
cfg = (board_diameter, inner_bulls_diameter, outer_bulls_diameter,
       triple_ring_width, triple_ring_distance, double_ring_width,
       double_ring_distance)
radialcord = input('Enter the radial coordinate (r) of the point where the\
 dart landed => ')
print(radialcord)
radialcord = float(radialcord)
angcord = input('Enter the angular coordinate (phi) of the point where\
 the dart landed => ')
print(angcord)
angcord = coterminal_converter(float(angcord))
pos = (radialcord, angcord)

if is_board_valid(cfg):
    get_score(cfg, pos)
else: 
    print('Invalid dartboard parameter(s) specified.')
    
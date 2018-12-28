'''
Ryan Prashad
10/1/18
This program deals with components of a racing on a racetrack
'''
import track

def calculate_curve(track, speed): #returns a tuple of (distance, time), input track as the track string directly from the module
    ''' This function calculates a curve
    '''
    a = track.upper()
    b = a.count('B')
    b += a.count('E')
    b += a.count('N')
    b += a.count('D')
    
    miles = (b * 0.25)
    fractional = 1 / speed
    timeraw = miles * fractional #raw because its still in hours
    time = timeraw * 60 * 60
    return miles, time

def calculate_straight(track, speed):
    '''this function calculates the
    straight piece tuple
    '''
    c = track.upper()
    a = c.count('S')
    a += c.count('T')
    a += c.count('R')
    a += c.count('A')
    a += c.count('I')
    a += c.count('G')
    a += c.count('H')
    
    miles = (a * 0.25)
    fractional = 1 / speed
    timeraw = miles * fractional
    time = timeraw * 60 * 60
    return miles, time
    
trackselection = int(input('Select a track between 1 and {} => '.format(track.get_number_of_tracks())))
print(trackselection)
curvespd = input('Speed on curved segments (MPH) => ')
print(curvespd)
curvespd = float(curvespd)
straightspd = input('Speed on straight segments (MPH) => ')
print(straightspd)
straightspd = float(straightspd)
print('')

print('Track:', track.get_track(int(trackselection)), sep= '\n', end= '\n')

curvetuple = calculate_curve(track.get_track(trackselection), curvespd)
straighttuple = calculate_straight(track.get_track(trackselection), straightspd)

curvepercent = (curvetuple[0] / (curvetuple[0] + straighttuple[0]))
straightpercent = (straighttuple[0] / (curvetuple[0] + straighttuple[0]))

if curvetuple[0] == 0:
    agspeed = straightspd
elif straighttuple[0] == 0:
    agspeed = curvespd
else:
    #agspeed = (curvetuple[0] + straighttuple[0]) / ((curvetuple[0] / curvetuple[1]) + (straighttuple[0] / straighttuple[1]))
    agspeed = 1 / ((((1 / curvespd)) * curvepercent) + ((1 / straightspd) * straightpercent))
print('is {:.2f} miles long. You raced it in {:.2f} seconds at an average speed of {:.2f} MPH'.format(curvetuple[0] + straighttuple[0], curvetuple[1] + straighttuple[1], agspeed))

if agspeed < 60:
    print('Kind of slow.')
elif (agspeed >= 60) and (agspeed < 120):
    print('Getting there.')
else:
    print('Wow, quite the car!')
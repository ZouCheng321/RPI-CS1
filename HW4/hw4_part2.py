'''
Ryan Prashad
10/16/18
looks up zip codes and calculates things with them
'''
from hw04_util import read_zip_all
import math

def zip_by_location(zip_codes, location):
    '''
    this function returns a list of zip codes for a specific location
    '''
    
    zips = []
    for x in zip_codes:
        for y in range(3, len(x)): 
            if x[y].upper() == location[0]:
                for z in range(3, len(x)):
                    if x[z].upper() == location[1]:
                        zips.append(x[0])
                        
    a = ', '.join(zips)
    if a == '':
        return False
    else:
        return a

def location_by_zip(zip_codes, codes):
    '''
    this function returns a 5-tuple object depending on the
    zip code given
    '''
    for x in zip_codes:
        if x[0] == codes:
            return tuple(x)
    return False
    

def dist(zip_codes, zip1, zip2):
    '''
    this function finds the distance between zip codes
    '''
    place1 = []
    place2 = []
    
    for x in zip_codes:
        if x[0] == zip1:
            place1 = x
    for y in zip_codes:
        if y[0] == zip2:
            place2 = y

    if (len(place1) == 0) or (len(place2) == 0):
        return False
        
    deltlat = degrees_to_rads(place2[1]) - degrees_to_rads(place1[1])
    deltlong = degrees_to_rads(place2[2]) - degrees_to_rads(place1[2])
    
    a = ((math.sin((deltlat / 2))) ** 2) + \
        (math.cos(degrees_to_rads(place1[1])))\
         * (math.cos(degrees_to_rads(place2[1]))) * \
         ((math.sin((deltlong / 2))) ** 2)
    
    return (2 * 3959.191) * math.asin(math.sqrt(a))

def degrees_to_rads(degrees):
    '''
    this function converts degrees to rads
    '''
    return degrees * (math.pi / 180)

def degree_formatter(lat, long):
    '''
    this function formats for degrees
    '''
    south = False
    west = False
    if lat < 0:
        south = True
        lat = -1 * lat
    elif long < 0:
        west = True
        long = -1 * long
        
    latdegs = math.trunc(lat)
    longdegs = math.trunc(long)
    latdeci = lat - latdegs
    longdeci = long - longdegs
    latmins = math.trunc(latdeci * 60)
    longmins = math.trunc(longdeci * 60)
    latsecs = ((latdeci * 60) - latmins) * 60 
    longsecs = ((longdeci * 60) - longmins) * 60 
    
    if south == True and west == True:
        return ('({:03d}\xb0{}\'{:.2f}"{},{:03d}\xb0{}\'{:.2f}"{})')\
               .format(latdegs, latmins, latsecs, 'S', longdegs, \
                       longmins, longsecs, 'W')
    elif south == True and west == False:
        return ('({:03d}\xb0{}\'{:.2f}"{},{:03d}\xb0{}\'{:.2f}"{})')\
               .format(latdegs, latmins, latsecs, 'S', longdegs, \
                       longmins, longsecs, 'E')
    elif south == False and west == True:
        return ('({:03d}\xb0{}\'{:.2f}"{},{:03d}\xb0{}\'{:.2f}"{})')\
               .format(latdegs, latmins, latsecs, 'N', longdegs, \
                       longmins, longsecs, 'W')
    else:
        return ('({:03d}\xb0{}\'{:.2f}"{},{:03d}\xb0{}\'{:.2f}"{})')\
               .format(latdegs, latmins, latsecs, 'N', longdegs, \
                       longmins, longsecs, 'E')

while True:
    '''
    this main loop takes in a user input and 
    pushes it to the appropriate function
    '''
    a = input("Command ('loc', 'zip', 'dist', 'end') => ")
    print(a)
    
    if a.upper() == 'END':
        print('')
        print('Done')
        break
    
    if a.upper() == 'LOC':
        d = input('Enter a ZIP code to lookup => ')
        print(d)
        w = location_by_zip(read_zip_all(), d)
        if w == False:
            print('Invalid or unknown ZIP code\n')
        else:
            print('ZIP code {} is in {}, {}, {} county,\n\tcoordinates: {}\n'\
                  .format(d, w[3], w[4], w[5], degree_formatter(w[1], w[2])))
    elif a.upper() == 'ZIP':
        b = input('Enter a city name to lookup => ')
        print(b)
        b = b.upper()
        c = input('Enter the state name to lookup => ')
        print(c)
        c = c.upper()
        if zip_by_location(read_zip_all(), (b, c)) == False:
            print('No ZIP code found for {}, {}\n'\
                  .format(b.lower().capitalize(), c))
        else:
            print('The following ZIP code(s) found for {}, {}: {}\n'\
                  .format(b.lower().capitalize(), c, \
                          zip_by_location(read_zip_all(), (b, c))))
    elif a.upper() == 'DIST':
        e = input('Enter the first ZIP code => ')
        print(e)
        f = input('Enter the second ZIP code => ')
        print(f)
        if e == f:
            print('The distance between {} and {} is 0.00 miles\n'\
                  .format(e, f))            
        elif dist(read_zip_all(), e, f) == False:
            print('The distance between {} and {} cannot be determined\n'\
                  .format(e, f))            
        else:
            print('The distance between {} and {} is {:.2f} miles\n'\
                  .format(e, f, dist(read_zip_all(), e, f)))
    else:
        print('Invalid command, ignoring\n')
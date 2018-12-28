'''
Ryan Prashad
10/1/18
This program calculates dimensions of a lattice
'''
from math import pi, ceil

def find_volume_sphere(radius):
    '''
    this function returns a sphere radius
    '''
    return( (4 / 3) * (pi) * (radius ** 3))

def find_volume_cube(side):
    '''
    this function returns a cube volume
    '''
    return(side ** 3)

radius = input('Enter the gum ball radius (in.) => ')
print(radius)
radius = float(radius)
sales = input('Enter the weekly sales => ')
print(sales)
sales = float(sales)
print('')
totalballs = int(ceil(1.25 * sales))
onesideballs = ceil((totalballs ** (1 / 3)))
edgelength = onesideballs * (radius * 2)

print('The machine needs to hold {} gum balls along each edge.'.format(onesideballs))
print('Total edge length is {:.2f} inches.'.format(edgelength))
print('Target sales were {}, but the machine will hold {} extra gum balls.'.format(totalballs, (onesideballs ** 3) - totalballs))
print('Wasted space is {:.2f} cubic inches with the target number of gum balls,\nor {:.2f} cubic inches if you fill up the machine.'.format((find_volume_cube(edgelength)) - (totalballs * find_volume_sphere(radius)), (find_volume_cube(edgelength)) - ((onesideballs ** 3) * (find_volume_sphere(radius)))))
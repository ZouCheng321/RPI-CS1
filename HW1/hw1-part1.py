'''
Ryan Prashad
9/18/18
This program computes a lifeguard running time based on several outside factors
'''

import math

d1 = input('Enter the shortest distance from the lifeguard to water, d1 (yards) => ')
print(d1)
d2 = input('Enter the shortest distance from the swimmer to the shore, d2 (feet) => ')
print(d2)
h = input('Enter the lateral displacement between the lifeguard and the swimmer, h (yards) => ')
print(h)
v_sand = input('Enter the lifeguard\'s running speed on sand, v_sand (MPH) => ')
print(v_sand)
n = input('Enter the lifeguard\'s swimming slowdown factor, n => ')
print(n)
theta1 = input('Enter the direction of lifeguard\'s running on sand, theta1 (degrees) => ')
print(theta1)
d1 = float(d1)
d2 = float(d2)
h = float(h)
v_sand = float(v_sand)
n = float(n)
theta1 = float(theta1)


d1Feet = 3*d1

v_sandFPS=(v_sand*5280)/(3600)

v_swimFPS=(v_sand/n)

x=(d1Feet) * (math.tan(((math.pi / 180) * theta1)))

l1=math.sqrt((x ** 2)+(d1Feet ** 2))

l2=math.sqrt((((3 * h) - x) ** 2)+((d2) ** 2))

t=(l1 + (n * l2) ) / v_sandFPS

print('If the lifeguard starts by running in the direction with theta1 of {} degrees,\nthey will reach the swimmer in {} seconds'.format(round(theta1), round(t, 1)))
'''
Ryan Prashad
11/26/18
this program runs simulations with 2 supporting classes:
universe.py and person.py

simulations stops if all persons are stopped

load all universes in addition to the specified one, because the portals need
other universe instances to work ?????? not sure

The simulation ends either at 100 steps or when there is no individual left moving
'''
import json
from Universe import *
from Person import *
import math
infile = input('Input file => ').strip()
print(infile)
u = json.loads(open(infile).read())

universes = []
for c in u:
    d = list(c.keys())
    universes.append(Universe(c[d[0]], c[d[1]], c[d[2]], c[d[3]]))
    
people = []
for uni in universes:
    for p in uni.individuals:
        people.append(Person(p[0], p[1], p[2], p[3], p[4], p[5], uni.name))

print('All universes')
print('-' * 40)
for u in universes:
    print(u)
print('All individuals')
print('-' * 40)
for p in people:
    print(p)
print()
print('Start simulation')
print('-' * 40)
step = 0
stopped = []
poplist = []
laststep = 0
crashtimes = 0
while step <= 100:
    ''' 
    main program loop 
    check if person should stop, then if theyre actually stopped  before moving them!
    '''
    #step += 1 
    for universe in universes:
        for person in people:   
            #print(step, person.name, person.stopped, 'stopcheck')
            if person.stopped == False and person.should_stop():
                stopped.append(person)
                print('{} stopped at simulation step {} at location ({:.1f},{:.1f})\n'.\
                      format(person.name, step, person.x, person.y))
                
    if len(stopped) == len(people):
        break            
                
    for universe in universes:
        for person in people:
            if person.cu == universe.name and person.stopped == False:
                person.move()
    step += 1            
                
    for universe in universes:
        for person in people:           
            #print(step, person.name, person.stopped, 'rewardcheck')
            if person.cu == universe.name and person.stopped == False:
                for r in universe.rew:
                    if person.reward_check(r):
                        print('{} picked up "{}" at simulation step {}'.\
                              format(person.name, r[3], step))
                        universe.rew.remove(r) #removes from universe and gives to person
                        print(str(person) + '\n')
                        #print(person.name)
                        #print(person.should_stop(), person.dx, person.dy, person.name)
                        if person.should_stop():
                            stopped.append(person)
                            print('{} stopped at simulation step {} at location ({:.1f},{:.1f})\n'.format(person.name, step, person.x, person.y))
                            
                        
    for universe in universes:
        for person in people:               
            for p in people:
                #print(step, person.name, p.name, math.sqrt((p.x - person.x) ** 2 + (p.y - person.y) ** 2) <= p.radius + person.radius, p.name != person.name, p.cu == person.cu, laststep != step)
                if p.name != person.name and p.cu == person.cu and laststep != step:
                    a = person.crash(p)
                    if a != False:
                        print('{} and {} crashed at simulation step {} in universe {}'.format(person.name, p.name, step, p.cu))
                        for z in universes:
                            if len(a[0]) > 0 and z.name == a[0][4]:
                                print('{} dropped "{}", reward returned to {} at ({},{})'.format(person.name, a[0][3], z.name, a[0][0], a[0][1]))
                                z.rew.append(a[0])
                                
                            if len(a[1]) > 0 and z.name == a[1][4]:
                                print('{} dropped "{}", reward returned to {} at ({},{})'.format(p.name, a[1][3], z.name, a[1][0], a[1][1]))
                                z.rew.append(a[1])
                        print(person)
                        print(p)
                        print()
                        laststep = step #only allows crash to occur once per step, fix it so that a crash can occur some multiple times per step!
                            
    for universe in universes:
        for person in people:                   
            for portal in universe.portals:
                if person.portal_check(portal):
                    print('{} passed through a portal at simulation step {}'.format(person.name, step))
                    print(str(person) + '\n')
                        
    if len(stopped) == len(people):
        break
    #step += 1
print()
print('-' * 40)
print('Simulation stopped at step {}'.format(step))
inter = set(people).difference(set(stopped))
b = ''
if len(inter) == 0:
    print('0 individuals still moving')
else:
    for x in list(inter):
        b += '{} individuals still moving: '.format(len(inter))
        b += '{} '.format(x)
print('Winners:')
winnerdict = dict()
winner = []
for pe in people:
    winnerdict[pe] = pe.points
    #print(winnerdict)
maxval = max(list(winnerdict.values()))
#for value in winnerdict.values():
    #if value == max(list(winnerdict.values())):
        #winner.append(list(winnerdict.keys())[list(winnerdict.values()).index(value)])
for j in people:
    if j.points == maxval:
        winner.append(j)
        
for x in winner:
    print(x)
    rewardstring = 'Rewards:\n'
    for r in x.rewards:
        rewardstring += '    {}\n'.format(r[3])
    print(rewardstring)


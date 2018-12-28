'''
Ryan Prashad
11/8/18
this program compares beasts in different harry potter titles
'''
import textwrap #join the list this returns with newlines!

while True:
    title = input('Enter a title (stop to end) => ').strip()
    print(title)
    if title.upper() == 'STOP':
        break
    print('')
    title = title.upper()
    words = []
    titles = []
    buffer = []
    f = open('titles.txt') #no user iunput for file???
    for line in f: #put the title in an ordered list, and the beasts in a set
        line = line.strip()
        words.append(set(line.split('|')))
        titles.append(line.split('|')[0])
    for x in range(len(words)): #remove title from set of beasts
        words[x].remove(titles[x])
    setnum = -1
    for x in range(len(titles)):
        if titles[x].upper().find(title) != -1:
            setnum = x
            break
    if setnum == -1:
        print('This title is not found!')
        print('')
        continue
    #print(titles)
    print('Found the following title: {}'.format(titles[setnum]))
    
    beastsintitle = 'Beasts in this title: '
    beastsintitle += ', '.join(sorted(words[setnum]))
    lines = textwrap.wrap(beastsintitle)
    beastsintitle2 = '\n'.join(lines)
    print(beastsintitle2)
    print('')
    
    othertitles = []
    for x in range(len(words)):
        if x != setnum:
            if len(words[x] & words[setnum]) != 0:
                othertitles.append(titles[x])    
    newstr = 'Other titles containing beasts in common: '
    newstr += ', '.join(sorted(othertitles))
    lines2 = textwrap.wrap(newstr)
    newstr2 = '\n'.join(lines2)
    print(newstr2)
    print('')
        
    bigset = set()
    for j in range(len(words)):
        if j != setnum:
            for k in range(len(words[j])):
                words[j] = list(words[j])
                bigset.add(words[j][k])
    onlyinhere = set()  
    onlyinhere = words[setnum] - bigset #difference of this and all beasts
    littlestr = 'Beasts appearing only in this title: '
    littlestr += ', '.join(sorted(onlyinhere))
    lines3 = textwrap.wrap(littlestr)
    newstr3 = '\n'.join(lines3)
    print(newstr3)
    print('')
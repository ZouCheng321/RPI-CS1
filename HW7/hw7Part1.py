'''
Ryan Prashad
11/13/18
this program will autocorrect a word with drop [insert], swap, or replace
'''
def match(word):
    '''
    this function checks to see if a word given is already in the dictionary
    '''
    '''
    wordset = set()
    wordset.add(word)
    matches = wordset & dictfile
    '''
    if word in dictfreq:
        return word
    else:
        return set()
    '''
    if len(matches) == 0:
        return set()
    else:
        return min(matches)
    '''
def drop(word):
    '''
    this function tries dropping a letter from the word
    returns false if drop doesnt work
    returns the word if drop worked
    this function assumes dictionary is named 'dictfile' in the main program body
    it also assumes 'workfile' is the file of inputs
    BOTH ARE ASSUMED TO BE PARSED ALREADY!!
    
    hw7 update: also includes the insert function, written mainly as a case
    of matches being an empty set which means drop did NOT find anything.
    if drop finds something, insert is therefore bypassed.
    '''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm',\
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']
    
    possiblewords = set()
    hi = 100 
    lo = 100
    for y in range(len(word)):
        if word.count(word[y]) > 1:
            hi = word.rindex(word[y])
            lo = word.index(word[y])
            firstbithi = word[0:hi]
            secondbithi = word[hi + 1::]
            possiblewords.add(word[0:lo] + word[lo + 1::])
            possiblewords.add(word[0:hi] + word[hi + 1::])  
            
    for x in range(len(word)):
        if word.index(word[x]) == hi or word.index(word[x]) == lo:
            continue
        else:
            possiblewords.add(word.replace(word[x], '', 1))
    
    matches = possiblewords & dictfile
    
    posswords = set()
    for z in range(len(word) + 1):
        for c in range(len(letters)):
            new = list(word)
            new.insert(z, letters[c])
            string = ''
            for letter in new:
                string += letter
            posswords.add(string)
    #print(posswords)
    newmatch = posswords & dictfile
    
    matches.update(newmatch)
    
    if len(matches) == 0:
        '''
        for z in range(len(word) + 1):
            for c in range(len(letters)):
                new = list(word)
                new.insert(z, letters[c])
                string = ''
                for letter in new:
                    string += letter
                posswords.add(string)
        print(posswords)
        newmatch = posswords & dictfile
        if len(newmatch) == 0:
            return set()
        else:
            return newmatch
        '''
        return set()
    else:
        return matches
    
def swap(word):
    '''
    swaps 2 consecutive letters in a word and checks to see if its in the
    given dictionary file
    '''
    possiblewords = set()
    for x in range(len(word) - 1): #subtract one because lastbit will throw index error
        repstr = word[x + 1] + word[x]
        firstbit = word[0:x]
        lastbit = word[x + 2::]
        possiblewords.add(firstbit + repstr + lastbit)
    
    matches = possiblewords & dictfile
                
    if len(matches) == 0:
        return set()
    else:
        return matches

def replace(word):
    '''
    replace each letter in the word with each letter
    in the provided keyboard file
    '''
    possiblewords = set()
    for x in range(len(word)):
        new = list(word)
        for key in replets.keys():
            #print(key)
            #print(new[x])
            if new[x] == key:
                for y in replets[key]:
                    m = new.copy()
                    m[x] = y
                    string = ''
                    for letter in m:
                        string += letter
                    possiblewords.add(string)
    matches = possiblewords & dictfile
    if len(matches) == 0:
        return set()
    else:
        return matches

dictname = input('Dictionary file => ').strip()
print(dictname)
infile = input('Input file => ').strip()
print(infile)
keyfile = input('Keyboard file => ').strip()
print(keyfile)
dictfile = set()
dictfreq = dict()
replets = dict()
workfile = []
d = open(dictname)
e = open(infile)
f = open(keyfile)

for line in d:
    dictfile.add(line.strip().split(',')[0])
    l = line.strip().split(',')
    dictfreq[l[0]] = float(l[1])
#print(dictfreq)
for lin in e:
    workfile.append(lin.strip())

for li in f:
    k = li.strip().split(' ')
    j = k.pop(0)
    replets[j] = k 

 
for wrd in workfile:
    a = match(wrd)
    b = list(drop(wrd))
    c = list(swap(wrd))
    d = list(replace(wrd))
    
    if len(a) != 0:
        print('{:15s} -> {:15s} :FOUND'.format(wrd, wrd))
        continue
    
    biglist = []
    for x in range(len(b)):
        biglist.append(b[x])
    for x in range(len(c)):
        biglist.append(c[x])
    for x in range(len(d)):
        biglist.append(d[x])
    if len(biglist) == 0:
        print('{:15s} -> {:15s} :NO MATCH'.format(wrd, wrd))
        continue
    elif len(biglist) == 1:
        print('{:15s} -> {!s:15s} :MATCH 1'.format(wrd, biglist[0]))
        continue
    
    vals = dict()
    for w in biglist:
        vals[dictfreq[w]] = w
        
    if len(biglist) == 2:
        a = max(vals.keys())
        b = min(vals.keys())
        print('{:15s} -> {:15s} :MATCH 1'.format(wrd, vals[a]))
        print('{:15s} -> {:15s} :MATCH 2'.format(wrd, vals[b]))
        continue
    
    maxlist = sorted(list(vals.keys()))
    print('{:15s} -> {:15s} :MATCH 1'.format(wrd, vals[maxlist[-1]]))
    print('{:15s} -> {:15s} :MATCH 2'.format(wrd, vals[maxlist[-2]]))
    print('{:15s} -> {:15s} :MATCH 3'.format(wrd, vals[maxlist[-3]])) 
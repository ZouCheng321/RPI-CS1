'''
Ryan Prashad
11/8/18
this program will autocorrect a word with drop, swap, or replace
'''
def match(word):
    '''
    this function checks to see if a word given is already in the dictionary
    '''
    wordset = set()
    wordset.add(word)
    matches = wordset & dictfile
    
    if len(matches) == 0:
        return False
    else:
        return min(matches)

def drop(word):
    '''
    this function tries dropping a letter from the word
    returns false if drop doesnt work
    returns the word if drop worked
    this function assumes dictionary is named 'dictfile' in the main program body
    it also assumes 'workfile' is the file of inputs
    BOTH ARE ASSUMED TO BE PARSED ALREADY!!
    
    '''
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
    
    if len(matches) == 0:
        return False
    else:
        return min(matches)
    
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
        return False
    else:
        return min(matches)

def replace(word):
    '''
    replace each letter in the word with each letter in the alphabet
    '''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm',\
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']
    #hi = 0 
    #lo = 
    hi = []
    lo = []
    hiwords = []
    lowords = []
    wordindex = []
    for z in range(len(word)):
        if word.count(word[z]) > 1 and (z not in hi):
            #hi = word.rindex(word[z])
            #lo = word.index(word[z])
            hi.append(word.rindex(word[z]))
            lo.append(word.index(word[z]))
            wordindex.append(z)
    for g in range(len(hi)):
        hiwords.append(word[0:hi[g]] + '.' + word[hi[g] + 1::])
    for h in range(len(lo)):
        lowords.append(word[0:lo[h]] + '.' + word[lo[h] + 1::])
    
    #hiword = word[0:hi] + '.' + word[hi + 1::] 
    #loword = word[0:lo] + '.' + word[lo + 1::]  
    #print(hiwords)
    #print(lowords)
    possiblewords = set()
    for k in range(len(hi)):
        for y in range(len(letters)):
            possiblewords.add(hiwords[k].replace('.', letters[y], 1))
    for k in range(len(lo)):
        for y in range(len(letters)):
            possiblewords.add(lowords[k].replace('.', letters[y], 1))
            
    for x in range(len(word)):
        for y in range(len(letters)):
            if word.count(word[x]) > 1:
                #possiblewords.add(hiword.replace('.', letters[y], 1))
                #possiblewords.add(loword.replace('.', letters[y], 1))
                continue
            else:
                possiblewords.add(word.replace(word[x], letters[y], 1))   
    #print(sorted(possiblewords))
    #print(dictfile)
    matches = possiblewords & dictfile
    
    if len(matches) == 0:
        return False
    else:
        return min(matches)
    
dictname = input('Dictionary file => ').strip()
print(dictname)
infile = input('Input file => ').strip()
print(infile)

dictfile = set()
workfile = []
d = open(dictname)
e = open(infile)
for line in d:
    dictfile.add(line.strip())
    
for lin in e:
    workfile.append(lin.strip())

for wrd in workfile:
    a = match(wrd)
    b = drop(wrd)
    c = swap(wrd)
    d = replace(wrd)
    if a == wrd:
        print('{:15s} -> {:15s} :FOUND'.format(wrd, wrd))
    elif b != False:
        print('{:15s} -> {:15s} :DROP'.format(wrd, b))
    elif c != False:
        print('{:15s} -> {:15s} :SWAP'.format(wrd, c))
    elif d != False:
        print('{:15s} -> {:15s} :REPLACE'.format(wrd, d))
    elif ((a == False) and (b == False)) and ((c == False) and (d == False)):
        print('{:15s} -> {:15s} :NO MATCH'.format(wrd, wrd))
        
'''
Ryan Prashad
11/14/18
this program analyzes json files and gets info from them
'''
import json

movies = json.loads(open('movies.json').read())
ratings = json.loads(open('ratings.json').read())

minyr = input('Min year => ').strip()
print(minyr)
minyr = int(minyr)
maxyr = input('Max year => ').strip()
print(maxyr)
maxyr = int(maxyr)
imweight = input('Weight for IMDB => ').strip()
print(imweight)
imweight = float(imweight)
twitweight = input('Weight for Twitter => ').strip()
print(twitweight)
twitweight = float(twitweight)
print()
calcweight = dict() # movieid:calculated rating
for key in movies.keys():
    if movies[key]['movie_year'] >= minyr and movies[key]['movie_year'] <= maxyr:
        if (key in ratings.keys()) and (len(ratings[key]) >= 3):
            imdb_rating = movies[key]['rating']
            averagetwitter = sum(ratings[key]) / len(ratings[key])
            c = (imweight * imdb_rating + twitweight * averagetwitter) / (imweight + twitweight)
            calcweight[key] = c

while True:
    #calcweight = dict() # movieid:calculated rating
    g = input('What genre do you want to see? ').strip()
    print(g)
    if g.upper() == 'STOP':
        break
    print()
    
    #goodkeys = []
    #for key in movies.keys():
        #if movies[key]['movie_year'] >= minyr and \
           #movies[key]['movie_year'] <= maxyr:
            #if g.title() in movies[key]['genre']:
                #goodkeys.append(key)
    goodkeys = []
    for key in calcweight.keys():
        #if movies[key]['movie_year'] >= minyr and \
           #movies[key]['movie_year'] <= maxyr:
        if g.title() in movies[key]['genre']:
            goodkeys.append(key)
                
    if len(goodkeys) == 0:
        print('No {} movie found in {} through {}'.format(\
            g.title(), minyr, maxyr))
        print()
        continue
        
    #for z in range(len(goodkeys)):
        #if goodkeys[z] not in ratings.keys():
            #continue
        #if len(goodkeys[z]) < 3: #may need to change to <= 3
            #continue 
        
        #imdb_rating = movies[goodkeys[z]]['rating']
        #average_twitter_rating = sum(ratings[goodkeys[z]]) / len(ratings[goodkeys[z]])
        #calcrate = ((imweight * imdb_rating) + (twitweight * average_twitter_rating)) / (imweight + twitweight)
        #calcweight[calcrate] = goodkeys[z]
        
    #maxs = list(calcweight.values()).index(sorted(calcweight.values())[0], reverse=True)
    #mins = list(calcweight.values()).index(sorted(calcweight.values())[0])
    #maxid = list(calcweight.keys())[maxs]
    #minid = list(calcweight.keys())[mins]
    narrowdict = dict()
    for key in goodkeys:
        narrowdict[calcweight[key]] = key
    maxid = sorted(narrowdict.keys(), reverse=True)[0]
    minid = sorted(narrowdict.keys())[0]
    print('Best:')
    print('\tReleased in {}, {} has a rating of {:.2f}'.format(\
        movies[narrowdict[maxid]]['movie_year'], \
        movies[narrowdict[maxid]]['name'], maxid))
    print()
    print('Worst:')
    print('\tReleased in {}, {} has a rating of {:.2f}'.format(\
        movies[narrowdict[minid]]['movie_year'], \
        movies[narrowdict[minid]]['name'], minid))
    print()
'''
Ryan Prashad
9/18/2018
This program imports and uses string operations to manipulate substrings of the constitution.
'''
import constitution
#fix constitution---------------------------------------
constitutionFixed = constitution.get_all_text().replace('@', ' ').replace('#', '\n\n').replace('^', '\n')
linecount = constitutionFixed.count('\n')

#stars at beginning and end-----------------------------------
averagelinecount = (len(constitutionFixed)- linecount) / (linecount + 1)
#don't include newlines, add 1 to linecount for very first line that doesnt start with \n
print('*' * int(round(averagelinecount)))
print(constitutionFixed)
print('*' * int(round(averagelinecount)))

#count articles and sections--------------------------------------------
articles = constitutionFixed.count('Article.') + 1#there is a typo in the constitution file, on article III it says 'Article III.' not 'Article. III.'
sections = constitutionFixed.count('Section.')
print('\nThere are {} articles and {} sections in the United States Constitution'.format(articles, sections))
print('')
#Text of Article 1----------------------------------------------------
art1start = constitutionFixed.find('Article. I.\n\n')+len('Article. I.\n\n')
art1end = constitutionFixed.find('\n\nArticle. II.')-1 #-1 to compensate for char before newline
article1substring = constitution.substring(constitutionFixed, art1start, art1end - (art1start - 1))#substring is (string,start,count) not (string,start,end)!
art1split = article1substring.split()

#print(article1substring)
#print(art1split)

print('Text of Article I starts at position {} (character \'{}\') with the word "{}"'.format(art1start, constitutionFixed[art1start], str(art1split[0])))
print('Text of Article I ends at position {} (character \'{}\') with the word "{}"'.format(art1end, constitutionFixed[art1end], str(art1split[len(art1split) - 1])))
print('')
#find and count word-------------------------------------------------------
uppercaseConstitution=constitutionFixed.upper()
wordFind = input('Enter the word to count in the Constitution => ')
print(wordFind)
print('Word "{}" appears {} times (without regard to case) in the text of the United States Constitution'.format(wordFind.upper(), uppercaseConstitution.count(wordFind.upper())))
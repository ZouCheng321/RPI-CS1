'''
Ryan Prashad
9/19/18
This program creates a grid of stars
'''
import math

 
word=input('Word => ')
print(word)
cols=int(input('#columns => '))
print(cols)
rows=int(input('#rows => '))
print(rows)
print('Your word is: {}'.format(word))
print('')
stars='*** '
finalcols = (stars*cols).rstrip(' ')
printrows = ((finalcols+'\n')*rows)
print('(a)')
print(printrows)
#-----------------------
cs1row=rows/2
cs1col=cols/2

finalcolsb = (stars*cols).rstrip(' ')
printrowsb = ((finalcolsb+'\n')*math.floor(cs1row))
printrowsb = printrowsb + ((stars*math.floor(cs1col))+'CS1 '+ ((stars*math.floor(cs1col)).rstrip(' ')+'\n'))
printrowsb = printrowsb + ((finalcolsb+'\n')*math.floor(cs1row))
print('(b)')
print(printrowsb)
#--------------------------------------------------
cs1rowc=rows/2
cs1colc=cols/2

toprow = (stars*(math.floor(cs1colc))+' ^  ' + (stars*(math.floor(cs1colc)))).rstrip(' ') +'\n'#top row always same

toprow2 = toprow + ((stars*(math.floor(cs1colc)-1)) + ' /  ' + (stars) + ' \  ' + (stars*(math.floor(cs1colc)-1))).rstrip(' ')+'\n'#same as second top row

printrowsc = ((stars*(math.floor(cs1colc)-1)) + ' |  ' + (stars) + ' |  ' + (stars*(math.floor(cs1colc)-1))).rstrip(' ') +'\n' #basic format for row with | | in it

toprow3 = toprow2 + (printrowsc*(math.floor(cs1rowc)-2)) #using basic format for every row e amountil the one before CS1 row

row_cs1 = toprow3 + ((stars*(math.floor(cs1colc)-1)) + ' |  ' +'CS1 '+ ' |  ' + (stars*(math.floor(cs1colc)-1))).rstrip(' ') +'\n'

printrowc1 = row_cs1 + (printrowsc*(math.floor(cs1rowc)-2))#use basic format samut of times as we did leading up to cs1

printrowc2 = printrowc1 + ((stars*(math.floor(cs1colc)-1)) + ' \  ' + (stars) + ' /  ' + (stars*(math.floor(cs1colc)-1))).rstrip(' ')+'\n'#2nd row to closing (backwards of toprow2)

printrowc3 = printrowc2 + (stars*(math.floor(cs1colc))+' v  ' + (stars*(math.floor(cs1colc)))).rstrip(' ') #finish up with same as row 1 but with V instead of ^

print('(c)')
print(printrowc3)

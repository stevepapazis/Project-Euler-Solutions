"""Problem 89: Roman numerals
The rules for writing Roman numerals allow for many ways of writing each
number (see About Roman Numerals). However, there is always a "best" way
of writing a particular number.

For example, the following represent all of the legitimate ways of writing
the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least
number of numerals.

The 11K text file, roman.txt, contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; that is, they are arranged in
descending units and obey the subtractive pair rule (see About Roman Numerals
for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their minimal
form.

Note: You can assume that all the Roman numerals in the file contain no more
than four consecutive identical units.
"""


def roman_to_modern_numerals(txt):
    L=len(txt)
    summa=0
    for i in range(L):
        try:
            if txt[i]=='I':
                if txt[i+1]=='V':
                    summa-=1
                elif txt[i+1]=='X':
                    summa-=1
                else:
                    summa+=1
            elif txt[i]=='X':
                if txt[i+1]=='L':
                    summa-=10
                elif txt[i+1]=='C':
                    summa-=10
                else:
                    summa+=10
            elif txt[i]=='C':
                if txt[i+1]=='D':
                    summa-=100
                elif txt[i+1]=='M':
                    summa-=100
                else:
                    summa+=100
            elif txt[i]=='V':
                summa+=5
            elif txt[i]=='L':
                summa+=50
            elif txt[i]=='D':
                summa+=500
            elif txt[i]=='M':
                summa+=1000
        except IndexError:
            if txt[i]=='I':
                summa+=1
            elif txt[i]=='X':
                summa+=10
            elif txt[i]=='C':
                summa+=100
            elif txt[i]=='V':
                summa+=5
            elif txt[i]=='L':
                summa+=50
            elif txt[i]=='D':
                summa+=500
            elif txt[i]=='M':
                summa+=1000
    return summa
    
def modern_to_roman_numerals(n):
    string='M'*(n//1000)
    n%=1000
    temp=n//100
    if temp==4:
        string+='CD'
    elif temp==9:
        string+='CM'
    elif temp>4:
        string+='D'
        temp-=5
        string+='C'*temp
    else:
        string+='C'*temp
    n%=100
    temp=n//10
    if temp==4:
        string+='XL'
    elif temp==9:
        string+='XC'
    elif temp>4:
        string+='L'
        temp-=5
        string+='X'*temp
    else:
        string+='X'*temp
    n%=10
    if n==4:
        string+='IV'
    elif n==9:
        string+='IX'
    elif n>4:
        string+='V'
        n-=5
        string+='I'*n
    else:
        string+='I'*n
    return string

file=open('roman')
numerals=file.readlines()
for i in range(999):
    numerals[i]=numerals[i][:-1]
file.close()
 
difference=0
for i in numerals:
    difference+=len(i)-len(modern_to_roman_numerals(roman_to_modern_numerals(i)))
print(difference)

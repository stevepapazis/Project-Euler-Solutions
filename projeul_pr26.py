"""Project Euler Problem 26-Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:
1/2    =   0.5 
1/3    =   0.(3)     
1/4    =   0.25
1/5    =   0.2
1/6    =   0.1(6)    
1/7    =   0.(142857)
1/8    =   0.125
1/9    =   0.(1)     
1/10   =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d <= 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part."""

"""Lemma
n/9=0.nnnnnnn....    n=1,2,3,4,5,6,7,8  |e.g. 3/9=0.333333...
n/99=0.nnnnnnnn....  n=1,2,3,...,98  |e.g. 21/99=0.212121...
...

If there is an integer a so that 9*(10**k+10**(k-1)+...+1)=a*n, then the
recurring cycle of 1/n is k+1.
1/n=a/9*(10**k+10**(k-1)+...+1) and a<9*(10**k+10**(k-1)+...+1)=a*n
"""

list = [3,5,7,11,13]
for i in range(list[-1]+2, 1000, 2):
    stop = int(i**.5)+1
    flag = 1
    for j in list:
        if i%j==0:
            flag =0
            break
        elif j>stop: break
    if flag: list.append(i)
del list[:2]

l=len(list)
max=1 
s=9

while l!=1:
    max+=1
    s=s*10+9
    i=0
    while i<l:
        if s%list[i]==0:
            del list[i]
            l-=1
            i-=1
        i+=1

print("Solution",list[0])
input()

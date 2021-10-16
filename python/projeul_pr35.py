"""Problem 35: Circular primes

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""

import sys
sys.path.insert(0,"""C:\\Documents and Settings\\User\\Τα έγγραφά μου\\Η μουσική μου\\python\\mathstaff\\""")
import time
from primes import primes 


def mixdigits(n):
    n+=n[0]
    n=n.replace(n[0],'',1)
    return n

def search(l,n):
    i=0; end=len(l)
    while l[i] < n:
        i+=1
        if i+1 == end: break
    if l[i] == n: return i


start=time.clock()
s=[2,3,5,7]
p=primes(1000000, returnlist="")
l=len(p)

k=0
while k < l:
    if search(s, p[k])!=None: k+=1; continue
    strng = str(p[k])
    for j in strng:
        if search(['0','2','4','5','6','8'],j)!=None: break
    else:
        mx = mixdigits(strng); i=0 
        while mx != strng:
            if search(p, int(mx))==None: break
            mx = mixdigits(mx); i+=1
        else:
            mx = strng
            for I in range(i+1):
                s.append(int(mx))
                mx = mixdigits(mx)
            s.sort()
    k+=1
            
print(len(s))
print(time.clock()-start)


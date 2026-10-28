problem = """Problem 35: Circular primes

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""

import time


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


start=time.time()
s=[2,3,5,7]
# p=primes(1000000, returnlist="")

with open("primelist.dat") as f:
    primes = []
    while True:
        line = [int(p) for p in f.readline().split() if int(p)<10**6]
        primes.extend(line)

        if not line:
            break

l=len(primes)

k=0
while k < l:
    if search(s, primes[k])!=None: k+=1; continue
    strng = str(primes[k])
    for j in strng:
        if search(['0','2','4','5','6','8'],j)!=None: break
    else:
        mx = mixdigits(strng); i=0
        while mx != strng:
            if search(primes, int(mx))==None: break
            mx = mixdigits(mx); i+=1
        else:
            mx = strng
            for I in range(i+1):
                s.append(int(mx))
                mx = mixdigits(mx)
            s.sort()
    k+=1

print(problem)
print("Answer:", len(s))
print("Computed in", time.time()-start, "seconds")
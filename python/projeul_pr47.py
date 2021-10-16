"""Problem 47: Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:
14 = 2*7
15 = 3*5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2**2*7*23
645 = 3*5*43
646 = 2*17*19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?"""

def factorization(n):
    factors=[]
    if n==1: return factors
    elif len(factors)>4: return factors
    if n%2==0:
        n//=2
        factors.append(2)
        while n%2==0: n//=2
    if n%3==0:
        n//=3
        factors.append(3)
        while n%3==0: n//=3
    if n%5==0:
        n//=5
        factors.append(5)
        while n%5==0: n//=5
    if n%7==0:
        n//=7
        factors.append(7)
        while n%7==0: n//=7
    if n==1: return factors
    for i in range(3,int(n**.5)+1,2):
        if n%i==0:
            n//=i
            while n%i==0:
                n//=i
            break
    else:
        return factors+[n]
    return factors+factorization(i)+factorization(n)

i=648
while True:
    if len(factorization(i))==4:
        if len(factorization(i+1))==4:
            if len(factorization(i+2))==4:
                if len(factorization(i+3))==4:
                    break
                else: i+=4
            else: i+=3
        else: i+=2
    else: i+=1

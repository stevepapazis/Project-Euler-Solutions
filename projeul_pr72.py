"""Problem 72: Counting fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d<=8 in ascending order
of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions
for d<=1,000,000?"""

helpme="""\
1/n,2/n,...,k/n,...,(n-1)/n <~~ From the fractions on the left there are only
phi(n) fractions such as HCF(k,n)=1. Then, the number of elements that the set
of reduced proper fractions has is phi(2)+...+phi(n).
"""

primes = [3, 5, 7]
for i in range(9, 1000, 2):
    flag = 0
    sqrt = int(i**.5)
    for j in primes:
        if i%j==0: break
        if j> sqrt:
            flag = 1
            break
    if flag: primes.append(i)
primes.insert(0, 2)

def phi(n): #Euler's totient function, for values n<=1000000 ONLY!
    p = n
    for i in primes:
        if n%i==0:
            p*=(i-1)/i
            while n%i==0:
                n//=i
            if n==1: return int(p)
    if p==n: return n-1
    else: return int(p*(n-1)/n)
        
S = 0
for i in range(2, 1000001):
    S += phi(i)
print("Solution:", S)
input()

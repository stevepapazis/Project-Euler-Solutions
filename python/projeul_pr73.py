"""Problem 73: Counting fractions in a range

Consider the fraction, n/d, where n and d are positive integers. If n<d and
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
fractions for d ≤ 12,000?"""

primes = [3, 5, 7]
for i in range(9, 78, 2):
    flag = 0
    sqrt = int(i**.5)
    for j in primes:
        if i%j==0: break
        if j>sqrt:
            flag = 1
            break
    if flag: primes.append(i)
primes.insert(0, 2)

def factorization(n): #It only works for 2<=n<=6000!
    factors=[]
    for i in primes:
        if n%i==0:
            factors.append(i)
            while n%i==0:
                n//=i
            if n==1: return factors
    factors.append(n)
    return factors

def f(n):
    """It returns the number of fractions n/d such as gcd(n,d)=1 and 1/3<n/d<1/2 when d≤12000."""
    p = factorization(n)
    N = len(p)
    end = min(n-1, 12000 - 2*n)
    r = end
    if N==1:
        r -= end//p[0]
    elif N==2:
        l = p
        r -= sum( end//i for i in l )
        r += end//(p[0]*p[1])
    elif N==3:
        l = p
        r -= sum( end//i for i in l )
        l = [p[0]*p[1], p[0]*p[2], p[1]*p[2]]
        r += sum( end//i for i in l )
        r -= end//(p[0]*p[1]*p[2])
    elif N==4:
        l = p
        r -= sum( end//i for i in l )
        l = [p[0]*p[1], p[0]*p[2], p[0]*p[3], p[1]*p[2], p[1]*p[3], p[2]*p[3]]
        r += sum( end//i for i in l )
        l = [p[0]*p[1]*p[2], p[0]*p[1]*p[3], p[0]*p[2]*p[3], p[1]*p[2]*p[3]]
        r -= sum( end//i for i in l )
        r += end//(p[0]*p[1]*p[2]*p[3])
    elif N==5:
        l = p
        r -= sum( end//i for i in l )
        l = [p[0]*p[1], p[0]*p[2], p[0]*p[3], p[0]*p[4], p[1]*p[2], p[1]*p[3], p[1]*p[4], p[2]*p[3], p[2]*p[4], p[3]*p[4]]
        r += sum( end//i for i in l )
        l = [p[0]*p[1]*p[2], p[0]*p[1]*p[3], p[0]*p[1]*p[4], p[0]*p[2]*p[3], p[0]*p[2]*p[4], p[0]*p[3]*p[4], p[1]*p[2]*p[3], p[1]*p[2]*p[4], p[1]*p[3]*p[4], p[2]*p[3]*p[4]]
        r -= sum( end//i for i in l )
        l = [p[0]*p[1]*p[2]*p[3], p[0]*p[1]*p[2]*p[4], p[0]*p[1]*p[3]*p[4], p[0]*p[2]*p[3]*p[4], p[1]*p[2]*p[3]*p[4]]
        r += sum( end//i for i in l )
        r -= end//(p[0]*p[1]*p[2]*p[3]*p[4])
    return r

print("Solution:", sum(f(n) for n in range(2, 6000)))
input()

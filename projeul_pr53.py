"""Problem 53: Combinatoric selections


There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, C(5,3) = 10.

In general, C(n, r) = n!/(r!*(n-r)!), where r<=n,
n! = n*(n-1)*...*3*2*1, and 0! = 1.


It is not until n = 23, that a value exceeds one-million: C(23,10) = 1144066.

How many, not necessarily distinct, values of C(n, r), for 1<=n<=100, are
greater than one-million?"""

def nCr(n,r):
    if r==0: return 1
    if r==n: return 1
    b=n-r
    p=n
    if r>b:
        for i in range(r+1,n):
            p*=i
        for i in range(2,b+1):
            p/=i
    else:
        for i in range(b+1,n):
            p*=i
        for i in range(2,r+1):
            p/=i
    return int(p)

s=0
for n in range(23,101):
    for r in range(2,n+1):
        if nCr(n,r)>1000000: s+=1

print("Solution:",s)
input()


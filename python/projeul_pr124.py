"""Problem 124: Ordered radicals

The radical of n, rad(n), is the product of the distinct prime factors of n. For
example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on
n if the radical values are equal, we get:

Unsorted        Sorted
n  rad(n)    n  rad(n)  k
--------------------------
1    1       1    1     1
2    2       2    2     2
3    3       4    2     3
4    2       8    2     4
5    5       3    3     5
6    6       9    3     6
7    7       5    5     7
8    2       6    6     8
9    3       7    7     9
10   10      10   10    10

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000)."""

def factorization(n):
    factors=[]
    if n%2==0:
        factors.append(2)
        n//=2
        while n%2==0: n//=2
    if n%3==0:
        factors.append(3)
        n//=3
        while n%3==0: n//=3
    if n%5==0:
        factors.append(5)
        n//=5
        while n%5==0: n//=5
    if n%7==0:
        factors.append(7)
        n//=7
        while n%7==0: n//=7
    if n==1: return factors
    temp=int(n**.5)+1
    for i in range(3,temp,2):
        if n%i==0:
            n//=i
            while n%i==0: n//=i
            break
    else:
        return factors+[n]
    return factors+factorization(i)+factorization(n)

E=[(0,0)]
for n in range(1,100001):
    temp=factorization(n)
    radn=1
    for i in temp: radn*=i
    if radn<10000:           #n>=rad(n)>10000
        E.append((radn,n))
    
E.sort()
print("Solution:",E[10000][1])
input()

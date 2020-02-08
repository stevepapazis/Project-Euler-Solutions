"""Problem 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers."""

from bisect import bisect as bisect

def properdivisors(n):
    list=[1]
    l=int(n**.5)
    for i in range(2,l):
        if n%i==0:
            list+=[i,n//i]
    if l**2==n: list+=[l]
    elif n%l==0: list+=[l,n//l]
    return sum(list)

abundant=[]
for i in range(12,28123):
    if properdivisors(i)>i:
        abundant.append(i)

numbersthataddtoanabuntantnumber=set()
for i in abundant:
    for j in abundant:
        if i+j>28122: break
        numbersthataddtoanabuntantnumber.add(i+j)


l=list(numbersthataddtoanabuntantnumber)
l.sort()

sum=276 #1+2+3+...+23
c=0
for i in range(24,28123):
    if l[c]==i: c+=1
    else: sum+=i
    
print("Solution:",sum)

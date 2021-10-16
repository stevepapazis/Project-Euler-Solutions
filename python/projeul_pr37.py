"""Problem 37: Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def primality_test(n):
    if n%2==0: return True
    elif n%3==0:
        if n==3: return False
        return True
    elif n%6==1 or n%6==5:
        for i in range(5,int(n**.5+1),2):
            if n%i==0: return True
        else: return False
        
truncatable=[23,37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
n=1
c=11

while c-11:
    for a in ('23','29','31','37','53','59','71','73','79','97'):
        for z in ('13','17','37','73','97'):
            t=int(a+str(n)+z)
            s=t
            d=0
            while t>0:
                if primality_test(t): break
                t//=10
                d+=1
            else:
                x=10
                for i in range(d):
                    if primality_test(s%x): break
                    x*=10
                else:
                    c+=1
                    truncatable.append(s)
    n+=2


print(truncatable)
print(sum(truncatable))

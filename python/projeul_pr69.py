""" Problem 69: Totient maximum

Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
prime to nine, φ(9)=6.

+---+-------------------+------+---------+
| n |  Relatively Prime | φ(n) |  n/φ(n) |
+---+-------------------+------+---------+
| 2 |  1  	             |  1   |    2    |
| 3 |  1,2	             |  2   |   1.5   |
| 4 |  1,3	             |  2   |    2    |
| 5 |  1,2,3,4          |  4   |   1.25  |
| 6 |  1,5	             |  2   |    3    |
| 7 |  1,2,3,4,5,6      |  6   | 1.166...|
| 8 |  1,3,5,7          |  4   |    2    |
| 9 |  1,2,4,5,7,8      |  6   |   1.5   |
|10 |  1,3,7,9          |  4   |   2.5   |
+---+-------------------+------+---------+

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum."""


solution="""
>>> φ(n) /n  =  Π( 1 - 1/p[i])      where p is a list of prime factors of n
<=> n/φ(n)  =  Π( p[i]/(p[i]-1) )

If n is the value for which n/φ(n) is a maximum then n can't be a prime, because if so:
n/φ(n)  =  n/(n-1)   =  1 + 1/(n-1)  ≤  2  =  2/φ(2)  ≤  3  =  6/φ(6)
n is a composite number, so n  =  a*b*...*z where a,b,...z are primes and a,b,...,z<=1000.

Let 'primes' be a list with all the prime numbers bellow 1,000 and l=len(primes).

max{ n/φ(n), n ≤ 1,000,000 }  =  min{ φ(n) /n, n ≤ 1,000,000 }

>>> 1/primes[i]  >=  1/primes[j]         when i in {0,1,2,3,4,5,6} and j in {0,1,2,...,l-1} and i ≤ j
<=> 1 - 1/primes[i]  ≤  1 -1/primes[j]  <  1         when i in {0,1,2,3,4,5,6} and j in {0,1,2,...,l-1}  and i ≤ j
 => [ Π( 1 - 1/primes[i] ) for i in {0,1,2,3,4,5,6} ]   ≤  [ Π( 1 -1/primes[j] ) for j in  J and J is a no empty subset of  {0,1,2,...,l-1} ]
 => [ Π( 1 - 1/primes[i] ) for i in {0,1,2,3,4,5,6} ]  ≤  φ(n) /n         when n = [ Π( primes[j]) for j in J ]

N  =  primes[0]*primes[1]*primes[2]*primes[3]*primes[4]*primes[5]*primes[6]
φ( N ) / N  =  min{ φ(n) /n, n ≤ 1,000,000 } = max{ n/φ(n), n ≤ 1,000,000 }
=> Solution = N
"""

primes = [2, 3]
for i in range(5, 1000, 2):
    for j in range(3, i, 2):
        if i%j==0:
            break
    else:
        primes.append(i)

print('Solution:', primes[0]*primes[1]*primes[2]*primes[3]*primes[4]*primes[5]*primes[6])
input()

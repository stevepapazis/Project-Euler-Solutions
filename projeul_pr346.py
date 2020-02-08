"""Problem 346: Strong Repunits

The number 7 is special, because 7 is 111 written in base 2, and 11 written in
base 6 (i.e. 7(base:10) = 11(base:6) = 11(base:12)). In other words, 7 is a
repunit in at least two bases b > 1. 

We shall call a positive integer with this property a strong repunit. It can be
verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}. 

Furthermore, the sum of all strong repunits below 1000 equals 15864. 

Find the sum of all strong repunits below 10**12."""

helpme = """\
For every natural number n: n = 11(base:n-1).
Let n be a strong repunits number with k digits in base b.
Then n = [ Σ b**i, for i in [0, k-1] ]  = (b**k-1)/(b-1).

b ≥ 2 => n ≤ b**k ≤ 10**12 => b ≤ 10**(12/(k-1))
k ≥ 3 => b ≤ 10**6
n > b**(k-1) => log(n, b) > k-1 => int(log(n, b)) > k-1 => k ≤ 1+int(log(n, b)) 
"""

from math import log as log

L = [1] #A list of all strong repunit numbers bellow 10**12.
 
for b in range(2, 1000000):
    end = 1 + int( 1 + 12*log(10,b) )
    t = b + 1
    B = b 
    for i in range(3, end):
        B *= b
        t += B
        if t < 1000000000000:
            L.append(t)
L = set(L)
L = list(L)
print("Solution:", sum(L))
input()

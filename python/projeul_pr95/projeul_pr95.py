from math import log as log

listOfPrimes = [int(i) for i in open("prime_list.txt").read().split()]

problem = """\
Problem 95: Amicable chains

The proper divisors of a number are all the divisors excluding the number
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As
the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of
the proper divisors of 284 is 220, forming a chain of two numbers. For this
reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496,
we form a chain of five numbers:

        12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable
chain.

Find the smallest member of the longest amicable chain with no element
exceeding one million.
"""

explanation = """\
The sum d of the divisors of a number is a multiplicative function, that
is d(1)=1 and d(a*b)=d(a)*d(b) whenever gcd(a,b)=1. Moreover, it is
straightforward to compute that d(p**a)=(p**(a+1)-1)/(p-1). Using those
properties and a list of primes we can create a sieve with the sums of
the proper divisors for all numbers less than 1000000.

Having that sieve, we can compute the lengths of the amicable chains.
"""

sumOfProperDivisors = [0]
sumOfProperDivisors.extend( list( [1 for i in range(10**6)] ) )

for p in listOfPrimes:
    for k in range(p, 1000000, p):
        sumOfProperDivisors[k] *= 1+p
    t = int(6*log(10,p))+1
    step = p
    for a in range(2,t):
        step *= p
        increase = step*p-1
        decrease = step-1
        for k in range(step, 1000000, step):
            sumOfProperDivisors[k] *= increase
            sumOfProperDivisors[k] //= decrease

for i,k in enumerate(sumOfProperDivisors):
    sumOfProperDivisors[i] -= i

amicableChains = []

for n in range(1000000):
    amicableChains.append([n])
    next = sumOfProperDivisors[n]
    while 1 < next <= 1000000 and next not in amicableChains[n]:
        amicableChains[n].append(next)
        if next == n: break
        next = sumOfProperDivisors[next]
    if next != n:
        amicableChains[n] = []

removedoubles = []
sortedremovedoubles = []
amicableChains = [i for i in amicableChains if i]

while amicableChains:
    next = amicableChains.pop()
    if sorted(next) not in sortedremovedoubles:
        removedoubles.append(next)
        sortedremovedoubles.append( sorted(next) )

amicableChains = removedoubles

maxChain = amicableChains[0]

for chain in amicableChains:
    if len(chain) > len(maxChain):
        maxChain = chain

solution = min(maxChain)


print(
    problem,
    "\n\n\n",
    explanation,
    "\n\n\n",
    "All the amicable chains with elements less than one million are:\n",
    sep=""
    )

for chain in amicableChains:
    print(*chain,chain[0],sep=" → ")

print("\nThe longest chain has length ",
      len(maxChain),
      " and its smallest member is ",
      solution,".",sep=""
      )

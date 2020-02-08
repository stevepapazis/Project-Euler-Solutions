with open('primelist.dat', mode="r") as file:
    nl=file.read().split('  ')
    primes=[]
    for i in nl:
        primes.append(int(i))
    del nl
    file.close()

def getNextPrime():
    next = primes[-1] + 2
    end = next**.5
    while True:
        j=1
        while( primes[j] <= end ):
                if next % primes[j] == 0: break
                j += 1
        else:
                primes.append(next)
                break
        next += 2
        end = next**.5

from heapq import *

def maxExponentsOfNumbersLessThan(M):
    exponents = [1,0]
    nextIncrease = [(4,0),(3,1)]
    heapify(nextIncrease)
    l = 2
    for i in range(M-1):
        if exponents[-1]!=0:
            if l == len(primes):
                getNextPrime()
            heappush( nextIncrease, (primes[l],l) )
            exponents.append(0)
            l += 1
        priority, primeIndex = heappop(nextIncrease)
        exponents[primeIndex] += 1
        heappush(nextIncrease, (priority**2, primeIndex))
    return exponents

exponentsOfAnswer = maxExponentsOfNumbersLessThan(500500)
max = 1
for i,e in enumerate(exponentsOfAnswer):
    max = ((primes[i]**(2**e-1))%500500507*max)%500500507
print("The answer is: ", max)
input()

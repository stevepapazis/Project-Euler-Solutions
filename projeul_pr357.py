problem = """\
Problem 357: Prime generating integers

Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100000000
such that for every divisor d of n, d+n/d is prime."""

explanation = """\
Since n%1==0, there exists a prime p such as n = p - 1.
If d+n/d is to be prime it cannot contain a square, therefore n = 4k+2.
"""



class PrimeSieve:
    """\
Generate a prime sieve and compute a list with all the primes less than N, if
generatelist == True.

An initial list of primes can be provided in primelist.
"""
    

    def __init__(sieve, N, primelist = None, generatelist = False):
        sieve.__setup_sieve__(N, primelist)
        sieve.__generate_sieve__()
        if generatelist:
            sieve.getPrimes()

               
    def __setup_sieve__(sieve, N, primelist):
        sieve.__N = N
        sieve.__topIndex = N//2 + 1
        sieve.__oddPrimeSieve = bytearray( [1]*(sieve.__topIndex) )
        if primelist != None:
            for p in primelist:
                if p == 2: continue
                for multipleOfp in range(p**2//2, sieve.__topIndex, p):
                    sieve.__oddPrimeSieve[multipleOfp] = 0
        sieve.__oddPrimeSieve[0] = 0

        
    def __generate_sieve__(sieve):
        sqrt = sieve.__N**.5
        for k, isItPrime in enumerate(sieve.__oddPrimeSieve,1):
            odd = 2*k - 1
            if odd>sqrt:
                break
            if isItPrime:
                for multipleOfOdd in range(odd**2//2, sieve.__topIndex, odd):
                    sieve.__oddPrimeSieve[multipleOfOdd] = 0


    def __repr__(sieve):
        return str(sieve.getPrimes())


    def __len__(sieve):
        try:
            return sieve.__numberOfPrimes
        except AttributeError:
            sieve.__numberOfPrimes = len(sieve.getPrimes())
        return sieve.__numberOfPrimes


    def __getitem__(sieve, key):
        return sieve.getPrimes()[key]


    def isOddPrime(sieve, n):
        """Test if the odd number n is prime against the sieve."""
        try:
            return bool( sieve.__oddPrimeSieve[n//2] )
        except IndexError:
            pass
        raise Exception( "n must be less than " + str(sieve.__N) )


    def isPrime(sieve, n):
        """Test if n is prime against the sieve."""
        if n%2==0:
            if n==2:
                return True
            else:
                return False
        else:
            return sieve.isOddPrime(n)


    def topLimit(sieve):
        return sieve.__N


    def getPrimes(sieve):
        """Get a list with all the prime numbers in the sieve."""
        try:
            return sieve.__primes
        except AttributeError:
            sieve.__primes = [2]
            sieve.__primes.extend(
                [
                    2*n + 1 \
                    for n in range(len(sieve.__oddPrimeSieve)-1)\
                    if sieve.__oddPrimeSieve[n]
                 ]
                )
            return sieve.__primes




primesieve = PrimeSieve(10**8)


primeGeneratingIntegers = [1]
        

for p in range(3,100000000,4):
    if not primesieve.isOddPrime(p):
        continue
    candidate = p - 1
    sqrt = int(candidate**.5) + 1
    for d in range(2, sqrt):
        if candidate % d == 0:
            if not primesieve.isPrime( d + candidate//d ):
                break
    else:
        primeGeneratingIntegers.append( candidate )
                
            
answer = sum(primeGeneratingIntegers)

    


print(
    problem,
    "\n\n\n",
    explanation,
    "\n\n",
    "Answer: ",
    answer,
    sep=""
    )

input()

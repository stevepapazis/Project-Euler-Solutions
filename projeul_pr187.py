with open('primelist.dat', mode="r") as file:
    nl=file.read().split('  ')
    primes=[]
    for i in nl:
        primes.append(int(i))
    del nl
    file.close()

def numberOfPrimesLessThan(n):
    for i in range(int(n),-1,-1):
        try:
            return indexOfPrime[i]
        except KeyError:
            continue

indexOfPrime = dict( [ (j,i+1) for i,j in enumerate(primes) ] )

S = 0
prime = 2
index = 0
while prime < 10**4:
    S += numberOfPrimesLessThan(10**8/prime) - index 
    index += 1
    prime = primes[index]
print("The answer is: ", S)
input()

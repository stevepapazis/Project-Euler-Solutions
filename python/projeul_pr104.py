problem = """\
Problem 104: Pandigital Fibonacci ends

The Fibonacci sequence is defined by the recurrence relation:
F_n = F_(n−1) + F_(n−2), where F_1 = 1 and F_2 = 1.

It turns out that F_541, which contains 113 digits, is the first Fibonacci number
for which the last nine digits are 1-9 pandigital (contain all the digits 1 to
9, but not necessarily in order). And F_2749, which contains 575 digits, is the
first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that F_k is the first Fibonacci number for which the first nine digits AND
the last nine digits are 1-9 pandigital, find k.
"""

explanation = """\
It is known that the last digits of Fibonacci numbers circle periodically.
The last digit repeats after 60 indices, the two last digits repeat after 300
indices and the last d digits repeat after 15*10**(d-1) indices.

By using a closed form expression for the sequence, we can compute the first 9
digits."""



fiblist = [0,1]

def fibonacci(n):
    """Compute the nth Fibonacci number."""
    try:
        return fiblist[n]
    except IndexError:
        a = fiblist[-2]
        b = fiblist[-1]
        for i in range(n-len(fiblist)+1):
            a, b = b, (a+b) 
            fiblist.append(b)
        return fiblist[n]



fastfiblist = dict()
fastfiblist[0] = 0
fastfiblist[1] = 1

def fastFib(n):
    """\
Compute the nth Fibonacci number by a recursive formula involving \
n//2 and n//2+1."""
    if n%2 == 1:
        try:
            return fastfiblist[n]
        except KeyError:
            fastfiblist[n] = fastFib(n//2+1)**2 + fastFib(n//2)**2 
            return fastfiblist[n]
    else:
        try:
            return fastfiblist[n]
        except KeyError:
            a = fastFib(n//2-1)
            b = fastFib(n//2)  
            fastfiblist[n] = 2*a*b + b**2  
            return fastfiblist[n]




fastfiblastlist = dict()
fastfiblastlist[0] = 0
fastfiblastlist[1] = 1

def fastFibLast9Digits(n):
    """\
Compute the last 9 digits of the nth Fibonacci number by a recursive formula\
involving n//2 and n//2+1."""
    getlastdigs = 1000000000
    if n%2 == 1:
        try:
            return fastfiblastlist[n]
        except KeyError:
            r = (fastFibLast9Digits(n//2+1)**2 \
                 + fastFibLast9Digits(n//2)**2) % getlastdigs
            fastfiblastlist[n] = r 
            return r
    else:
        try:
            return fastfiblastlist[n]
        except KeyError:
            a = fastFibLast9DigitsMemoryError(n//2-1)
            b = fastFibLast9DigitsMemoryError(n//2) 
            r = ( 2*a*b + b**2  ) % getlastdigs
            fastfiblastlist[n] = r
            return r




def slowLastDigitPeriod(numbOfDigs):
    """It only works for numbOfDigs<=9 due to fastFibLast9Digits."""

    def previousLastDigitPeriod(numbOfDigs):
        getlastdigits = 10**numbOfDigs
        if numbOfDigs == 1:
            k = 1
            b = fiblist[k]
            while True:
                a = b
                k += 1
                b = fastFibLast9Digits(k)
                if a%getlastdigits==0 and b%getlastdigits==1: break
            return k-1
        else:
            k = 0
            previousperiods = previousLastDigitPeriod(numbOfDigs-1)
            while True:
                k += previousperiods
                a = fastFibLast9Digits(k)%getlastdigits
                b = fastFibLast9Digits(k+1)%getlastdigits
                if a==0 and b==1: break
            return k

    return previousLastDigitPeriod(numbOfDigs)



        
def lastDigitsPeriod(numbOfDigs):
    if numbOfDigs < 3: return slowLastDigitPeriod(numbOfDigs)
    else: return 15*10**(numbOfDigs-1)





def fastFibFirst9Digits(n, previous=None):
    """\
Compute the first 9 digits of a Fibonacci number.
It works best for big values of n."""
    if previous==None:
        p = 0.4472135954999579
    else:
        p = previous
    for i in range(n):
        p *= 1.618033988749895
        p = int(str(p).replace(".","")[:15])
    p = str(p).replace(".","")
    return p[:9],int(p)



def is9Pandigital(n):
    return ''.join(sorted(str(n)))=='123456789'


print(
    problem,
    "\n\n\n",
    explanation,
    "\n\n\n",
    "Fibonacci numbers with 9-pandigital starts and ends:",
    sep=""
    )


a = fibonacci(1)
b = fibonacci(2)
k=2
previous = fastFibFirst9Digits(k)
previouskey = k
number_double_pandigital_fib=0
while True:
    a, b = b,(a+b)%1000000000
    k += 1
    if is9Pandigital(b):
        previous = fastFibFirst9Digits( k-previouskey, previous[1] )
        previouskey = k
        if is9Pandigital(previous[0]):
            number_double_pandigital_fib += 1
            print("\n")
            print( number_double_pandigital_fib,":","("+str(k)+", ", previous[0]+" ... "+str(b)+")" )




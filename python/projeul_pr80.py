problem = """Problem 80: Square root digital expansion

It is well known that if the square root of a natural number is not an integer,
then it is irrational. The decimal expansion of such square roots is infinite
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the
first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of
the first one hundred decimal digits for all the irrational square roots."""


def squareRoot(n, accuracy):
    sqrt = str(n**.5).split(".")
    decimal = int( sqrt[0] + sqrt[1][:-1] )
    acc = len( sqrt[1] )
    n = n*10**(2*acc)

    def addLastDig( decimal, digit ): return decimal*10 + digit
    
    def findNxtDecimal( decimal, lowGuess, highGuess ):
        if highGuess == lowGuess + 1:
            high = addLastDig( decimal, highGuess )
            if high**2 >= n:
                return addLastDig( decimal, lowGuess )
            else:
                return high
            
        midGuess = ( lowGuess + highGuess )//2
        midDecimal = addLastDig( decimal, midGuess )
        
        if midDecimal**2 > n:
            return findNxtDecimal( decimal, lowGuess, midGuess )
        else: 
            return findNxtDecimal( decimal, midGuess, highGuess )

    while acc <= accuracy:
        decimal = findNxtDecimal( decimal, 0, 9 )
        acc += 1
        n *= 100

    return sqrt[0] + "." + str(decimal)[len(sqrt[0]):]

def sumDigits(n):
    return sum([ int(d) for d in n ])


squares = [4, 9, 16, 25, 36, 49, 64, 81]
non_squares = [ n for n in range(2,100) if n not in squares ]

answer = sum(
        [
            sumDigits( squareRoot(n, 100-1 ).replace(".", "") )
                       for n in non_squares
        ]
    )

print(problem)
print("\n")
input("The total is " + str(answer) + ".")

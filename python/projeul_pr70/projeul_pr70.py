problem = """\
Problem 70: Totient permutation

Euler's Totient function, φ(n), is used to determine the number of positive
numbers less than or equal to n which are relatively prime to n. For example,
as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine,
φ(9)=6.
The number 1 is considered to be relatively prime to every positive number,
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1<n<10**7, for which φ(n) is a permutation of n and the
ratio n/φ(n) produces a minimum.
"""

explanation = """\
Since we know that φ(n) = n * Π(1-1/p_i) when  Π p_i^a_i  is the prime
factorization of n, we deduce the equation n/φ(n)  =  Π p_i/(p_i-1).

Because p/(p-1)>=1 and 87109=11*7919, the minimum value is attained at a number
n which has at most two prime factors less than 10**7.

If n were prime, φ(n)=n-1 and it would end in 1,3,7 or 9. Subtracting 1 only
changes the last digit to 0,2,6 or 8, therefore n-1 can not be a permutation
of n.

So n=p*q for two prime numbers 2<=p,q<5*10**6.
"""


listofprimes = [int(i) for i in open("prime_list.txt").read().split()]


def isItAPermutationOf(m, n):
    """Check whether m is a permutation of n."""
    m_digits = sorted([i for i in str(m)])
    n_digits = sorted([i for i in str(n)])
    return m_digits==n_digits

minimum = 87109/79180


for p in listofprimes:
    templist = (i for i in listofprimes)
    for q in templist:
        n=p*q
        if n >= 10000000:
            break
        phi_p_q = (p-1)*(q-1)
        if isItAPermutationOf(n, phi_p_q):
            if n/phi_p_q < minimum:
                solution = n
                minimum = n/phi_p_q


print(
    problem,
    "\n\n\n",
    explanation,
    "\n\n\n",
    "By testing all the numbers produced that way we find that n/φ(n) is",
    "\nminimized for n=", solution,", where it attains the minumum value ",
    minimum,".",
    sep=""
    )

problem = """\
Problem 700: Eulercoin

Leonhard Euler was born on 15 April 1707.

Consider the sequence a_n = 1504170715041707n mod 4503599627370517.

An element of this sequence is defined to be an Eulercoin if it is strictly
smaller than all previously found Eulercoins.

For example, the first term is 1504170715041707 which is the first Eulercoin.
The second term is 3008341430083414 which is greater than 1504170715041707 so
is not an Eulercoin. However, the third term is 8912517754604 which is small
enough to be a new Eulercoin.

The sum of the first 2 Eulercoins is therefore 1513083232796311.

Find the sum of all Eulercoins."""

explanation = """\
Let p = 4503599627370517 and m = 1504170715041707. Since p is prime, m has a
modular inverse, that is an integer m_inverse such as  m*m_inverse == 1 (mod p).
Then   a_n = m*n % p  <=>  m_inverse * a_n = n % p.

If we know that e is an Eulercoin, we can find the smallest index
n = m_inverse * r = n % p such as a_n = r when 1<=r<e. By sorting those indices
and we find the corresponding values from which we filter the Eulercoins. 
"""


def gcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if a == 0:
        return (b, 0, 1)
    else:
        b_div_a, b_mod_a = divmod(b, a)
        g, x, y = gcd(b_mod_a, a)
        return (g, y - b_div_a * x, x)

def modularInverse(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, y = gcd(a, b)
    if g != 1:
        raise Exception('There exists no modular inverse: gcd(a, b) != 1')
    return x % b


p = 4503599627370517
m = 1504170715041707
m_inverse = modularInverse(m,p)


eulercoins = [(1504170715041707, 1), (8912517754604, 3)]

def eulerCoin(n):
    try:
        return eulercoins[n-1]
    except IndexError:
        previousValue = eulerCoin(n-1)[0]
        previousIndex = eulerCoin(n-1)[1]
        for i in range(previousIndex+1,999999999999999999):
            r = (1504170715041707*i)%4503599627370517
            if r < previousValue:
                eulercoins.append((r,i))
                return (r,i)

limit = eulerCoin(16)[0] 

indices = [
    candidateValue * m_inverse % p for candidateValue in range(1,limit)
    ]

indices.sort()

values = [m * index % p for index in indices]

for value in values:
    if value < limit:
        limit = value
        eulercoins.append( ( limit, limit * m_inverse % p ) )

eulercoins.append( (0,p) )
        
    
solution = sum([i[0] for i in eulercoins])


print(
    problem,
    "\n\n\n",
    explanation,
    "\n\n",
    "There are ",
    len(eulercoins),
    " Eulercoins: \n",
    "".join([str(i[0])+", " for i in eulercoins[:-1]]),
    eulercoins[-1][0],
    "\n\n\nAnswer:", solution,
    sep=""
    )

input()

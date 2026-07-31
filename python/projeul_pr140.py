from math import isclose, isqrt
from functools import cache

problem = """\
Problem 140: Modified Fibonacci Golden Nuggets

Consider the infinite polynomial series A_G(x) := Σ G_k * x**k, where G_k is
the k-th term of the second order recurrence relation G_k := G_{k-1} + G_{k-2},
G_1 := 1 and G_2 := 4; that is, 1, 4, 5, 9, 14, 23, ...

For this problem we shall be concerned with values of x for which A_G(x) is
a positive integer.

The corresponding values of x for the first five natural numbers are shown
below.
                    +----------------+-----------+
                    |       x        |   A_G(x)  |
                    +----------------+-----------+
                    |   (√5-1)/4     |     1     |
                    |      2/5       |     2     |
                    |   (√22-2)/6    |     3     |
                    |  (√137-5)/14   |     4     |
                    |      1/2       |     5     |
                    +----------------+-----------+

We shall call A_G(x) a golden nugget if x is rational, because they become
increasingly rarer; for example, the 20-th golden nugget is 211345365.

Find the sum of the first thirty golden nuggets.
"""

explanation = """
Explanation:
To begin, we derive a closed-form expression for the generating function of
the sequence. Observe that
      A_G(x) == Σ G_n * x**n
             == G_1*x + G_2*x**2 + (G_1 + G_2)*x**3 + (G_2 + G_3)*x**4 + ...
             == x + 4*x**2 + A_G(x)*x**2 + (A_G(x) - G_1*x)*x
             == x + 3*x**2 + A_G(x)*(x**2 + x)
  <=> A_G(x) == (x + 3*x**2) / (1 - x - x**2)

Let n be a positive integer such that A_G(x) == n. Solving for x gives
        x == (- n - 1 + sqrt(5*n**2 + 14*n + 1)) / (2*(n+3))

Hence, x is rational if and only if 5*n**2 + 14*n + 1 is a perfect square.

Writing Y**2 == 5*n**2 + 14*n + 1 and setting X := 5*n+7, transforms the
problem into the general Pell equation X**2 - 5*Y**2 = 44. Thus the golden
nuggets can be recovered from its integer solutions.

Every solution of the generalized Pell equation is obtained from a minimal
representative by multiplication with powers of the fundamental unit 9+4√5,
which is the fundamental solution of the Pell equation: u**2-5*v**2 == 1.

Equivalently, if (X_n, Y_n) is a solution, then
    X_{n+1} = 9*X_n + 20*Y_n
    Y_{n+1} = 4*X_n +  9*Y_n

Therefore, it suffices to determine the minimal representatives (or seed
solutions) of the generalized Pell equation X**2 - 5*Y**2 = 44. These are
(7,1), (8,2), (13,5), (17,7), (32,14), (43,19).
"""

@cache
def _pell_solution(k, x0, y0):
    if k == 0: return x0, y0
    x, y = _pell_solution(k - 1, x0, y0)
    return (
        9*x + 20*y,
        4*x + 9*y,
    )

def general_pell_solution(k):
    orbits = [(7,1), (8,2), (13,5), (17,7), (32,14), (43,19)]
    N = len(orbits)
    x0, y0 = orbits[k%N]
    return _pell_solution(k//N, x0, y0)

N = 30

print(problem, explanation, f"First {N} golden nuggets", sep="\n")

sum = 0
k = 0
i = 0
while k != N:
    i += 1
    X,_ = general_pell_solution(i)

    if (X-7) % 5 != 0: continue

    n = (X-7)//5

    m = isqrt(5*n*n + 14*n + 1)
    assert m*m == 5*n*n + 14*n + 1

    p = - n - 1 + m
    q = 2 * (n + 3)
    A_G = p*(q + 3*p) / (q**2 - p*q - p**2)
    assert isclose(A_G, n)

    k += 1
    print(f"\t{k}. A_G({p}/{q}) == {n}")
    sum += n

print(f"\nAnswer: sum_of_first_{N}_golden_nuggets == {sum}")
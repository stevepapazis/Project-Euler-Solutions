from math import isclose, isqrt
from functools import cache

problem = """\
Problem 137: Fibonacci Golden Nuggets

Consider the infinite polynomial series A_F(x) := Σ F_k * x**k, where F_k is
the k-th term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ...; that is,
F_k := F_{k-1} + F_{k-2}, F_1 := 1 and F_2 := 1.

For this problem we shall be interested in values of x for which A_F(x) is a
positive integer.

Surprisingly,
A_F(1/2) == (1/2)*1 + (1/2)**2*1 + (1/2)**3*2 + (1/2)**4*3 + (1/2)**5*5 + ...
         == 1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
         == 2

The corresponding values of x for the first five natural numbers are shown
below.
                    +----------------+-----------+
                    |       x        |   A_F(x)  |
                    +----------------+-----------+
                    |    √2 - 1      |     1     |
                    |      1/2       |     2     |
                    |   (√13-2)/3    |     3     |
                    |   (√89-5)/8    |     4     |
                    |   (√34-3)/5    |     5     |
                    +----------------+-----------+

We shall call A_F(x) a golden nugget if x is rational, because they become
increasingly rarer; for example, the 10-th golden nugget is 74049690.

Find the 15-th golden nugget.
"""

explanation = """
Explanation:
To begin, we derive a closed-form expression for the generating function of
the Fibonacci sequence. Observe that
      A_F(x) == Σ F_n * x**n
             == F_1*x + F_2*x**2 + (F_1 + F_2)*x**3 + (F_2 + F_3)*x**4 + ...
             == x + x**2 + A_F(x)*x**2 + (A_F(x) - x)*x
             == x + A_F(x)*(x**2 + x)
  <=> A_F(x) == x / (1 - x - x**2)

Let n be a positive integer such that A_F(x) == n. Solving for x gives
        x == (- n - 1 + sqrt(5*n**2 + 2*n + 1)) / (2*n)

Hence, x is rational if and only if 5*n**2 + 2*n + 1 is a perfect square.

Writing Y**2 == 5*n**2 + 2*n + 1 and setting X := 5*n+1, transforms the
problem into the general negative Pell equation X**2 - 5*Y**2 = -4. Thus
the golden nuggets can be recovered from its integer solutions.

Every solution of the generalized Pell equation is obtained from a minimal
representative by multiplication with powers of the fundamental unit 9+4√5,
which is the fundamental solution of the Pell equation: u**2-5*v**2 == 1.

Equivalently, if (X_n, Y_n) is a solution, then
    X_{n+1} = 9*X_n + 20*Y_n
    Y_{n+1} = 4*X_n +  9*Y_n

Therefore, it suffices to determine the minimal representatives (or seed
solutions) of the generalized Pell equation X**2 - 5*Y**2 = -4. These are
(1,1), (4,2), (11,5).
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
    orbits = [(1,1), (4,2), (11,5)]
    N = len(orbits)
    x0, y0 = orbits[k%N]
    return _pell_solution(k//N, x0, y0)

N = 15

print(problem, explanation, f"First {N} golden nuggets", sep="\n")

k = 0
i = 0
while k != N:
    i += 1
    X,_ = general_pell_solution(i)

    if (X-1) % 5 != 0: continue

    n = (X-1)//5

    m = isqrt(5*n*n + 2*n + 1)
    assert m*m == 5*n*n + 2*n + 1

    p = - n - 1 + m
    q = 2*n
    A_F = p*q / (q**2 - p*q - p**2)
    assert isclose(A_F, n)

    k += 1
    print(f"\t{k}. A_F({p}/{q}) == {n}")

print(f"\nAnswer: {N}-th golden nugget == {n}")
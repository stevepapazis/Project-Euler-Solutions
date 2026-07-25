problem = """\
Problem 918: Recursive Sequence Summation

The sequence a(n) is defined by a(1):=1, and then recursively for n>=1:
                a(2*n) = 2*a(n)
              a(2*n+1) = a(n) - 3*a(n+1)

The first ten terms are 1, 2, -5, 4, 17, -10, -17, 8, -47, 34.

Define S(N) = Σ_{n=1}^N a(n). You are given S(10) = -13.

Find S(10**12).
"""

explanation = """
Notice that a(2*n) + a(2*n+1) == -3*(a(n+1) - a(n)).
Therefore
    Σ_{k=1}^{2*n} a(k) == a(1) + 2*a(n) - 3*(a(n)-a(1)) == 4 - a(n),
                        S(2*n) == 4 - a(n)
                               and
                      S(2*n+1) == 4 - 3*a(n+1)

"""

_a = dict()
_a[1]=1

def a(n):
    if n in _a:
        return _a[n]
    if n%2 == 0:
        _a[n] = 2*a(n//2)
    else:
        _a[n] = a(n//2) - 3*a(n//2+1)
    return _a[n]

def S(n):
    if n%2 == 0:
        return 4 - a(n//2)
    else:
        return 4 - 3*a(n//2+1)

print(
    problem,
    explanation,
    f"The first ten a(n) values: {', '.join([str(a(n)) for n in range(1,11)])}.",
    f"{S(3)=}",
    f"Answer: {S(10**12)=}",
    sep="\n"
)
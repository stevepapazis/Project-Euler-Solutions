import numpy as np

problem = """\
Problem 932: 2025

For the year 2025: 2025 == (20 + 25)**2

Given positive integers a and b, the concatenation ab we call a 2025-number if ab == (a+b)**2.
Other examples are 3025 and 81.
Note 9801 is not a 2025-number because the concatenation of 98 and 1 is 981.

Let T(n) be the sum of all 2025-numbers with n digits or less. You are given T(4)==5131.

Find T(16).
"""

explanation = """
Let a,b,k be integers such as a*10**k+b == (a+b)**2. Then
                a*10**k + b == (a+b)**2
        <=> a*10**k - a + 0.25 == (a+b-0.5)**2
        <=> b ==  - a + 0.5 + (a*10**k-a+0.25)**.5
"""

print(problem, explanation, "2025-numbers with less than 16 digits:", sep="\n")

answer = np.uint64(0)
for k in range(1, 9):
    a = np.arange(1, 10**k)
    b = -a + .5 + (a*10**k - a + .25)**.5
    b_int = np.round(b)
    i = np.nonzero( (b_int >= 10**(k-1)) & (b-b_int==0) )
    a = np.uint64(a[i])
    b = np.uint64(b_int[i])
    answer += ((a+b)*(a+b)).sum()
    print("\n".join([f"\t{_1}_{_2}" for _1,_2 in zip(a, b)]))

print("\nAnswer: ", answer)
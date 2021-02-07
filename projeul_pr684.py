problem = """\
Problem 684: Inverse Digit Sum

Define s(n) to be the smallest number that has a digit sum of n.
For example s(10)=19.

Let S(n) := sum( s(k) for k in range(1,n) ). You are given S(20) = 1074.

Further let f_i be the Fibonacci sequence defined by f_0 = 0, f_1 = 1 and
f_(i+2) := f_i + f_(i+1) for all i>=0.

Find the sum of S(f_i) when i = 2,...,90 modulo 10**9+7.
"""

explanation = """\
If m is the smallest number with a digit sum of n, its digits in the left
should be smaller than its digits in the right.

For example all of the numbers: 199, 289, 298, 1099 have a digit sum of 19
but 199 is the smallest.

In general, it is easy to prove that the smallest number with a digit sum
of n has the form (n%9)999...999 where the digit 9 appears n//9 times.
Since (n%9)999...999 == (n%9+1)000...000 - 1, we use the geometric series
formula to get a closed-form expression for S.
"""

modulo = 10**9+7

def mod_s(n): 
    return ( (n%9+1)*pow(10,n//9,modulo) - 1 ) % modulo
    
def mod_S(n):
    k = n//9
    r = n%9
    return (
            6 * pow(10,k,modulo)
          - 9 * k
          - 6
          + sum([ mod_s(9*k+i) for i in range(r,0,-1) ])
        ) % modulo 

def fib(n, a=0, b=1):
    if n==0: return a
    else: return fib(n-1, b, a+b)

solution = sum([ mod_S(fib(i)) for i in range(90,1,-1) ]) % modulo

print(
    problem,
    "\n\n\n",
    explanation,
    "\n\n\nSum of S(f_i) when i = 2,...,90 modulo 10**9+7 = ",
    solution,
    sep="",
    end=""
    )

input()







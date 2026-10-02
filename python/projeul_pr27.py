print(
"""Problem 27: Quadratic primes

Euler discovered the remarkable quadratic formula: n**2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n**2+ 79n + 1601 was discovered, which produces 80
primes for the consecutive values n = 0 to 79. The product of the coefficients,
79 and 1601, is 126479.

Considering quadratics of the form:
n**2 + an + b, where |a| <= 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""
)

print("\nSolution:")

import time

def search(l,n):
    i=0; end=len(l)
    while l[i] < n:
        i+=1
        if i+1 == end: break
    if l[i] == n: return i


start=time.time()

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
stop_at = len(primes)

for p in range(1001,997**2+2,2):
    for k in primes[1:stop_at]:
        if p%k==0:
            break
        if k*k > p:
            primes.append(p)
            break

print(f"Found all primes up to {primes[-1]} in {time.time()-start} seconds")

n_best = 0
a_best = 0
b_best = 0


for b in primes:
    if b > 1000: break

    for a in range(-999,1000,2):
        p = lambda n: n**2+a*n+b

        for n in range(0,b): # p(b) % b == (b**2 + a*b + b) % b == 0
            if p(n) <= 0 or search(primes, p(n)) == None:
                break

        if n > n_best:
            n_best = n
            a_best = a
            b_best = b

print(f"\nThe expression n**2 {'+' if a_best>0 else '-'} {abs(a_best)}*n + {b_best} produces {n_best} primes:")
print(", ".join([str(n**2 + a_best*n + b_best) for n in range(n_best)]))
print(f"\nSolution found in {time.time()-start} seconds")
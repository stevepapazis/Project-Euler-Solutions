"""Problem 46: Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2*1**2
15 = 7 + 2*2**2
21 = 3 + 2*3**2
25 = 7 + 2*3**2
27 = 19 + 2*2**2
33 = 31 + 2*1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

from bisect import bisect as bisect


p = [3,5,7,11,13]
def primes(end, l=p):
    for i in range(l[-1]+2, end, 2):
        stop = int(i**.5)+1
        flag = 1
        for j in l:
            if i%j==0:
                flag =0
                break
            elif j>stop: break
        if flag: l.append(i)

flag = 1
end = 1000
primes(end)
n =  35
while flag:
    if p[bisect(p, n)-1]==n: n+=2
    else:
        try:
            c = 0
            while p[c]<n:
                if (((n-p[c])/2)**.5).is_integer(): break
                c+=1
            else:
                flag = 0
                print("Solution:",n)
            n+=2
        except IndexError:
            end+=1000
            primes(end)
    

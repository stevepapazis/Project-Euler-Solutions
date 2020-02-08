"""Problem 123: Prime square remainders

Let p(n) be the nth prime: 2, 3, 5, 7, 11, ..., and let r(n) be the remainder
when (p(n)−1)**n + (p(n)+1)**n is divided by p(n)**2.
For example, when n = 3, p(3) = 5, and 4**3 + 6**3 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10**9 is 7037.

Find the least value of n for which the remainder first exceeds 10**10."""


"""
r(n) = [(p(n)−1)**n + (p(n)+1)**n]%p(n)**2
     = [Σ nCr*p(n)**i*( 1+(-1)**n-i ), 0<=i<=n]%p(n)**2
     = 1 + (-1)**n + n*p(n)*(1+(-1)**(n-1)),  n in N
     
Since r(2k) = 2, n must be odd to be the first integer so that r(n)>10**10.

Let R(k) = r(2k+1) = 2*(2k+1)*p(2k+1).

It can be proven that for the nth prime p(n) the following expression holds:
0<=ln(n)+ln(ln(n))-p(n)/n<=1, n>=2.
From this expression we conclude that if R(k)>10**10 then 10117<=k<=10539.
p(2*10117+1) = 227609 
p(2*10539+1) <= 258306 """

n = 2*10118+1 
not_skip = 1 #skip even numbers
for p in range(227609, 258306, 2):
    end = int(p**.5)+1
    for i in range(3, end, 2):
        if p%i==0: break
    else:
        if not_skip:
            if n*p>5000000000:
                print("Solution:", n)
                break
            not_skip = 0
        else:
            not_skip = 1
        n+=1
        

"""Problem 145: How many reversible numbers are there below one-billion?

Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and
409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and
904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10**9)?"""


helpme = """\
If there is an m such as m = reverse(n), then n = reverse(m).

Let n be a reversible number and s(n) = n + reverse(n).

n = abc...xyz

   abc...xyz
 + zyx...cba
-------------
   sss...sss

n[i] == reverse(n)[L-i-1]     where i in {0, 1, 2, ..., L-1 }

>>> s(n)[0] = ( n[0] + reverse(n)[0] )%2 == 1
 => ( n[0]%2==1 & reverse(n)[0]%2==0 ) or ( n[0]%2==0 & reverse(n)[0]%2==1 )

>>>  n[-2] + reverse(n)[-2] > 9 & ( n[L-1] + reverse(n)[L-1] )%2==1
 => s[L-1]%2 == ( n[L-1] + reverse(n)[L-1] + 1 )%2 == 0
 => n is not reversible
If n is reversible, then n[-2] + reverse(n)[-2] < 10.

>>> ( n[0] + reverse(n)[0] )%2 == 1
 =>  n[1] + reverse(n)[1] < 10
 => ( n[2] + reverse(n)[2] )%2 == 1
 => .....
 => .....
 => ( n[2*i] + reverse(n)[2*i] )%2 == 1     when i is a non negative integer
 =>  n[2*i+1] + reverse(n)[2*i+1] < 10     when i is a non negative integer

Let w(L) be the number of reversible numbers with L digits. Then:
w(4*k+1) = 0     when k is a non negative integer
w(2*k) = 20*30**(k-1)     when k is a positive integer
w(4*k+3) = 20*20**k*25**k*5     when k is a positive integer
"""

def w(L):
    if L%2==0:
        return 20*30**(L//2-1)
    if L%4==1:
        return 0
    if L%4==3:
        return 20**(L//4+1)*5**(2*(L//4)+1)

print("Solution:", sum([w(L) for L in range(1,10)]))

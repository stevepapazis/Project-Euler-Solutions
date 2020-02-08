"""Problem 33: Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator."""


helpme= """\
@ ab/cb = a/c <=> 10ac+bc = 10ac+ba <=> bc = ba <=> ( b=0 or a=c )
@ ba/bc = a/c <=> 10bc+ac = 10ab+ca <=> 10bc = 10ab <=> ( b=0 or a=c )
@ ba/cb = a/c < 1 => ( a < c && b < c )
  ba/cb = a/c <=> 10bc+ac = 10ac+ab <=> 9c(a-b) = b(c-a)
  a < c <=> 0 < b(c-a) = 9c(a-b) <=> a > b => b < a < c
  There are no a, b, c such as 9c(a-b) = b(c-a) and b < a < c.  
@ ab/bc = a/c <=> 10ac+bc = 10ab+ac <=> 9a(c-b) = b(a-c)
  a < c <=> 0 < b(a-c) = 9a(c-b) <=> c < b => a < c < b
  9a(c-b) = b(a-c) => (a,b,c) in { (4,9,8), (1,6,4), (1,9,5), (2,6,5) }

49/98*16/64*19/95*26/65 = 1/2*1/4*1/5*2/5 = 1/100
"""
print("Solution:",100)
input()

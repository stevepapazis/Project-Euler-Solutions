"""Problem 74: Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of
its digits is equal to 145: 1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers
that link back to 169; it turns out that there are only three such loops that
exist:
169->363601->1454->169
871->45361->871
872->45362->872

It is not difficult to prove that EVERY starting number will eventually get
stuck in a loop. For example:
69->363600->1454->169->363601->(1454)
78->45360->871->45361->(871)
540->145->(145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty
non-repeating terms?
"""

factorials=(1,1,2,6,24,120,720,5040,40320,362880)
d={169:3,871:2,872:2,2:1,145:0,40585:0,1:1}

def production(n,remaining=0,d=d):
    try: return d[n]+remaining
    except KeyError:
        string=str(n)
        remaining+=1
        s=production(sum(factorials[int(i)] for i in string),remaining)
        d[i]=s-remaining+1
        return s
c=0
for i in range(3,1000000):
    if production(i)==60:
        c+=1
        
#PossibleSolution=402

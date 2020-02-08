"""Problem 30: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:
1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits."""

dict=dict()
for i in range(10):
    dict[i]=i**5
list=[]
for a in range(2):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        s=0
                        for i in (a,b,c,d,e,f):
                            s+=dict[i]
                        s2=100000*a+10000*b+1000*c+100*d+10*e+f
                        if s2==s: list.append(s)

print(sum(list[2:]))

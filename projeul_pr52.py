"""Problem 52: Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits."""

flag=1
for t in range(1000):
    for b in range(7):
        if t>100: a='0'
        elif t>10: a='00'
        else: a='000'
        strn=''.join(['1',str(b),a,str(t)])
        lst=[i for i in strn]
        lst.sort()
        n=int(strn)
        for i in range(2,7):
            temp=str(i*n)
            ltemp=[j for j in temp]
            ltemp.sort()
            if ltemp!=lst: break
        else:
            flag=0
            break
s=1000
while flag:
    for b in range(7):
        strn=''.join(['1',str(b),str(s)])
        lst=[i for i in strn]
        lst.sort()
        n=int(strn)
        for i in range(2,7):
            temp=str(i*n)
            ltemp=[j for j in temp]
            ltemp.sort()
            if ltemp!=lst: break
        else:
            flag=0
            break
    s+=1
        
for i in range(1,7):
    print(i*n)

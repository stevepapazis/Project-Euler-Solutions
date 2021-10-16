"""Problem 39: Integer right triangles
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p<=1000, is the number of solutions maximised?"""

from time import time as ti
s=ti()
p=2
d=0
max=[0]
while p<=1000:
    c=0
    for y in range(1,p//2):
        t=(y**2+4*p*y)**.5-y
        x=-1
        if t%2==0:
            x=p-t/2
            if (y-x)%2==0:
                c+=1
                d=y
        if d==x:break
    if c/2>max[0]:max=[c/2,p]
    p+=2
print(ti()-s)
print('Solution:',max[1])

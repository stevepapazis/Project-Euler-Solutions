"""Problem 99: Largest exponential

Comparing two numbers written in index form like 2^11 and 3^7 is not difficult,
as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt, a text file containing one thousand lines with a
base/exponent pair on each line, determine which line number has the
greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.
"""

import math
log=math.log2

data=[]
file=open('base_exp.txt')
for i in file:
    data.append([int(j) for j in (i.replace('\n','')).split(',')])
max=[data[0][1]*log(data[0][0]),0]
for i in range(1000):
    if data[i][1]*log(data[i][0])>max[0]:
        max=(data[i][1]*log(data[i][0]),i)

print(max[0],max[1]+1)

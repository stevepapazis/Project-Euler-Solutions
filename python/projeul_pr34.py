"""Problem 34: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""

#1st solution
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

dictionary=dict([['0',1]])
for i in range(1,10):
    dictionary[str(i)]=factorial(i)
outputlist=[]
d=[0,0,0,0,0,0,0]
string=str
integer=int
for d[6] in range(2):
    for d[0] in range(10):
        for d[1] in range(10):
            for d[2] in range(10):
                for d[3] in range(10):
                    for d[4] in range(10):
                        for d[5] in range(10):
                            s2=string(1000000*d[6]+100000*d[0]+10000*d[1]+1000*d[2]+100*d[3]+10*d[4]+d[5])
                            s=0
                            for j in str(s2):
                                s+=dictionary[j]
                            if integer(s2)==s: outputlist.append(s)
print(sum(outputlist[2:]),end='\n')

#2nd solution
factorials={'0':1,'1':1,'2':2,'3':6,'4':24,'5':120,'6':720,'7':5040,'8':40320,'9':362880}
for i in range(3,1476265):
    temp=str(i)
    L=len(temp)
    sums=0
    counter=0
    while counter<L:
        if sums<=i:
            sums+=factorials[temp[counter]]
        else:
            break
        counter+=1
    if sums==i:
        print(i)
        

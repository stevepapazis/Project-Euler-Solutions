"""Problem 49: Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in
this sequence?
"""

from bisect import bisect_left

def permutations(n):
    qwer=set()
    string=[n//1000,(n-n//1000*1000)//100,(n%100-n%10)//10,n%10]
    for a in string:
        sa=string[:]
        sa.remove(a)
        for b in sa:
            sb=sa[:]
            sb.remove(b)
            for c in sb:
                sc=sb[:]
                sc.remove(c)
                if sc[0]%2==0: continue
                try:
                    t=a*1000+b*100+c*10+sc[0]
                    if primes[bisect_left(primes,t)]==t:
                        qwer.add(t)
                except: pass
    if len(qwer)<3: return []
    qwer=list(qwer)
    qwer.sort()
    l=len(qwer)
    sums=dict()
    for n in range(1,l):
        for i in range(n):
            for j in range(i,l-n,n):
                try:
                    sums[qwer[j+n]-qwer[j]][0]+=1;sums[qwer[j+n]-qwer[j]][1].add(qwer[j+n])
                except:
                    sums[qwer[j+n]-qwer[j]]=[1,set([qwer[j],qwer[j+n]])]
    out=[]
    for i in sums.items():
        if i[0]==3330:
            if i[1][0]==2:
                i[1][1]=sorted(list(i[1][1]))
                for j in range(0,i[1][0]):
                    if i[1][1][j]+i[0]!=i[1][1][j+1]:
                        break
                else:
                    out.append(i[1][1])
    return out

primes = []
append = primes.append
for i in range(1117,9999,2):
    r = int(i**.5)
    for j in range(3,r,2):
        if i%j==0:break
    else:
        if '0' not in str(i):
            append(i)

output=[]
for i in primes:
    temp=permutations(i)
    for i in temp:
        if i not in output:
            output.append(i)
print(output)

solution=296962999629

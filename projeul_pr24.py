"""Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.

The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""

def fu(l,t):
    m=[]
    for i in l:
        if i not in t:
            m.append(i)
    return m

def s():
    d=[0,0,0,0,0,0,0,0,0,0]
    xrange=(0,1,2,3,4,5,6,7,8,9); c=0
    for d[0] in xrange:
        for d[1] in fu(xrange,[d[0]]):
            for d[2] in fu(xrange,(d[0],d[1])):
                for d[3] in fu(xrange,(d[0],d[1],d[2])):
                    for d[4] in fu(xrange,(d[0],d[1],d[2],d[3])):
                        for d[5] in fu(xrange,(d[0],d[1],d[2],d[3],d[4])):
                            for d[6] in fu(xrange,(d[0],d[1],d[2],d[3],d[4],d[5])):
                                for d[7] in fu(xrange,(d[0],d[1],d[2],d[3],d[4],d[5],d[6])):
                                    for d[8] in fu(xrange,(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7])):
                                        for d[9] in fu(xrange,(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8])):
                                            c+=1
                                            if c==1000000:
                                                print("Solution:", end = ' ')
                                                for i in range(10):
                                                    print(d[i],end='')
                                                return
s()
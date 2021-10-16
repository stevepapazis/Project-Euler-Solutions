"""Problem 166: Criss Cross

A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.
It can be seen that in the grid

            6 3 3 0
            5 0 4 3
            0 7 1 4
            1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of each
diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that
each row, each column, and both diagonals have the same sum?"""



"""
If S= Σ a[i][k] = Σ a[k][i] = Σ a[k][k] = Σ a[3-k][k],for k in {0,1,2,3} then:
    S=r17+r13+r12+r10
    a[0][0]=r17
    a[0][1]=-r16+r15-r12+r11+r10
    a[0][2]=r16-r15+r13+r12-r11
    a[0][3]=r12
    a[1][0]=-r17+r16+r15+r14-r13
    a[1][1]=-r15+r13+r12
    a[1][2]=r17-r16+r10
    a[1][3]=r17-r14+r13
    a[2][0]=r17-r16-r15-r14+r13+r12+r10
    a[2][1]=r16
    a[2][2]=r15
    a[2][3]=r14
    a[3][0]=r13
    a[3][1]=r17+r12-r11
    a[3][2]=r11
    a[3][3]=r10
"""

a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]     #0<=a[i][j]<=9
counter=0

for r17 in range(0,10):
    for r16 in range(0,10):
        for r10 in range(0,10):
            if 10>r17-r16+r10>-1:
                for r11 in range(0,10):
                    for r12 in range(0,10):
                        if 10>r17+r12-r11>-1:
                            for r15 in range(0,10):
                                if 10>-r16+r15-r12+r11+r10>-1:
                                    for r13 in range(0,10):
                                        if 10>r16-r15+r13+r12-r11>-1 and 10>-r15+r13+r12>-1:
                                            for r14 in range(0,10):
                                                if 10>r17-r16-r15-r14+r13+r12+r10>-1 and 10>-r17+r16+r15+r14-r13>-1 and 10>r17-r14+r13>-1:
                                                    counter+=1

print("Solution",counter)

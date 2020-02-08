"""\\Problems - Project Euler.htm"""


def u(n)->'1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10':
    #return n**3    #test sequence from the example
    S=1
    for i in range(1,11): S+=(-n)**i
    return S
    
def detA(n)->'det(A(n))':
    p=1
    for i in range(2,n+1):
        for j in range(1,n):
            if i==j: break
            p*=i-j
    return p

def Xi(n, m, detAiB)->'X = A**(-1)*B':
    AB = [ [ [ i**j, 1 ] for i in range(1, n+1) ] for j in range(n) ]
    AB[m] = [ [ u(i), 1 ] for i in range(1, n+1) ]
    detAiB = [ 1, detAiB ]
    for i in range(n-1):
        for j in range(i+1, n):
            l = [AB[j][i][0]*AB[i][i][1], AB[i][i][0]*AB[j][i][1]]
            for k in range(i, n):
                AB[j][k][0] = AB[j][k][0]*AB[i][k][1]*l[1] - AB[j][k][1]*l[0]*AB[i][k][0]
                AB[j][k][1] = l[1]*AB[j][k][1]*AB[i][k][1]
                if AB[j][k][0]%AB[j][k][1]==0: AB[j][k] = [ AB[j][k][0] // AB[j][k][1], 1 ]
        if AB[i+1][i+1][0]==0: return 0
        detAiB[0] *= AB[i+1][i+1][0]
        if detAiB[0]%detAiB[1]==0:
            detAiB[0] //= detAiB[1]
            detAiB[1] = 1
        if detAiB[0]%AB[i+1][i+1][1]==0: detAiB[0] //= AB[i+1][i+1][1]
        else: detAiB[1] *= AB[i+1][i+1][1]
    return detAiB[0]/detAiB[1]

def OP(k):
    if k == 1: M = [u(1)]
    else:
        temp = detA(k)
        M = []
        for i in range(k): M.append(Xi(k, i, temp))
    return M

SumofFITofBOPofUn = 0
k = 1
coefficients = OP(k)
while coefficients != [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]: #[0,0,0,1]
    m = k+1
    while 1:
        OPkm = sum([coefficients[i]*m**i for i in range(k)])
        if OPkm != u(m):
            SumofFITofBOPofUn+=OPkm
            break
        m+=1
    k+=1
    coefficients = OP(k)
print("Solution: ", int(SumofFITofBOPofUn))
input()
    
#PROBLEM IN PRECISION
"""
def Xi(n, m, detAiB):
    AB = [[i**j for i in range(1,n+1)] for j in range(n)]
    AB[m] = [u(i) for i in range(1,n+1)]
    multiply = 0
    for i in range(n-1):
        for j in range(i+1, n):
            l = AB[j][i] / AB[i][i]
            for k in range(i, n):
                AB[j][k] -= l*AB[i][k]
        if AB[i+1][i+1]==0: return 0
        elif multiply: detAiB *= AB[i+1][i+1]
        elif detAiB / AB[i+1][i+1] < 1:
            multiply = 1
            detAiB = AB[i+1][i+1]/detAiB
        else: detAiB /= AB[i+1][i+1]
    return detAiB
#"""

#WRONG (FUCKED THE MATH BEHIND IT)
"""
def X(p):
    M = []
    for k in range(1, p+1):
        M.append((u(k)-sum([u(j)*j**(k-j) for j in range(1, k)])))
        for i in range(2, p):
            if i!=k:
                 M[k-1]*=i**(i-1)-sum([i**(j-1)*j**(i-j) for j in range(1, i) if j!=k])-u(i)/u(k)*k**(i-1)
                 M[k-1]/=i**(i-1)-sum([i**(j-1)*j**(i-j) for j in range(1, i)])
        M[k-1]/=k**(k-1)-sum([k**(j-1)*j**(k-j) for j in range(1, k)])
    return M
\"""
def X2(p):
    M = []
    temp = detA(p)
    for k in range(1, p+1):
        last = []
        t = (u(k)-sum([u(j)*j**(k-j) for j in range(1, k)]))
        if temp%t==0: M.append(temp//t)
        else:
            M.append(temp)
            last.append(t)
        multiply = 0
        for i in range(2, p):
            if i!=k:
                t = i**(i-1)-sum([i**(j-1)*j**(i-j) for j in range(1, i) if j!=k])-u(i)/u(k)*k**(i-1)
                if multiply:
                    M[k-1]*= t
                elif M[k-1]/t<1:
                    multiply=1
                    if t%M[k-1]==0: M[k-1] = t//M[k-1]
                    else:
                        last.append(M[k-1])
                        M[k-1] = t
                else:
                    if M[k-1]%t==0: M[k-1]//=t
                    else: last.append(t)
            for j in last:
                M[k-1]/=j
    return M
#"""

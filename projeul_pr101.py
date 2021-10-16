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

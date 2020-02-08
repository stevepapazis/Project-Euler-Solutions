def numberOfHexagonsInAllTrianglesWithSidesSmallerThan(N):
    S = 0
    for n in range(3, N + 1):
        S += int( n//3 * ( n//3 + 1 ) * ( n**2 + n - 1 - 4*n*( n//3 ) - 3/2*( n//3 ) + 9/2*( n//3 )**2 ) )
    return S//4  
print("The answer is: ", numberOfHexagonsInAllTrianglesWithSidesSmallerThan(12345))
input()

problem = """Problem 76: Counting summations

It is possible to write five as a sum in exactly six different ways:
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?"""


temp = dict() #temp is used to store values to be used again later

def w(N,i):
    """Returns the number of ways that N can be written as the sum of
non-negative integers that are less than i.

N = 1*N = 1+1+...+1+1 <=> w(N,1) = 1

0 = 0+0+0+... <=> w(0,i) = 1

If N<=i then w(N,i) = w(N,N).

N = (N-1) + 1
  = (N-2) + 2 = (N-2) + 1 + 1
  = (N-3) + 3 = (N-3) + 2 + 1 = (N-3) + 1 + 1 + 1
  = ....
  = 1 + 1 + 1 + ... + 1 + 1 + 1

w(N,i) = sum( w(N-n,n) for n in range(1, i+1 ) )"""
    
    if N == 0: return 1
    if i == 1: return 1  
    elif i >= N:
        i = N
    S = 0
    for n in range(1, i+1 ):
        try:
            S += temp[(N-n, n)]
        except KeyError:
            temp[(N-n, n)] = w(N-n, n)
            S += temp[(N-n, n)]
    return S

#w(100,100) also includes the sum 100+0
print(problem, "\n\nAnswer: ", w(100,100)-1, sep='\n')  
input()

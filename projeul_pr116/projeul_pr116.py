"""\\Problem 116 - Project Euler.htm"""

def function(lengthcolour, n):
    black = 50 - n*lengthcolour
    end = black + n + 1
    p = 1
    if black > n:
        for i in range(black+1, end): p*=i
        n+=1
        for i in range(2, n): p/=i
    else:
        for i in range(n+1, end): p*=i
        black+=1
        for i in range(2, black): p/=i
    return int(p)

S = 0
for tilelength in (2, 3, 4):
    tilenumber = 1
    while tilenumber*tilelength <= 50:
        S+=function(tilelength, tilenumber)
        tilenumber+=1
    
print("Solution:",S)
input()

def function(black, red, green, blue):
    n = 1
    c1 = 2
    c2 = 2
    c3 = 2
    end = black + red + green + blue +1
    for i in range(red + 1, end):
        n*= i
        while c1 <= green and n%c1==0:
            n//= c1
            c1+= 1
        while c2 <= blue and n%c2==0:
            n//= c2
            c2+= 1
        while c3 <= black and n%c3==0:
            n//= c3
            c3+= 1
    green+= 1
    blue+= 1
    black+= 1
    for i in range(c1 + 1, green): n//= c1
    for i in range(c2 + 1, blue): n//= c2
    for i in range(c3 + 1, black): n//= c3
    return n

s=0
for r in range(0, 26):
    for g in range(0, 17):
        for b in range(0, 13):
            if 50 >= 2*r + 3*g + 4*b:
                s+=function(50 - 2*r - 3*g - 4*b, r, g, b)
                
print("Solution:", s)
input()

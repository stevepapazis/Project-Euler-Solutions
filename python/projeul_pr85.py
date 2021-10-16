"""Problem 85: Counting rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2
contains eighteen rectangles.
Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution."""

#A rectangular grid measuring x by y contains 1/4*x*(x+1)*y*(y+1) rectangles.
#s(x,y)=1/4*x*(x+1)*y*(y+1)

#s(x,y)=s(y,x)
#s(x,x)=2*10^6 => x~=53

#s(x,y)=2*10^6 => x=(-1+(1+32*10**6/(y**2+y))**.5)/2


min_approximation = 2*10^6
result = 0
for y in range(1,54):
    x = (-1+(1+32*10**6/(y**2+y))**.5)/2
    x_int = int(x)
    if x_int + .5 < x: x_int+=1
    temp = 1/4*x_int*(x_int+1)*y*(y+1) - 2000000
    if -min_approximation < temp < min_approximation:
        result = x_int*y
        min_approximation = temp

print("Solution:", result)
input()

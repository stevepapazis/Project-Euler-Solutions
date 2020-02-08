"""\\Problem 173 - Project Euler.htm"""

helpme = "projeul_pr173_helpme.jpeg"

c=0
for i in range(1,250000):
    c+=int((-i+(i**2+1000000)**.5)/2)
print("Solution:", c)
input()

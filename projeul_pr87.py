"""Problem 87: Prime power triples

The smallest number expressible as the sum of a prime square, prime cube, and
prime fourth power is 28. In fact, there are exactly four numbers below fifty
that can be expressed in such a way:
28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime
square, prime cube, and prime fourth power?"""

#  x>84  =>  x**2+x**3+x**4 > 50386896 > 50000000

p = [3,5,7,11,13]
for i in range(17, 7071, 2):
    stop = int(i**.5)+1
    flag = 1
    for j in p:
        if i%j==0:
            flag =0
            break
        elif j>stop: break
    if flag: p.append(i)
p.insert(0,2)

numbers = set()

for a in p:
    a2 = a**2
    for b in p:
        b3=b**3
        if a2+b3>50000000: break
        s=a2+b3
        for c in p:
            c4=c**4
            if s+c4>50000000: break
            numbers.add(s+c4)
print("Solution:",len(numbers))

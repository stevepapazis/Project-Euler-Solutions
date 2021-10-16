"""Problem 32: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital. HINT: Some products can be obtained in
more than one way so be sure to only include it once in your sum."""

output = set()
list = ('1','2','3','4','5','6','7','8','9')
for i in range(1,10000):
    for j in range(1,100):
        p = i*j
        q = str(p)+str(i)+str(j)
        if len(q)!=9:
            continue
        for k in list:
            if k not in q: break
        else:
            output.add(p)

print("Solution:",sum(output))

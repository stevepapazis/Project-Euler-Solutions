"""Problem 41: Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?"""
   
def rotationsGenerator(l):
    length = len(l)
    if length==2:
        return [l, [i for i in reversed(l)]]
    else:
        p = rotationsGenerator(l[:-1])
        temp = []
        for i in p:
            for j in range(0, length):
                t = i.copy()
                t.insert(j,  l[-1])
                temp.append(t)
    return temp

def is_it_prime(n):
    end = int(n**.5) + 1
    for i in range(3, end, 2):
        if n%i==0: return False
    return True


tobetested1 = [7,6,5,4,3,2,1]
tobetested2 = [4,3,2,1]
a1 = rotationsGenerator(tobetested1)
a2 = rotationsGenerator(tobetested2)

max = 0
for i in a1:
    if i[-1] in (2,4,5,6,8,0):
        continue
    value = int(''.join([str(j) for j in i]))
    if is_it_prime(value) and max<value:
        max = value
if max==0:
    for i in a2:
        if i[-1] in (2,4,5,6,8,0):
            continue
        value = int(''.join([str(j) for j in i]))
        if is_it_prime(value) and max<value:
            max = value
                
print("Solution:", max)

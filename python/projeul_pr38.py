"""Problem 38: Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:
    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9
and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?"""

list = ('1','2','3','4','5','6','7','8','9')
max = 918273645
for n in range(3,11):
    m = 1
    s = ''
    while len(s)<10:
        s = ''
        for i in range(1,n):
            s+= str(m*i)
        if len(s)==9:
            for i in list:
                if i not in s:
                    break
            else:
                if max<int(s): max = int(s)
        m+=1

print("Solution:",max)
input()

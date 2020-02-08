'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''


num1=''' One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve\
 Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen '''.split(' ')
num2='''Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety Hundred Thousand'''.split()


#1st solution
x={}
x2={}
for i,j in zip(range(0,20),num1):
    x[i]=j
for i,j in zip(range(2,10),num2):
    x2[i]=j


def _3digit(n):
    for i in range(0,10):
        if n//100==i:
            if n%100==0:
                return str(x.get(i)+' Hundred ')
            return str(x.get(i)+' Hundred and ')

def _2digit(n):
    if (n%100-n%10)/10==0:
        return str(x.get(0))
    if (n%100-n%10)/10==1:
        return str(x.get(n%10+10))
    for i in range(2,10):
        if (n%100-n%10)/10==i:
            return str(x2.get(i))    

def _1digit(n):
    if n%100<20 and n%100>10:
            return 0
    for i in range(0,10):
        if n%10==i:
            return i


for i in range(20,1000):
    if i>=100:
        x[i]= _3digit(i) + _2digit(i) + ' ' + str(x.get(_1digit(i)))
    else:
        x[i]= _2digit(i) + ' ' + str(x.get(_1digit(i)))
x[1000]= x[1] + ' ' + num2[-1]

l=''
for i in range(1,1001):
    for j in x[i].split(' '):
        l+=j
print(len(l))



#2nd Solution
l=''
for i in range(1,10):
    l+=str(x.get(i))*190
for i in range(10,20):
    l+=str(x.get(i))*10
l+=num2[8]*900+'and'*891+num2[9]+str(x.get(1))
for i in range(2,10):
    l+=str(x2.get(i))*100  
print(len(l))

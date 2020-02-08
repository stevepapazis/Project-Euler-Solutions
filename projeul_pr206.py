"""Problem 206: Concealed Square

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit.
"""

#1_2_3_4_5_6_7_8_9_0=x**2<=>x=a*10
#x in (1010101030, 1389026570)

for b in ("30","70"):
    for i in range(101010,1000000):
        s=str(int('10'+str(i)+b)**2)
        for j in range(10):
            if s[2*j]!=str((j+1)%10): break
        else: print(s)
for b in ("30","70"):
    for i in range(1000000,3890266):
        s=str(int('1'+str(i)+b)**2)
        for j in range(10):
            if s[2*j]!=str((j+1)%10): break
        else: print(int(s)**.5)

#answer=1389019170

problem = """Problem 92: Square digit chains

A number chain is created by continuously adding the square of the digits
in a number to form a new number until it has been seen before.
For example:
44->32->13->10->->1->1
85->89->145->42->20->4->16->37->58->89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually
arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?"""

def function(n):
    while 1:
        s=(n%10)*(n%10)
        while n>0:
            n//=10
            s+=(n%10)*(n%10)
        n=s
        if n==1:
            return 0
        elif n==89:
            return 1

list=[0,0,1]   
count89=1      #2->89
for i in range(3,568):       #abcdefg<10000000 a,b,c,d,e,f,g in {1,2,...,9}=>a**2+b**2+...+g**2<9**2+9**2+9**2+9**2+9**2+9**2+9**2=7*81=567
    t=function(i)
    list.append(t)
    count89+=t
for i in range(568,10000000):
    n=i
    s=(n%10)*(n%10)
    while n>0:
        n//=10
        s+=(n%10)*(n%10)
    count89+=list[s]

print(problem, '\n\n', "Solution: ", count89, sep='')
input()

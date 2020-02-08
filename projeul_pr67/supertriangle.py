try:
    file=open('supertriangleoutput.txt')
except:
    import supertriangleoutputcreator
    file=open('supertriangleoutput.txt')
    
global vertical, relationships
vertical, relationships, c = [],[[[0,1]]], 0
for i in file:
    vertical.append([])
    relationships.append([])
    relationships[c+1]=relationships[c]+[[0,1]]
    k=i.split(' ')
    l=len(k)-1                            #k's last element is '\n'
    for j in range(l):
        vertical[c].append(int(k[j]))
    c+=1
del relationships[-1],relationships[-2]   #deleting useless lines of relationships
c-=1

helpme='''From bottom upwards in rows and left to right, cross out numbers that
produce a sum less than a maximum sum.
relationships[i][j]=[] or [x] or [0,1]; where x in {0,1}

vertical:
...............
......| (i,j) | .......
......|(i+1,j)|(i+1,j+1)|.......
.......................................

If relationships[i][j]=[], then the sums that contain vertical[i][j] as their
j term are not to be considered in search of the maximum sum. Otherwise, if 
relationships[i][j]=[x], then from all the sums containing vertical[i][j] as
their j term, we are going to consider only those that contain vertical[i+1][j+x]
as their j+1 term in the evaluation of the maximum sum.
'''

for i in range(1,c):                #initialising process 
    if vertical[c][i-1]<vertical[c][i]: relationships[c-1][i-1]=[1]
    else: relationships[c-1][i-1]=[0]
c-=1

def sum(n,j):
    if n==c: return vertical[c][j]
    else:
        if len(relationships[n][j])==1: return sum(n+1,j+relationships[n][j][0])+vertical[n][j]
        elif len(relationships[n][j])==0: return 0
        else:
            sums=[sum(n+1,j),sum(n+1,j+1)]
            if sums[0]<sums[1]:relationships[n][j]=[1]
            else: relationships[n][j]=[0]
            return vertical[n][j]+max(sums)       

c+=1
for i in range(c,-1,-1):
    for j in range(i+1):
        sum(i,j)

s=sum(0,0)

""" Problem 81: Path sum(two ways)

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is equal to 2427.

2427 = 131 + 201 + 96 + 342 + 746 + 422 + 121 + 37 + 331 

        131	673	234	103	18
        201	96	342	965	150
        630	803	746	422	111
        537	699	497	121	956
        805	732	524	37	331

Find the minimal path sum in 'matrix', a file containing a 80 by 80 matrix, from
the top left to the bottom right by only moving right and down.
"""

file=open('matrix')
string=file.readlines()
matrix=[i.replace('\n','').split(',') for i in string]
for i in range(80):
    for j in range(80):
        matrix[i][j]=[0, int(matrix[i][j])]
matrix[79][79] = 2*[matrix[79][79][1]] 

for i in range(78,-1,-1):
    matrix[79][i][0]=matrix[79][i+1][0]+matrix[79][i][1]
    matrix[i][79][0]=matrix[i+1][79][0]+matrix[i][79][1]
    for j in range(78,i,-1):
        if matrix[j][i+1][0]>matrix[j+1][i][0]:
            matrix[j][i][0]=matrix[j+1][i][0]+matrix[j][i][1]
        else:
            matrix[j][i][0]=matrix[j][i+1][0]+matrix[j][i][1]
        if matrix[i][j+1][0]>matrix[i+1][j][0]:
            matrix[i][j][0]=matrix[i+1][j][0]+matrix[i][j][1]
        else:
            matrix[i][j][0]=matrix[i][j+1][0]+matrix[i][j][1]
    if matrix[i][i+1][0]>matrix[i+1][i][0]:
        matrix[i][i][0]=matrix[i+1][i][0]+matrix[i][i][1]
    else:
        matrix[i][i][0]=matrix[i][i+1][0]+matrix[i][i][1]

print('Solution:', matrix[0][0][0])

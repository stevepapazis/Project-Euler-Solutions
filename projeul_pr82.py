"""Problem 82: Path sum(three ways)

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the
left column and finishing in any cell in the right column, and only moving up,
down, and right, is indicated in red and bold; the sum is equal to 994.

994 = 201 + 96 + 342 + 234 + 103 +18

        131	673	234	103	18
        201	96	342	965	150
        630	803	746	422	111
        537	699	497	121	956
        805	732	524	37	331
	
Find the minimal path sum in 'matrix', a file containing a 80 by 80 matrix, from
the left column to the right column."""

with open('matrix') as file:
    string = file.readlines()
rows = [i.replace('\n','').split(',') for i in string]
matrix = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for i in range(80):
    for j in range(80):
        matrix[j].append(int(rows[i][j]))
        rows[i][j] = 0
rows[79] = matrix[79]


def row_pass(m, n):
    result = [0]
    
    for i in range(1,79):
        min = n[i]

        s = 0
        for j in range(i-1,-1,-1):
            s+=m[j]
            if s >= min: break
            elif s + n[j] < min: min = s + n[j]
        s = 0
        for j in range(i+1,80):
            s+=m[j]
            if s >= min: break
            elif s + n[j] < min: min = s + n[j]
        result.append(min + m[i])
        
    min = n[0]
    s = 0
    for j in range(1,80):
        s+=m[j]
        if s >= min: break
        elif s + n[j] < min: min = s + n[j]
    result[0] = min + m[0]
    
    min = n[79]
    s = 0
    for j in range(78,-1,-1):
        s+=m[j]
        if s >= min: break
        elif s + n[j] < min: min = s + n[j]
    result.append(min + m[79])

    return result


for i in range(79, 0, -1):
    rows[i-1] = row_pass(matrix[i-1], rows[i])

print('Solution:', min(rows[0]))

problem = """Problem 91: Right triangles with integer coordinates"""

explanation = """\
There are three distinct cases for a right triangle OPQ with non-negative
integer coordinates, where P = (p1, p2) and Q = (q1, q2) such that p1<=q1,
p2>=q2 and 0<=p1,p2,q1,q2<=n:

    1. O == right angle, it is easy to calculate that there exist n**2
                         right triangles with these specifications.
                         
    2. P == right angle. Therefore we obtain
         OP**2 + PQ**2 = OQ**2 <=> p1**2 + p2**2 - p1*q1 - p2*q2 = 0
         We can count the triangles in this case by finding all the
         solutions of this equation that respect the constraints.
    
    3. Q == right angle, the number of these triangles equals the number
                         of right triangles in the second case because
                         of the x=y line symmetry.                         
"""

n = 50

trianglesWithOasRightAngle = n**2

trianglesWithPasRightAngle = 0

for q1 in range(0,n+1):
    for p1 in range(0,q1+1):
        for p2 in range(0, n+1):
            for q2 in range(0, p2+1):
                if p1**2 + p2**2 - p1*q1 - p2*q2 == 0:
                    if p1==q1 and p2==q2: continue       #no triangle is formed
                    if p1==0 and p2==0: continue       #no triangle is formed
                    if q1==0 and q2==0: continue       #no triangle is formed
                    trianglesWithPasRightAngle += 1

trianglesWithQasRightAngle = trianglesWithPasRightAngle


print(problem, explanation, sep="\n\n")        
input(
    "Number of right triangles with non-negative integer coordinates<="
    + str(n)
    + ": "
    + str(
        trianglesWithOasRightAngle
        +trianglesWithPasRightAngle
        +trianglesWithQasRightAngle
        )
    )

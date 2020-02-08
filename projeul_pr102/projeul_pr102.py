"""Problem 102: Triangle containment

Three distinct points are plotted at random on a Cartesian plane, for which
-1000<=x<=1000 and -1000<=y<=1000, such that a triangle is formed.

Consider the following two triangles:
A(-340,495), B(-153,-910), C(835,-947)
X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ
does not.

Using triangles.txt, a 27K text file containing the co-ordinates of one thousand
"random" triangles, find the number of triangles for which the interior contains
the origin.

NOTE: The first two examples in the file represent the triangles in the example
given above."""

#ANALYTIC GEOMETRY ROCKS!!!

file=open('triangles.txt')
string=file.readlines()
file.close()

triangles=[]
for i in string:
    triangles.append([int(j) for j in (i.replace('\n','')).split(',')])

def line(vector,point):
    #The equation of a line(l) that is vertical on a vector AB=(a,b) and 
    #passes through a point P(c,d) is ax+by-ac-bd=0.
    #Let f(x,y)=ax+by-ac-bd.
    #If P, C, D are points on a plane, as the vectors CD and AB are paralell
    #and C is lying on the line(l) then:
    #   ~ f(P)>0 <=> P is lying on the half-plane that D is also lying on 
    #   ~ f(P)=0 <=> P is lying on the line(l)
    #   ~ f(P)<0 <=> P is lying on the other half-plane that D is lying on
    #
    #f(O(0,0))=-ac-bd
    return -vector[0]*point[0]-vector[1]*point[1]   

O=(0,0)
c=0
for i in triangles:
    A, B, C = (i[0],i[1]), (i[2],i[3]), (i[4],i[5])
    AB=(B[0]-A[0],B[1]-A[1])
    AC=(C[0]-A[0],C[1]-A[1])
    ABxAC_z=AB[0]*AC[1]-AB[1]*AC[0]
    if ABxAC_z<0:
        B, C = (i[4],i[5]), (i[2],i[3])
        AB=(B[0]-A[0],B[1]-A[1])
        AC=(C[0]-A[0],C[1]-A[1])
        ABxAC_z=-ABxAC_z
    BC=(C[0]-B[0],C[1]-B[1])
    hxAB=(-ABxAC_z*AB[1],ABxAC_z*AB[0]) #hxAB=(ABxAC)xAB
    ACxh=(ABxAC_z*AC[1],-ABxAC_z*AC[0]) #ACxh=ACx(ABxAC)
    hxBC=(-ABxAC_z*BC[1],ABxAC_z*BC[0]) #hxBC=(ABxAC)xBC
    if line(hxAB,A)>0 and line(ACxh,A)>0 and line(hxBC,B)>0: c+=1
    elif line(hxAB,A)==0 and line(ACxh,A)==0 and line(hxBC,B)==0: print(i)

#second method
class line():
    def __init__(self,a,b):
        self.point1=a
        self.point2=b
    def equation(self,point):
        return (self.point2[1]-self.point1[1])*(point[0]-self.point1[0])-(self.point2[0]-self.point1[0])*(point[1]-self.point1[1])
    def same_halfspace(self,point1,point2):
        a1=self.equation(point1)
        a2=self.equation(point2)
        if a1>=0 and a2>=0:
            return True
        elif a1<=0 and a2<=0:
            return True
        else: return False
counter=0
for i in triangles:
    A, B, C = (i[0],i[1]), (i[2],i[3]), (i[4],i[5])
    lineAB=line(A,B)
    lineAC=line(A,C)
    lineBC=line(B,C)
    if lineAB.same_halfspace(C,O):
        if lineAC.same_halfspace(B,O):
            if lineBC.same_halfspace(A,O):
                counter+=1


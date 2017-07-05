#We want to make symbolic expressions for the co-rotational matrix, 
from sympy import *

B2 = zeros(3, 6)
D2 = zeros(3, 3)
#Create symbolic matrices
#Symbolic representation of C
C_sym = zeros(3,3)
c11 =symbols('c11')
c12 =symbols('c12')
c13 =symbols('c13')
c21 = symbols('c21')
c22 = symbols('c22')
c23 = symbols('c23')
c31 = symbols('c31')
c32 = symbols('c32')
c33 = symbols('c33')

#Symbolic representation of A
A_sym = zeros(3,3)
a11 =symbols('a11')
a12 =symbols('a12')
a13 =symbols('a13')
a21 = symbols('a21')
a22 = symbols('a22')
a23 = symbols('a23')
a31 = symbols('a31')
a32 = symbols('a32')
a33 = symbols('a33')

#Symbolic representation of B
B_sym = zeros(3,3)
b11 =symbols('b11')
b12 =symbols('b12')
b13 =symbols('b13')
b21 = symbols('b21')
b22 = symbols('b22')
b23 = symbols('b23')
b31 = symbols('b31')
b32 = symbols('b32')
b33 = symbols('b33')

C_sym=Matrix([[c11,c12,c13],[c21,c22,c23],[c31,c32,c33]])
B_sym=Matrix([[b11,b12,b13],[b21,b22,b23],[b31,b32,b33]])

A_sym=Matrix([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])

# find A=BC, B - new position, C - original position
#initialize \vec{k} = {k1,..,k4} representing an element's new position
k1 = zeros(1,3);
k2 = zeros(1,3);
k3 = zeros(1,3);
k4 = zeros(1,3);

#define symbols for each element
k1x = symbols('k1x')
k1y = symbols('k1y')
k1z = symbols('k1z')

k2x = symbols('k2x')
k2y = symbols('k2y')
k2z = symbols('k2z')

k3x = symbols('k3x')
k3y = symbols('k3y')
k3z = symbols('k3z')

k4x = symbols('k4x')
k4y = symbols('k4y')
k4z = symbols('k4z')

k1[0] = k1x; k1[1] = k1y; k1[2] = k1z;
k2[0] = k2x; k2[1] = k2y; k2[2] = k2z;
k3[0] = k3x; k3[1] = k3y; k3[2] = k3z;
k4[0] = k4x; k4[1] = k4y; k4[2] = k4z;

#But k's inside of B
B = zeros(3,3);

B = Matrix([(k2 - k1),(k3-k1),(k4-k1)]);
B=B.T

#Now we make vector of the original position
xzero1 = zeros(1,3);
xzero2 = zeros(1,3);
xzero3 = zeros(1,3);
xzero4 = zeros(1,3);

xzero1x = symbols('xzero1x')
xzero1y = symbols('xzero1y')
xzero1z = symbols('xzero1z')

xzero2x = symbols('xzero2x')
xzero2y = symbols('xzero2y')
xzero2z = symbols('xzero2z')

xzero3x = symbols('xzero3x')
xzero3y = symbols('xzero3y')
xzero3z = symbols('xzero3z')

xzero4x = symbols('xzero4x')
xzero4y = symbols('xzero4y')
xzero4z = symbols('xzero4z')

xzero1[0] = xzero1x; xzero1[1] = xzero1y; xzero1[2] = xzero1z;
xzero2[0] = xzero2x; xzero2[1] = xzero2y; xzero2[2] = xzero2z;
xzero3[0] = xzero3x; xzero3[1] = xzero3y; xzero3[2] = xzero3z;
xzero4[0] = xzero4x; xzero4[1] = xzero4y; xzero4[2] = xzero4z;

C = zeros(3,3);
C = Matrix([(xzero2 - xzero1),(xzero3-xzero1),(xzero4-xzero1)]);
#print B
C = C.T


#inverse C
C_inv = C_sym.inv();
A = B*C_inv
#Vectors of matrix A
a0 = A_sym[:,0];
a1 = A_sym[:,1];
a2 = A_sym[:,2];

#Gram-Schmit vectors
r0 = a0.normalized()

proj = Matrix([[r0.dot(a1)],[r0.dot(a1)],[r0.dot(a1)]])
r1= (a1-proj).normalized()
r2 = r0.cross(r1)

R = zeros(3,3)
R = Matrix([r0.T,r1.T,r2.T])

#Symbolic representation of R
R_sym = zeros(3,3)
R11 =symbols('R11')
R12 =symbols('R12')
R13 =symbols('R13')
R21 = symbols('R21')
R22 = symbols('R22')
R23 = symbols('R23')
R31 = symbols('R31')
R32 = symbols('R32')
R33 = symbols('R33')

R_large=zeros(12,12)
R_sym=Matrix([[R11,R12,R13],[R21,R22,R23],[R31,R32,R33]])
R_large[0,0] = R_sym
R_large[3,3] = R_sym
R_large[6,6] = R_sym
R_large[9,9] = R_sym
print R_large.rows, R_large.cols
print R_large





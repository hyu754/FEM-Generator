#2D M matrix
#symbolic integration of the M matrix
from sympy import *
E = symbols('young_E')
nu = symbols('nu')
M = zeros(3,3)
A = symbols('A')
rho = symbols('rho')
x = symbols('x')
y = symbols('y')
dt = symbols('dt')
xi = symbols('xi')
alpha = symbols('alpha')
beta1 = symbols('beta1')
beta2 = symbols('beta2')
a_i = symbols('a_i')
b_i = symbols('b_i')
c_i = symbols('c_i')
a_j = symbols('a_j')
b_j = symbols('b_j')
c_j = symbols('c_j')
a_k = symbols('a_k')
b_k = symbols('b_k')
c_k = symbols('c_k')
det_J = symbols('det_J')
thickness = symbols('thickness')
y23 = symbols('y23')
y31 = symbols('y31')
y12 = symbols('y12')
x32 = symbols('x32')
x13 = symbols('x13')
x21 = symbols('x21')

B2 = zeros(3, 6)
D2 = zeros(3, 3)

B2[0,0] = B2[2,1] = y23 / det_J
B2[0,2] = B2[2,3] = y31 / det_J
B2[0,4] = B2[2,5] = y12 / det_J
B2[1,1] = B2[2,0] = x32 / det_J
B2[1,3] = B2[2,2] = x13 / det_J
B2[1,5] = B2[2,4] = x21 / det_J

D2[0,0] = D2[1,1] = 1.0
D2[0,1] = D2[1,0] = nu
D2[2,2] = (1 - nu) / 2.0

integrand = B2.T * D2 * B2
integrand9 = (dt*xi*beta1+beta2*dt*dt/2.0)*integrand*(E/(1.0 - nu*nu))*thickness # this is for K matrix
b= zeros(3,1)


'''
N_i = (1/(2*A))*(a_i+b_i*x+c_i*y)
N_j = (1/(2*A))*(a_i+b_j*x+c_j*y)
N_k = (1/(2*A))*(a_k+b_k*x+c_k*y)

N_i = symbols('N_i')
N_j = symbols('N_j')
N_k = symbols('N_k')
'''
dim = 3
size_m =0
if dim == 2:
    N_i = symbols('xi')
    N_j = symbols('nu')
    N_k = symbols('1-xi-nu')
    N = Matrix([[N_i,0, N_j,0,1-N_i-N_j,0],[0,N_i, 0,N_j,0,1-N_i-N_j]])
    t = symbols('thickness')
    M = N.T*N*t
    #M = (1.0+dt*beta1*alpha)*M
    size_m = 6
elif dim ==3:
    M=zeros(3,3)
    N_i = symbols('xi')
    N_j = symbols('nu')
    N_k = symbols('Zeta')
    N_m = symbols('1-xi-nu-Zeta')
    N = Matrix([[N_i, 0,0, N_j,0, 0,N_k,0,0, 1 - N_i - N_j-N_k, 0,0], [0,N_i, 0,0, N_j,0, 0,N_k,0,0, 1 - N_i - N_j-N_k, 0],[0,0,N_i, 0,0, N_j,0, 0,N_k,0,0, 1 - N_i - N_j-N_k]])
    M = N.T * N
    size_m = 12
counter =0;
print ((N.T).shape)
b1 = symbols('b1')
b2= symbols('b2')
b3 = symbols('b3')
b[0,0] = b1
b[1,0] = b2
b[2,0] = b3


result_f_ext = N.T*b *det_J


for i in range(0,size_m):
    for j in range(0,size_m):
        #string = "M[" + str(i)+"]["+str(j) + "]=" + str(M[i,j])+";"
        answer = integrate(M[i, j], ('xi', 0, 1))

        answer2 = integrate(answer, ('nu', 0, 1))
        answer3 = integrate(answer2, ('Zeta', 0, 1)) *det_J*rho
        string = "K[36*offset" + "+" + str(counter) + "]="  + str(answer3) + ";"
        print "else if(offset_y ==" + str(counter)+"){"
        print string
        print "}"
        #For M matrix
        answer_m = integrate(M[i, j], ('xi', 0, 1))

        answer2_m = integrate(answer_m, ('nu', 0, 1))
        answer3_m = integrate(answer2_m, ('Zeta', 0, 1)) * det_J * rho
        # string = "M[" + str(i) + "][" + str(j) + "]=" + str(answer3) + ";"
        string_m =  str(answer3_m)
        string_m = string_m.replace("**2", "^2")
        string_m = string_m.replace("/3", "/3.0")
        string_m = string_m.replace("/4", "/4.0")
        string_m = string_m.replace("/6", "/6.0")

        string_m = string_m.replace("/12", "/12.0")


        #For K matrix
        #string = "K[144*offset" + "+" +str(counter) +"]=" + str(integrand[i, j]) + "+" + string_m+";"
        counter=counter+1
        string = string.replace("nu**2", "(nu*nu)")

        string = string.replace("det_J**2", "(det_J*det_J)")
        string = string.replace("x32**2", "(x32*x32)")
        string = string.replace("x21**2", "(x21*x32)")
        string = string.replace("x13**2", "(x13*x32)")
        string = string.replace("y23**2", "(y23*y23)")
        string = string.replace("y31**2", "(y31*y31)")
        string = string.replace("y12**2", "(y12*y12)")
        string = string.replace("dt**2", "(dt*dt)")




counter =0
for i in range(0,size_m):
    for j in range(0,size_m):
        #string = "M[" + str(i)+"]["+str(j) + "]=" + str(M[i,j])+";"
        answer = integrate(M[i, j], ('xi', 0, 1))

        answer2 = integrate(answer, ('nu', 0, 1))
        answer3 = integrate(answer2, ('Zeta', 0, 1)) *det_J*rho
        #string = "M[" + str(i) + "][" + str(j) + "]=" + str(answer3) + ";"
        string = "M[36*offset+"+str(counter)+"]=" + str(answer3) + ";"
        string = string.replace("**2", "^2")
        string = string.replace("/3","/3.0")
        string = string.replace("/4","/4.0")
        string = string.replace("/6","/6.0")

        string = string.replace("/12","/12.0")


        #print string
        counter = counter + 1
counter=0;
M_result = zeros(12,12)
lumped = symbols('det_J*rho/6')
for i in range(0, size_m):
    for j in range(0, size_m):
        # string = "M[" + str(i)+"]["+str(j) + "]=" + str(M[i,j])+";"
        answer = integrate(M[i, j], ('Zeta', 0, 1))

        answer2 = integrate(answer, ('nu', 0, 1))
        answer3 = integrate(answer2, ('xi', 0, 1)) * det_J * rho
        #string = "M[" + str(i) + "][" + str(j) + "]=" + str(answer3) + ";"
        M_result[i,j] = answer3
        string = "in_element->local_M[" + str(counter)+ "]=" + str(answer3) + ";"
        '''
        if i==j:
            string = "in_element->local_M[" + str(counter)+ "]=" + str(lumped) + ";"
        else:
            string = "in_element->local_M[" + str(counter)+ "]=" + str(0) + ";"
        '''
        counter=counter+1

        string = string.replace("**2", "^2")
        string = string.replace("0;", "0.0;")
        #print M[i, j]
        print string


        #print string
#print M_result
print 'beginning of f external'
print result_f_ext

counter=0;
for i in range(0, size_m):
    
    # string = "M[" + str(i)+"]["+str(j) + "]=" + str(M[i,j])+";"
    answer = integrate(result_f_ext[i], ('Zeta', 0, 1))

    answer2 = integrate(answer, ('nu', 0, 1))
    answer3 = integrate(answer2, ('xi', 0, 1)) 
    #string = "M[" + str(i) + "][" + str(j) + "]=" + str(answer3) + ";"
    #M_result[i,j] = answer3
    string = "in_element->f_body[" + str(counter)+ "]=" + str(answer3) + ";"
    
    counter=counter+1

    string = string.replace("**2", "^2")
    #string = string.replace("det_J^2", "det_J*det_J")
    #result_f_extstring = string.replace("0;", "0.0;")
    #print M[i, j]
    print string

'''
E = symbols('E')
nu = symbols('nu')
det_J = symbols('det_J')
B[0,0] = B[3,1] = B[5,2] = J_bar11;
B[1,1] = B[3,0] = B[4,2] = J_bar21;
B[2,2] = B[5,0] = B[4,1] = J_bar31;

B[0,3] = B[3,4] = B[5,5] = J_bar12;
B[1,4] = B[3,3] = B[4,5] = J_bar22;
B[2,5] = B[4,4] = B[5,3] = J_bar32;

B[0,6] = B[3,7] = B[5,8] = J_bar13;
B[1,7] = B[3,6] = B[4,8] = J_bar23;

B[2,8] = B[4,7] = B[5,6] = J_bar33;

B[0,9] = B[3,10] = B[5,11] = J_star1;
B[1,10] = B[3,9] = B[4,11] = J_star2;
B[2,11] = B[4,10] = B[5,9] = J_star3;


D[0,0] = D[1,1] = D[2,2] = (1.0 - nu);
D[0,1] = D[1,0] = D[0,2] = D[2,0] = D[1,2] = D[2,1] = nu;
D[3,3] = D[4,4] = D[5,5] = (1.0 - nu) / 2.0;
D=(E/(1-nu-2*nu*nu))*D*det_J / 6.0



print D
print B
print K
print result


result = B.T*D*B

print "start of local K"
sum = 0
for i in range(0,3):
    for j in range(0,3):
        string = "E_vector[" + "x" + "]" + "=" + str(result[i, j]) + ";"
        sum = sum+1
        'print string'
        'rint "if ((x == " +str(i)+")&&(y=="+str(j)+")){"+string+"} "'
        print "if ((x == " +str(sum)+")){"+string+"} "

'''
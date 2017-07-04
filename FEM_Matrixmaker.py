from sympy import *
B = zeros(6,12)

K = zeros(12,12)
D = zeros(6,6)

J_bar11 = symbols('J_bar11')
J_bar21 = symbols('J_bar21')
J_bar31 = symbols('J_bar31')
J_bar12 = symbols('J_bar12')
J_bar13 = symbols('J_bar13')
J_bar22 = symbols('J_bar22')
J_bar32 = symbols('J_bar32')
J_bar33 = symbols('J_bar33')
J_bar23 = symbols('J_bar23')
J_star1 = symbols('J_star1')
J_star2 = symbols('J_star2')
J_star3 = symbols('J_star3')

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
#D[3,3] = D[4,4] = D[5,5] = (1.0 - 2*nu) / 2.0;
D[3,3] = D[4,4] = D[5,5] = (1.0 - 2* nu) 
D=(E/(1-nu-2*nu*nu))*D*det_J / 6.0



rho = symbols('rho')
result = B.T*D*B
result_M = rho*B.T*B*det_J / 6.0

b= zeros(12,1)
b1x = symbols('b1x')
b1y = symbols('b1y')
b1z = symbols('b1z')
b2x = symbols('b2x')
b2y = symbols('b2y')
b2z = symbols('b2z')
b3x = symbols('b3x')
b3y = symbols('b3y')
b3z = symbols('b3z')
'''
b[0,0] = b1
b[1,0] = b2
b[2,0] = b3
result_f_ext = B.T*b *det_J/6.0
'''
'''
print D
print B
print K
print result
'''
print "start of local K"
sum = 0
for i in range(0,12):
    for j in range(0,12):
        #string = "E_vector[" + "x" + "]" + "=" + str(result[i, j]) + ";"
        string = "in_element->local_K" + "["+str(sum) + "]" + "=" + str(result[i, j]) + ";"
        sum = sum+1
        'print string'
        'rint "if ((x == " +str(i)+")&&(y=="+str(j)+")){"+string+"} "'
        string = string.replace("nu**2","nu*nu")
        string = string.replace("J_star1**2","J_star1*J_star1")
        string = string.replace("J_star2**2","J_star2*J_star2")
        string = string.replace("J_star3**2","J_star3*J_star3")

        string = string.replace("J_bar13**2","J_bar13*J_bar13")
        string = string.replace("J_bar23**2","J_bar23*J_bar23")
        string = string.replace("J_bar33**2","J_bar33*J_bar33")

        string = string.replace("J_bar12**2","J_bar12*J_bar12")
        string = string.replace("J_bar22**2","J_bar22*J_bar22")
        string = string.replace("J_bar32**2","J_bar32*J_bar32")

        string = string.replace("J_bar31**2","J_bar31*J_bar31")
        string = string.replace("J_bar32**2","J_bar32*J_bar32")
        string = string.replace("J_bar33**2","J_bar33*J_bar33")
        string = string.replace("J_bar11**2","J_bar11*J_bar11")
        string = string.replace("J_bar21**2","J_bar21*J_bar21")
        #print "if ((x == " +str(sum)+")){"+string+"} "3
        print string

sum = 0
count =0
for i in range(0,12):
    for j in range(0,12):
        string = "in_element->local_M" + "["+str(count) + "]" + "=" + str(result_M[i, j]) + ";"
        count= count + 1
        sum = sum+1
        'print string'
        'rint "if ((x == " +str(i)+")&&(y=="+str(j)+")){"+string+"} "'
        string = string.replace("J_star1**2","J_star1*J_star1")
        string = string.replace("J_star2**2","J_star2*J_star2")
        string = string.replace("J_star3**2","J_star3*J_star3")

        string = string.replace("J_bar13**2","J_bar13*J_bar13")
        string = string.replace("J_bar23**2","J_bar23*J_bar23")
        string = string.replace("J_bar33**2","J_bar33*J_bar33")

        string = string.replace("J_bar12**2","J_bar12*J_bar12")
        string = string.replace("J_bar22**2","J_bar22*J_bar22")
        string = string.replace("J_bar32**2","J_bar32*J_bar32")

        string = string.replace("J_bar31**2","J_bar31*J_bar31")
        string = string.replace("J_bar32**2","J_bar32*J_bar32")
        string = string.replace("J_bar33**2","J_bar33*J_bar33")
        string = string.replace("J_bar11**2","J_bar11*J_bar11")
        string = string.replace("J_bar21**2","J_bar21*J_bar21")



        print string
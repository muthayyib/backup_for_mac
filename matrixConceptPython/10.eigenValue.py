import math
def eigen_value(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    # val = (a+d)+math.sqrt((a+d)**2-4(a*d-c*b))/2
    eigval1 = ((a+d)+((a+d)**2-4*(a*d-c*b))**.5)/2
    eigval2 = ((a+d)-((a+d)**2-4*(a*d-c*b))**.5)/2
    print(eigval1)
    print(eigval2)

matrix = [[int(input("Enter elements"))for j in range(2)]for i in range(2)]
eigen_value(matrix)
def scalarMult(matrix, scalar):
    print("Scalar multiplied is: ")
    # below both code is true
    # sm = [[matrix[i][j]*scalar for j in range(col)]for i in range(row)]
    sm = [[j * scalar for j in i] for i in matrix]
    return sm


row = int(input("Enter number of row"))
col = int(input("Enter the number of coloumn"))
matrix = [[int(input(f"Enter element{i}{j}")) for j in range(col)] for i in range(row)]
scalar = int(input("Enter the scalar"))

result = scalarMult(matrix, scalar)
for i in result:
    print(i)

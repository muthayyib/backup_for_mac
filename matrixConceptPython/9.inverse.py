#inverse of 2*2 matrix,adj a, det a
def inverseMatrix(A):
    detA = A[0][0]*A[1][1]-A[0][1]*A[1][0]
    adjA = [[A[1][1], -A[0][1]],
            [-A[1][0],A[0][0]]]

    for i in adjA:
        print(i)
    print("Determinant of matrix:",detA)
    #list comprehension brain storming
    if detA==0:
        print("Inverse does not exist")
        return 0
    else:
        inverse = [[i/detA for i in adjA[j]]for j in range(len(adjA))]



        return inverse

A = [[int(input(f"Enter element{j} {i}: ")) for i in range(2)]for j in range(2)]
# A = [[1,2],
#      [3,4]]
result=inverseMatrix(A)
print("\nInverse of above matrix is: ")
for i in result:
    print(i)





#inverse of a 3*3 matrix
# def inverse33():
#     x = [[2, 3, 4],
#          [7, 8, 9],
#          [7, 1, 4]]
#     A = [[0 for j in range(3)] for i in range(3)]
#
#     A =[[x[1][1]*x[2][2]-x[2][1]*x[1][2],x[1][0]*x[2][2]-x[1][2]*[2][0]]
#         ]



# multliplication dot product
# def mult(x, y):
#     print("\nDot product of matrix x and y is:")
#     result = []
#     for i in range(3):
#         a = []
#         for j in range(3):
#             s = 0
#             for k in range(3):
#                 s = s + (x[i][k] * y[k][j])
#             a.append(s)
#         result.append(a)
#     for h in result:
#         print(h)
#
# x = [[2, 3, 4],
#      [7, 8, 9],
#      [7, 1, 4]]
#
# y = [[4, 8, 7],
#      [5, 4, 9],
#      [2, 3, 1]]
#
# mult(x, y)

#matrix mult input from user
def matrixMult(A,B,result):
    #iterate through rows of A
    for i in range(len(A)):
        #iterate throught colomn of B
        for j in range(len(B[0])):
            #iterate throgh rows of B
            for k in range(len(B)):
                result[i][j] +=  A[i][k]*B[k][j]
    return result
row1 = int(input("Enter the row of 1st matrix"))
col1 = int(input("Enter the col of 1st matrix"))
row2 = col1
print("Number of rows in 2nd matrix is ",col1)
col2 = int(input("Enter the number of col of 2nd matrix"))
print('Enter 1st matrix')
A = [[int(input()) for j in range(col1)] for i in range(row1)]
print("Enter 2nd matrix")
B = [[int(input()) for j in range(col2)] for i in range(row2)]
#creating a resultant matrix
result = [[0 for j in range(col2)] for j in range(row1)]

result = matrixMult(A,B,result)
for i in result:
    print(i)

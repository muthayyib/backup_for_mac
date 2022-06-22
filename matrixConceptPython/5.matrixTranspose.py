#transpose
def transpose(A, B):
    n = 4
    for i in range(n):
        for j in range(n):
            B[j][i] = A[i][j]
    return B


A = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4], ]
n=4
#create a matrix 0000 using list comprehesnigon
B = [[0 for i in range(4)] for j in range(n)]

trans = transpose(A, B)
print("\nResulatant transpose is")
for k in trans:
    print(k)
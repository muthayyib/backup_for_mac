def copy_matrix(x):
    copy = [[j for j in i]for i in x]
    for i in copy:
        print(i)

x = [[2, 3, 4],
     [7, 8, 9],
     [7, 1, 4]]
copy_matrix(x)
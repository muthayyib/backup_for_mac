def identity_matrix(n):
    idM = [[1 if i==j else 0 for j in range(n)]for i in range(n)]
    for i in idM:
        print(i)
identity_matrix(3)
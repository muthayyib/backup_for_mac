# addition method 1:
def addition(x, y):
    res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            res[i][j] = x[i][j] + y[i][j]

    for r in res:
        print(r)
    return res


addition(x, y)

# addition method 2
result1 = []


def addition2(x, y):
    for i in range(len(x)):
        temp = []
        for j in range(len(x[0])):
            temp.append(x[i][j] + y[i][j])
        result1.append(temp)
    return result1


sum = addition2(x, y)
for s in sum:
    print(s)


# addition method 3: list comprehension\
# newlist = [expression for item in iterable if condition == True]

def addition3(x, y):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
    for r in result:
        print(r)


addition3(x, y)


# substraction of asdfadsfasdfasdfadsf
def substraction(x, y):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    result = [[x[i][j] - y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
    for r in result:
        print(r)


substraction(x, y)

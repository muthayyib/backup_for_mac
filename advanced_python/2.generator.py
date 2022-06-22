def printuptotn():
    a =10+20
    b=85*85
    c =b-a
    yield a
    d=78/55
    yield c
    yield d

val = printuptotn()



print(val.__next__())
print(val.__next__())

print(next(val))
for i in val:
    print(i)


def test():
    i = 1
    while i<22:
        yield i*i
        i+=1
te = test()
print(te.__next__())
for j in te:
    print(j)
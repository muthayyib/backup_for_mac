""" sigle, multi-level, multiple, super, init, mro, """





class A:
    def __init__(self):
        print("init A")
    def hello(self):
        print("I am parent")

class B():
    def __init__(self):
        #if you want to call init of A

        super().__init__()

        print("init B")
class C(B,A):
    def __init__(self):
        #mro will take init of left ie. A
        super().__init__()
        print("init C")

obj = C()


class Hello:
    pass

class Hi:
    def __init__(self):
        print("in Hi")

class both(Hello,Hi):
    pass

obj1 = both()
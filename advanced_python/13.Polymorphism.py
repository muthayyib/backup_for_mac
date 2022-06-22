#duck typing

class Lenovo:
    def config(self):
        print("i5")
        print("Inter")
        print("fhd")
class Hp:
    def config(self):
        print("R3")
        print("Ryzen")
        print('HD')

class Laptop:
    def coding(self,system):
        system.config()

system = Lenovo()
lap = Laptop()
lap.coding(system)

#operator overloading I want add two objects
class Operator_loading:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    #overloads add method
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2+ other.m2
        s3 = Operator_loading(m1,m2)
        return s3

s1 = Operator_loading(20,55)
s2 = Operator_loading(36,45)
s3 = s1 + s2
print(s3.m1)


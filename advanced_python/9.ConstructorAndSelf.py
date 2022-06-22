class Person:
    #here passes object,name and age
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def compare(self,other):
        if self.age ==other.age:
            print("same")
        else:print("not same")

p1 = Person('Thayyib',27)
p2 = Person('Muneer',21)

p1.compare(p2)
#p1 goes to self and p2 passes to other:

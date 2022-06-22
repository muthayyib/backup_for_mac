#for eg. if I want to create a class called laptop, each student use different lap with diff
#conf. so I need a clas called Laptop inside student class

class Student:
    def __init__(self,name,age):
        self.name  = name
        self.age = age
        #laptop
        self.lap = self.Laptop()

    class Laptop:
        def __init__(self):
            self.brand  = 'Hp'
            self.cpu = 'i5'

s1 = Student('Christ',22).Laptop()
print(s1.lap)

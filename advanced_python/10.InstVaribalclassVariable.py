class Car:
    wheels = 4
    def __init__(self):
        self.name = 'Maruti'
        self.mil = 10
#change the value of class varibale it is common for all objects
Car.wheels =6
c1 = Car()
c2 = Car()
c2.name = "Brezza"
print(c1.name,c1.mil,c1.wheels)
print(c2.name,c2.mil,c2.wheels)
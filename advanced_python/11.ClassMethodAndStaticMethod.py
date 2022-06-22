class Student:
    school = "Telusko"

    #class method
    @classmethod
    def get_school_name(clas):
        return clas.school

    #static method no connection with class or object
    @staticmethod
    def static_m():
        print("I am static")

    #instance method
    def insta_m(self):
        self.name = "instagraa"
s1 = Student()
print(Student.static_m())
print(Student.get_school_name())
print(s1.static_m())


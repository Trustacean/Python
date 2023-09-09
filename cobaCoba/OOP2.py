class Person():
    def __init__(self,name,age):
        self.name = (name)
        self.age = age
    def display(self):
        print ("Person name: %s" % self.name)
        print ("Age: %s" % self.age)

class Student(Person):
    def __init__(self,name,age,section):
        Person.__init__(self,name,age)
        self.section = section
    def display(self):
        print ("Student name: %s" % self.name)
        print ("Age: %s" % self.age)
        print ("Section: %s" % self.section)

aPerson = Person("Don",23) 
aPerson.display()
aStudent = Student("Joey" , 10 , "Physics")
aStudent.display()

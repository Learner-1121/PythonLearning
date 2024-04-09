#parent class
class Person(object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)
    
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))

    def isPerson(self):
        return True

#child class
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post
        
        #invoking init of the parent class
        #Person.__init__(self,name,idnumber)
    
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
        Person.details(self)
    
    def isEmployee(self):
        return True
#creating object
a = Employee('Rahul', 886012, 200000, "Intern")
print(a.isPerson())
print(a.isEmployee())
a.display()
a.details()

#added new comment 202404091454



#class definition
class Dog:
    attr1 = "mammal"    #class attribute;
    
    def __init__(self,name): #similar to constructor in java
        self.name = name #Instance attribute

    def speak(self):
        print("My name is {}".format(self.name))

#Driver code
#Object instantiaton

Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

#Accessing class attributes

print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is a {}".format(Tommy.__class__.attr1))

#Accessing instance attributes
print("My name is {}".format(Rodger.name))

#Accessing class methods
Rodger.speak()
Tommy.speak()


# OOPS : Object Oriented Programming System
# Class : A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# Object : An object is an instance of a class. It is created from the class and has the attributes and methods defined in the class.
# Attribute : An attribute is a variable that is associated with an object. It is used to store information about the object.
# Method : A method is a function that is associated with an object. It is used to perform some action on the object or to retrieve some information from the object.
# Example of a class and an object in Python.

class Cars: # This is a class named Cars
    Company = "BMW" # This is an attribute of the class Cars
    Model = "M4"
    
    def race(self): # This is a method of the class Cars
        print("The car is racing")

car1 = Cars() # This is an object of the class Cars
print(car1.Company)  # This is an object attribute of the object car1
print(car1.Model)     
car1.race()  # This is an object method of the object car1

car2 = Cars()
print(car2.Company)
print(car2.Model)
car2.race()

car1.Model = "M3"
print(car1.Model)    # Output: M3
print(car2.Model)    # Output: M4
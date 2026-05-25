# INHERITANCE & ITS TYPES.
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.

# Types of Inheritance:
# 1. Single Inheritance: A child class inherits from a single parent class.
class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")
        
# Example of Single Inheritance:        
class Pens:
    def write(self):
        print("The pen is very good for Writing.")

class TypesOfPens(Pens):
    def types(self, type, color, price):
        self.type = type
        self.color = color
        self.price = price

pen1 = TypesOfPens()
pen1.write()  # Inherited from Pens class
pen1.types("Fountain", "Black", 15)  # Defined in TypesOfPens class



# 2. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")

class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")
        
# Example of Multilevel Inheritance:
class Cars:
    def start(self):
        print("The car is starting.")

class BMW(Cars):
    def model(self, model_name, price, color):
        self.model_name = model_name
        self.price = price
        self.color = color

class M4(BMW):
    def features(self):
        print("The M4 is a high-performance sports car.")
car1 = M4()
car1.start()  # Inherited from Cars class
car1.model("M4", 70000, "Red")  # Inherited from BMW class
car1.features()  # Defined in M4 class
    
    

# 3. Multiple Inheritance: A child class inherits from more than one parent class.
class Parent1:
    def parent1_method(self):
        print("This is the parent1 method.")

class Parent2:
    def parent2_method(self):
        print("This is the parent2 method.")

class Child(Parent1, Parent2):
    def child_method(self):
        print("This is the child method.")
        
# Example of Multiple Inheritance:
class Calling:
    def call(self):
        print("The phone can make calls.")
        
class Camera:
    def take_photo(self):
        print("The phone can take photos.")
        
class Smartphone(Calling, Camera):
    def features(self):
        print("The phone has multiple features.")
phone1 = Smartphone()
phone1.call()  # Inherited from Calling class
phone1.take_photo()  # Inherited from Camera class
phone1.features()  # Defined in Smartphone class
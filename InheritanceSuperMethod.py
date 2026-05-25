# Super Method : The `super()` function in Python is used to call a method from a parent class. It is particularly useful in inheritance scenarios where you want to extend or modify the behavior of a method inherited from a parent class.

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the __init__ method of the Parent class
        self.age = age

child_instance = Child("Alice", 10)
print(child_instance.name)
print(child_instance.age)

# Example of super()

class car:
    def __init__(self, type, model):
        self.type = type
        self.model = model
        
class BMW(car):
    def __init__(self, type, model, color, price):
        super().__init__(type, model)  # Call the __init__ method of the car class
        self.color = color
        self.price = price

car1 = BMW("SUV", "X5", "Blue", "$50000")
print(car1.type)
print(car1.model)
print(car1.color)
print(car1.price)
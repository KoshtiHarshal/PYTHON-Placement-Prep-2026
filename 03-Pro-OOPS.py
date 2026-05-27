# Q - Define a circle class to create a circle with radius r using constructor. Define an Area() method of the class which calculates the area of the circle. Define a perimeter() method of the class which calculates the perimeter of the circle.

class Circle: # This is a class named Circle
    def __init__(self, r):
        self.radius = r
        
    def Area(self):
        return (22/7) * self.radius ** 2
    
    def Perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(7)
print("Area of the circle is : ", c1.Area())
print("Perimeter of the circle is : ", c1.Perimeter())
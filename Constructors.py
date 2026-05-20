# Constructors are special methods in Python that are used to initialize the attributes of an object when it is created. The constructor method is defined using the __init__() function.
# Type of Constructors:
# 1. Default Constructor: A constructor that takes no parameters and initializes the attributes with default values.
# 2. Parameterized Constructor: A constructor that takes parameters and initializes the attributes with the values passed as arguments.

class Department:
    def __init__(self): # This is a default constructor
        self.name = "Computer Science" # This is an attribute of the class Department
        self.course = "B.Tech CSE"
class Student:      
    def __init__(self, name, age, year, div): # This is a parameterized constructor
        self.name = name # This is an attribute of the class Student
        self.age = age
        self.year = year
        self.div = div
        
s1 = Student("John", 20, "2nd Year", "A") # This is an object of the class Student created using the parameterized constructor
print(s1.name,"\n",s1.age,"\n",s1.year,"\n",s1.div)

d1 = Department() # This is an object of the class Department created using the default constructor
print(d1.name,"\n",d1.course) 

s2 = Student("Alice", 21, "3rd Year", "B")
print(s2.name,"\n",s2.age,"\n",s2.year,"\n",s2.div)
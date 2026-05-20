# Q - Create Student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student: # This is a class named Student
    def __init__(self, name, marks): # This is the constructor method that initializes the name and marks attributes of the Student class
        self.name = name # This is class attribute for name
        self.marks = marks
    
    def avg(self): # This is a method to calculate and print the average marks of the student
        average = sum(self.marks) / 3
        print("Average marks for " + self.name + " is " + str(average))
    
s1 = Student("Harshal", [85, 90, 96]) # This is object instance of the Student class with name "Harshal" and marks [85, 90, 96]
s1.avg() # This is method call to calculate and print the average marks for student s1

s2 = Student("Rohan", [92, 88, 95])
s2.avg()

s2.name = "Kaushal" # This is changing the name attribute of student s2 to "Kaushal"
s2.avg() # This will print the average marks for student s2 with the updated name
# Q - Define an Employee class with attributes role, department & salary. This class also has a showDetails() method. Create an Engineer class that inherits properties from Employee & has additional attribute : name & age.

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showDetails(self):
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        
class Engineer(Employee):
    def __init__(self, role, department, salary, name , age):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age
    def showDetails(self):        
        super().showDetails()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


eng1 = Engineer("Software Engineer", "IT", 80000, "Alice", 30)
eng1.showDetails()

eng2 = Engineer("Civil Engineer", "Construction", 75000, "Bob", 35)
eng2.showDetails()
class Account:
    def __init__(self, Name, Acc_no, Acc_pass):
        self.Name = Name
        self.Acc_no = Acc_no 
        self.__Acc_pass = Acc_pass # private attribute
        
    def printPass(self):
        print(self.__Acc_pass)  # accessing private attribute within the class
        
ACC1 = Account("ABC", "1234", "abcd")

print(ACC1.printPass()) # accessing private attribute through a public method of the class
print(ACC1.__Acc_pass) # trying to access private attribute outside the class will raise an error

class Person:
    def __init__(self):
        self.__name = "Anonymous" # protected attribute
    
    def __hello (self): # private method
        print("Hello", self.__name) # accessing private attribute within the private method
    
    def welcome(self): # public method to access private method
        self.__hello() # accessing private method through a public method of the class
        
p1 = Person()

print(p1.welcome()) # accessing private method through a public method of the class

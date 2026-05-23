# Q - Create Account class with 2 attributes - balance & account number. Create method for debit, credit & printing the balance.

class Account: # This is a class named Account
    def __init__(self, bal, acc): # This is the constructor method that initializes the balance and account attributes of the Account class
        self.balance = bal # This is class attribute for balance
        self.account = acc
    
    def debit(self,amount): # This is a method to debit the specified amount from the account balance
        self.balance -= amount
        print("Rs", amount ,"was debited from Acc_no.",self.account)
        print("The total balance is : ",self.get_balance())
        
    def credit(self , amount):
        self.balance += amount
        print("Rs", amount ,"was credited in Acc_no.",self.account)
        print("The total balance is : ",self.get_balance())
        
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000,1234)
acc1.debit(2000)
acc1.credit(5000)
acc2 = Account(10000,5678)
acc2.debit(3000)
acc2.credit(4000)
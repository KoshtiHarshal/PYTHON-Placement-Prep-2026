# FACTORIAL SERIES
def factorial(num):
    if(num == 1 or num==0):
        return 1
    else:
        return num * factorial(num-1)
    
num = int(input("Enter the number for factorial : "))
print("The factorial of the number",num,"is : ",factorial(num))



# FIBONACCI SERIES
def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return (n-1) + (n-2)


n = int(input("Enter the number for fibonacci : "))
print("The Fibonacci Series is : ",fibonacci(n))
    

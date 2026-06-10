# Stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle.
# Basic operation of Stack.
# 1. push, 2. pop, 3. top, 4. isEmpty, 5. isFull

# Implementaion of stack
# 1. Through LIST/ARRAY

# Creating Simple List and doing stack operation to assume it is stack
st = []

# Appending/Pushing values one by one using append() method.
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(6)

# Printing the Stack
print(st)

# Printing the removed value using pop() method.
print(st.pop())

print(st)

# Printing the Top/Last value of the Stack.
print(st[-1])


# 2. Using OOPS
class Stack: # Creating Stack class to modify List as a Stack. 
    def __init__(self):
        self.st = []

    def push(self,x): # Push/append funtion.
        self.st.append(x)

    def pop(self): # Pop function.
        if len(self.st) == 0:
            return -1 
        x = self.st[-1]
        self.st.pop()
        return x
    
    def top(self): # Top/Last value function.
        if len(self.st) == 0:
            return -1 
        return self.st[-1]
    
    def size(self): # Size function.
        return len(self.st)
    
stack = Stack() # Object Instance to create stack.

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(6)

print(stack.pop())

print(stack.top())

print(stack.size())

# Time Complexity of all the operation : O(1)
# Space Complexity : O(1)
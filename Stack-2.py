# Implementaion of stack
# 3. Through Linked List.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self,x):
        self.length += 1
        if self.top is None:
            self.top = Node(x)
            return
        else:
            newNode = Node(x)
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.top == None:
            return -1
        self.length -= 1
        x = self.top.data
        self.top = self.top.next
        return x
    
    def getTop(self):
        if self.top == None:
            return -1
        return self.top.data
    
    def size(self):
        return self.length
    
stack = Stack() # Object Instance to create stack.

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(6)

print(stack.pop())

print(stack.getTop())

print(stack.size())

# Time Complexity of all the operation : O(1)
# Space Complexity : O(1)
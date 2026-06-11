# Queue is a linear data structure that operates on the First In, First Out (FIFO) principle.
# Basic operation of Queqe.
# 1. push, 2. pop, 3. front, 4. isEmpty, 5. isFull

# Implementaion of Queqe
# 1. Through LIST/ARRAY using OOPS

class Queqe: # Creating Stack class to modify List as a Stack. 
    def __init__(self):
        self.qe = []
        self.front = -1

    def push(self,x): # Push/append funtion.
        if self.front == -1:
            self.front = 0
        self.qe.append(x)

    def pop(self): # Pop function.
        if len(self.qe) == 0:
            return -1 
        x = self.qe[self.front]
        self.front += 1
        if self.front == len(self.qe):
            self.front = -1
            self.qe = []
        return x
    
    def getFront(self): # Top/Last value function.
        if len(self.qe) == 0:
            return -1 
        return self.qe[self.front]
    
    def size(self): # Size function.
        if self.front == -1:
            return 0
        return len(self.qe) - self.front
    
que = Queqe() # Object Instance to create stack.

que.push(6) 
que.push(1)
que.push(2)
que.push(3)
que.push(4)

print(que.getFront())

print(que.pop())

print(que.getFront())

print(que.size())

# Time Complexity of all the operation : O(1)
# Space Complexity : O(1)
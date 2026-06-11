# Implementaion of stack
# 2. Through Linked List.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queqe:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0 

    def push(self,x):
        newNode = Node(x)
        self.length += 1

        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def pop(self):
        if self.front is None:
            return -1
        
        x = self.front.data
        self.front = self.front.next
        self.length -= 1 

        if self.front is None:
            self.rear = None
        return x
    
    def getFront(self):
        if self.front is None:
            return -1
        return self.front.data

    def size(self):
        return self.length
    
que = Queqe()

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


# There are four type of Queqe:
# 1. Simple Queqe
# 2. Circular Queqe
# 3. Priority Queqe
# 4. Double Ended Queqe
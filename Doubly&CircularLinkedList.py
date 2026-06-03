# Doubly Linked List implementation in Python
# A simple implementation of a doubly linked list in Python

class Node: # A class representing a node in a doubly linked list
    def __init__(self, data): # Constructor to initialize the node with data and set the next and prev pointers to None
        self.data = data # Store the data in the node
        self.next = None # Initialize the next pointer to None
        self.prev = None # Initialize the prev pointer to None
        
a = Node(1) # Create a new node with data 1 and assign it to variable a
b = Node(2)
c = Node(3)

a.next = b # Link node a to node b
b.prev = a # Link node b back to node a
b.next = c # Link node b to node c
c.prev = b # Link node c back to node b

head = a # The head of the doubly linked list is now node a, which points to node b, which points to node c, and each node also has a prev pointer to the previous node in the list.
tail = c # The tail of the doubly linked list is now node c, which points back to node b, which points back to node a.

# Accessing the data of the nodes in the doubly linked list
print(head.data)  # Output: 1
print(head.next.data)  # Output: 2
print(head.next.next.data)  # Output: 3

# Traversing the doubly linked list in forward direction
def traverse_forward(head): # Function to traverse the doubly linked list in forward direction starting from
    curr = head # Start traversing the doubly linked list from the head
    while curr != None:
        print(curr.data, end=" ") # Print the data of the current node followed by a space
        curr = curr.next # Move to the next node in the doubly linked list
traverse_forward(head) # Call the traverse_forward function to print the doubly linked list in forward direction
print() # Print a newline after traversing the doubly linked list in forward direction

# Traversing the doubly linked list in backward direction
def traverse_backward(tail): # Function to traverse the doubly linked list in backward direction starting from the tail
    curr = tail # Start traversing the doubly linked list from the tail
    while curr != None:
        print(curr.data, end=" ") # Print the data of the current node followed by a space
        curr = curr.prev # Move to the previous node in the doubly linked list
traverse_backward(tail) # Call the traverse_backward function to print the doubly linked list in backward direction
print() # Print a newline after traversing the doubly linked list in backward direction



# Circular Linked List implementation in Python
# A simple implementation of a circular linked list in Python
class Node: # A class representing a node in a circular linked list
    def __init__(self, data): # Constructor to initialize the node with data and set the next pointer to None
        self.data = data # Store the data in the node
        self.next = None # Initialize the next pointer to None

a = Node("A") # Create a new node with data 1 and assign it to variable a
b = Node("B")
c = Node("C")

a.next = b # Link node a to node b
b.next = c # Link node b to node c
c.next = a # Link node c back to node a, making the linked list circular

head = a # The head of the circular linked list is now node a, which points to node b, which points to node c, and node c points back to node a, forming a circular structure.

# Accessing the data of the nodes in the circular linked list
print(head.data)  # Output: A
print(head.next.data)  # Output: B
print(head.next.next.data)  # Output: C
print(head.next.next.next.data)  # Output: A (since it's circular, it goes back to the head after reaching the end of the list)

# Traversing the circular linked list
def traverse_circular(head): # Function to traverse the circular linked list starting from the head
    curr = head # Start traversing the circular linked list from the head
    while True:
        print(curr.data, end=" ") # Print the data of the current node followed by a space
        curr = curr.next # Move to the next node in the circular linked list
        if curr == head: # If we have come back to the head, we have completed one full traversal of the circular linked list
            break
traverse_circular(head) # Call the traverse_circular function to print the circular linked list
print() # Print a newline after traversing the circular linked list


# Traversing the circular linked list in reverse direction
def traverse_circular_reverse(head): # Function to traverse the circular linked list in reverse direction starting from the head
    curr = head # Start traversing the circular linked list from the head
    prev = None # Initialize a variable to keep track of the previous node
    while True:
        print(curr.data, end=" ") # Print the data of the current node followed by a space
        prev = curr # Update the previous node to the current node
        curr = curr.next # Move to the next node in the circular linked list
        if curr == head: # If we have come back to the head, we have completed one full traversal of the circular linked list
            break
traverse_circular_reverse(head) # Call the traverse_circular_reverse function to print the circular linked list in reverse direction
print() # Print a newline after traversing the circular linked list in reverse direction
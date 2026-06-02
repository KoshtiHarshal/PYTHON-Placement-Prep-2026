class Node: # A class representing a node in a linked list
    def __init__(self, data): # Constructor to initialize the node with data and set the next pointer to None
        self.data = data # Store the data in the node
        self.next = None

a = Node(1) # Create a new node with data 1 and assign it to variable a
b = Node(2)
c = Node(3)
a.next = b # Link node a to node b
b.next = c
head = a # The head of the linked list is now node a, which points to node b, which points to node c

print(head.data)  # Output: 1
print(head.next.data)  # Output: 2
print(head.next.next.data)  # Output: 3

# Traversing the linked list
def traverse(head): # Function to traverse the linked list starting from the head
    curr = head # Start traversing the linked list from the head
    while curr != None:
        print(curr.data, end=" ") # Print the data of the current node followed by a space
        curr = curr.next # Move to the next node in the linked list

traverse(head) # Call the traverse function to print the linked list
print() # Print a newline after traversing the linked list

# inserting a new node at the beginning of the linked list
new_node1 = Node(0) # Create a new node with data 0
new_node1.next = head # Point the new node's next to the current head of the linked list
head = new_node1 # Update the head of the linked list to the new node
traverse(head) # Call the traverse function to print the linked list after inserting the new node at the beginning
print() # Print a newline after traversing the linked list

# inserting a new node at the end of the linked list
new_node2 = Node(4) # Create a new node with data 4
curr = head # Start traversing the linked list from the head
while curr.next != None: # Traverse until the last node is reached
    curr = curr.next
    curr.next = new_node2 # Point the last node's next to the new node, effectively inserting it at the end of the linked list

traverse(head) # Call the traverse function to print the linked list after inserting the new node at the end
print() # Print a newline after traversing the linked list
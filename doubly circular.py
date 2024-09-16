class node:
    def __init__(self,data) -> None:
        self.data=data 
        self.next=None
        self.prev=None


node1=node(1)
node2=node(2)
node3=node(3)
node4=node(4)
node5=node(5)
node6=node(6)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node1


node1.prev=node6
node6.prev=node5
node5.prev=node4
node4.prev=node3
node3.prev=node2
node2.prev=node1

print("foreword traversal")
current=node1
start=node1
print(current.data,end=" ->")
current=current.next

while current!=start:
    print(current.data,end=' ->')
    current=current.next 
print("over")

print("reverse traversal")
current=node6
start=node6
print(current.data,end=" ->")
current=current.prev

while current!=start:
    print(current.data,end=" ->")
    current=current.prev
print("over")


# The code you’ve written implements a circular doubly linked list, where each node has both next and prev pointers, allowing traversal in both forward and reverse directions. Let's break it down:

# Class Definition:

# The class node includes data, next, and prev attributes. next points to the next node in the list, and prev points to the previous node.
# Circular Linked List:

# Six nodes are created and linked to form a circular doubly linked list, where:
# The next pointer of node6 points to node1 (forming a circle).
# The prev pointer of node1 points to node6 (closing the circle in reverse).
# Forward Traversal:

# You start from node1 and traverse the list using the next pointers until you return to node1, printing the data of each node.
# Reverse Traversal:

# You start from node6 and traverse backward using the prev pointers, printing the data of each node until you return to node6.
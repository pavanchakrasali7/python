# doubly linked list is the collection of item in order that we can traverse through the list from both te direction like forword or backword
# it  contains the 3 fields 
#     1)data:-it contains the actual data/ value
#     2)next:- it contains the adress of the next field or it is pointing to the next node 
#     3)prev:-it contains the adress of the previous node or it is poiting to the previous node 

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)

node1.next=node2

node2.prev=node1
node2.next=node3

node3.prev=node2
node3.next=node4

node4.prev=node3

print("forword traversal")
currentnode=node1
while currentnode:
    print(currentnode.data, end=" ->")
    currentnode=currentnode.next
print("null")

print("backword traversal")
currentnode=node4
while currentnode:
    print(currentnode.data, end=' <-')
    currentnode=currentnode.prev
print("null")
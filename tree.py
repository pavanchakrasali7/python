class Treenode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

def preorder(node):
        if node is None:
            return
        print(node.data,end=" ,")
        preorder( node.left)
        preorder( node.right)

def inorder(node):
        if  node is None:
            return 
        inorder( node.left)
        print( node.data,end=" ")
        inorder( node.right)

def postorder(node):
        if  node is None:
            return
        postorder( node.left)
        postorder( node.right)
        print( node.data,end=" ")





root=Treenode(13)
nod1=Treenode(7)
nod2=Treenode(5)
nod3=Treenode(8)
nod4=Treenode(11)
nod5=Treenode(5)
nod6=Treenode(6)

root.left=nod1
root.right=nod2
nod1.left=nod3
nod2.right=nod4
nod1.right=nod5
nod2.left=nod6
print("inorder traversal")
inorder(root)
print("preorder traversal")
preorder(root)

print("post ordertraversal")
postorder(root)

        
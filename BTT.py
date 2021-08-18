"""
#     Depth  First Traversal

1 = Inorder = (left root right)
2 = preorder = ( root left right)
3 = postorder = (left right  root)
"""

class node:
    def __init__(self,data):
        self.data = data
        self.left_node = None
        self.right_node = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def inorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self._inorder(self.root)
    def _inorder(self,current):
        if current:
            self._inorder(current.left_node)
            print(current.data,end=" ")
            self._inorder(current.right_node)
    def preorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self._preorder(self.root)
    def _preorder(self,current):
        if current:
            print(current.data,end=" ")
            self._preorder(current.left_node)
            self._preorder(current.right_node)
    def postorder(self):
        if(self.root == None):
            print("Tree Is Empty....")
        else:
            self._postorder(self.root)
    def _postorder(self,current):
        if current:
            self._preorder(current.left_node)
            self._preorder(current.right_node)
            print(current.data, end=" ")

ob1 = BinaryTree()
first = node(1)
second = node(2)
third = node(3)
fourth = node(4)
fifth = node(5)
sixth = node(6)
seventh = node(7)
ob1.root = first
first.left_node = second
first.right_node = third
second.left_node = fourth
second.right_node = fifth
third.left_node = sixth
third.right_node = seventh
print('Inorder : ',end=" ")
ob1.inorder()
print()
print("Preorder : ",end=' ')
ob1.preorder()
print()
print("Postorder : ",end=' ')
ob1.postorder()
print()



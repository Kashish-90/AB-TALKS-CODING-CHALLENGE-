# Binary Tree Traversal - Inorder

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Inorder Traversal (Left -> Root -> Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Creating Binary Tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

print("Inorder Traversal:")
inorder(root)

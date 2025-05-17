class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def preorder(self, node):
        if node:
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=' ')

bst = BST()
data = [50, 30, 70, 20, 40, 60, 80]

for item in data:
    bst.root = bst.insert(bst.root, item)

print("Preorder Traversal:")
bst.preorder(bst.root)

print("\nInorder Traversal:")
bst.inorder(bst.root)

print("\nPostorder Traversal:")
bst.postorder(bst.root)

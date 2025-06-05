# I am naming the variable per data type

class Node:
    def __init__(self, int_value, node_left=None, node_right=None):
        self.value = int_value
        self.left = node_left
        self.right = node_right

    def insertNode(self, int_value):
        if self.value == None:
            self.value = int_value
            return
        if int_value == self.value:
            print("You need to input a non existing data.")
            return
        elif int_value < self.value:
            if self.left:
                self.left.insertNode(int_value)
            else:
                self.left = Node(int_value)
        else:
            if self.right:
                self.right.insertNode(int_value)
            else:
                self.right = Node(int_value)

    def preOrder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.value, end=" ")
        if self.right:
            self.right.inOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.value, end=" ")


    def findNode(self, int_target):
        if int_target < self.value:
            if self.left == None:
                print(f"{int_target} does not exist.")
                return
            else:
                self.left.findNode(int_target)
        if int_target > self.value:
            if self.right == None:
                print(f"{int_target} does not exist.")
                return
            else:
                self.right.findNode(int_target)
        if self.value == int_target:
            print(f"{self.value} is found.")    

    def deleteNode(self, int_target):
        if int_target < self.value:
            if self.left:
                self.left = self.left.deleteNode(int_target)
            else:
                print(f"{int_target} does not exist.")
        elif int_target > self.value:
            if self.right:
                self.right = self.right.deleteNode(int_target)
            else:
                print(f"{int_target} does not exist.")
        else:
            if not self.left and not self.right:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            newNode = self.right
            while newNode.left:
                newNode = newNode.left
            self.value = newNode.value
            self.right = self.right.deleteNode(newNode.value)

        return self

            

node = Node(None)
while True:
    print("\n-- MENU --")
    print("1: Insert Node")
    print("2: Find Node")
    print("3: Delete Node")
    print("4: Traverse Tree")
    print("0: Exit")

    try:
        int_choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input.")
        continue

    match int_choice:
        case 1:
            int_value = int(input("Enter integer to insert: "))
            node.insertNode(int_value)
            print(f"{int_value} has been inserted .")

        case 2:
            if node:
                int_value = int(input("Enter integer to find: "))
                node.findNode(int_value)
            else:
                print("Tree is empty.")

        case 3:
            if node:
                int_value = int(input("Enter integer to delete: "))
                node = node.deleteNode(int_value)
            else:
                print("Tree is empty.")

        case 4:
            if not node:
                print("Tree is empty.")
                continue
            print("Choose traversal type:")
            print("  1. In-Order")
            print("  2. Pre-Order")
            print("  3. Post-Order")
            try:
                traversal_type = int(input("Enter traversal type: "))
            except ValueError:
                print("Invalid traversal choice.")
                continue

            match traversal_type:
                case 1:
                    print("In-Order: ", end="")
                    node.inOrder()
                case 2:
                    print("Pre-Order: ", end="")
                    node.preOrder()
                case 3:
                    print("Post-Order: ", end="")
                    node.postOrder()
                case _:
                    print("Invalid traversal option.")
            print()

        case 0:
            print("Goodbye!")
            break

        case _:
            print("Invalid choice.")
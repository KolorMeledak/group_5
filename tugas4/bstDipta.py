from graphviz import Digraph
class Node:
    def __init__(self, float_value, node_left=None, node_right=None):
        self.value = float_value
        self.left = node_left
        self.right = node_right

    def insertNode(self, float_value):
        if self.value == None:
            self.value = float_value
            return
        if float_value == self.value:
            print("You need to input a non existing data.")
            return
        elif float_value < self.value:
            if self.left:
                self.left.insertNode(float_value)
            else:
                self.left = Node(float_value)
        else:
            if self.right:
                self.right.insertNode(float_value)
            else:
                self.right = Node(float_value)

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


    def visualize(self):
        dot = Digraph()

        def addEdges(node):
            if node is None or node.value is None:
                return
            dot.node(str(id(node)), str(node.value))
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)), label="L")
                addEdges(node.left)
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)), label="R")
                addEdges(node.right)

        addEdges(self)
        dot.render('bst_output', view=True, format='png')

def filter(numbers):
    finalArray = []
    temp = ""
    for char in numbers:
        if char != " " and char != ",":
            temp += char
        else:
            if temp:
                finalArray.append(temp)
                temp = ""
            continue
    if temp:
        finalArray.append(temp)
    return finalArray



node = Node(None)
while True:
    print("\n-- MENU --")
    print("1. Insert Node")
    print("2. Insert Node Array")
    print("3. Find Node")
    print("4. Delete Node")
    print("5. Traverse Tree")
    print("6. Visualize Tree")
    print("0. Exit")

    try:
        int_choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input.")
        continue

    match int_choice:
        case 1:
            float_value = float(input("Enter integer to insert: "))
            node.insertNode(float_value)
            print(f"{float_value} has been inserted.")
            
        case 2:
            float_value = filter(input("Enter integers to insert: "))
            for number in float_value:
                node.insertNode(float(number))
                print(f"{float(number)} has been inserted.")

        case 3:
            if node:
                float_value = float(input("Enter integer to find: "))
                node.findNode(float_value)
            else:
                print("Tree is empty.")

        case 4:
            if node:
                float_value = float(input("Enter integer to delete: "))
                node = node.deleteNode(float_value)
            else:
                print("Tree is empty.")

        case 5:
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

        case 6:
            node.visualize()

        case 0:
            print("Goodbye!")
            break

        case _:
            print("Invalid choice.")

# Program Menambahkan, menghapus, mencari data dalam Linkedlist


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        currentNode = self.head
        while currentNode:
            if currentNode.next == None:
                print(f"{currentNode.value}-->None", end="")
            else:
                print(f"{currentNode.value}-->", end="")
            currentNode = currentNode.next

    def searchList(self,target):
        currentNode = self.head
        if currentNode == None:
            print("You must have existing node.")
            return
        
        while currentNode and currentNode.value != target:
            currentNode = currentNode.next
        
        if currentNode == None:
            print(f"Node {target} not found")
        else:
            print(f"There is a node {target}")


    def insertFront(self, data):
        node = Node(data, self.head)
        self.head = node
        self.tail = node if self.tail is None else self.tail
        # print(
        #     f"Current Head: {self.head.value}, Head Next: {"None" if self.head.next == None else self.head.next.value}, Current Tail: {"None" if self.tail == None else self.tail.value}"
        # )

    def insertAfter(self, position, data):
        currentNode = self.head
        if currentNode == None:
            print("You must have an existing node.")
            return
        while currentNode and currentNode.value != position:
            currentNode = currentNode.next
        if currentNode == None:
            print(f"Node {position} not found.")
            return
        newNode = Node(data, currentNode.next)
        currentNode.next = newNode
        if newNode.next == None:
            self.tail = newNode

    def insertBefore(self, position, data):
        currentNode = self.head
        if currentNode == None:
            print("You must have existing node.")
            return
        if currentNode.value == position:
            newNode = Node(data, self.head)
            self.head = newNode
        else:
            while currentNode.next and currentNode.next.value != position:
                currentNode = currentNode.next
            if currentNode.next == None:
                print(f"Node {position} not found.")
                return
            newNode = Node(data, currentNode.next)
            currentNode.next = newNode

    def insertBack(self, data):
        node = Node(data, next=None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        #     f"Current Head: {self.head.value}, Head Next: {"None" if self.head.next == None else self.head.next.value}, Current Tail: {"None" if self.tail == None else self.tail.value}"
        # )

    def deleteNode(self, position):
        currentNode = self.head

        if currentNode is None:
            print("Cannot delete from an empty list")
            return

        if self.head.value == position:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return

        while currentNode.next and currentNode.next.value != position:
            currentNode = currentNode.next

        if currentNode.next is None:
            print(f"Node {position} not found.")
            return

        if currentNode.next == self.tail:
            self.tail = currentNode
            self.tail.next = None
        else:
            currentNode.next = currentNode.next.next


linkedList1 = linkedList()

linkedList1.insertFront(5)
linkedList1.insertFront(8)
linkedList1.insertBack(3)
linkedList1.insertBack(4)

linkedList1.searchList(7)
# linkedList1.deleteNode(4)
# linkedList1.deleteNode(5)
# linkedList1.deleteNode(3)
# linkedList1.insertAfter(5,6)
# linkedList1.insertAfter(4,7)
# linkedList1.insertBefore(8,9)
linkedList1.printList()
print(
    f"\nHead: {linkedList1.head.value if linkedList1.head else "None"}\nTail: {linkedList1.tail.value if linkedList1.tail else "None"}"
)
# 8-->5-->3-->4-->None

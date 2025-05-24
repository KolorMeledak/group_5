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

    def insertFront(self, data):
        node = Node(data, self.head)
        self.head = node
        self.tail = node if self.tail is None else self.tail
        # print(
        #     f"Current Head: {self.head.value}, Head Next: {"None" if self.head.next == None else self.head.next.value}, Current Tail: {"None" if self.tail == None else self.tail.value}"
        # )

    def insertAfter(self, position, data):
        currentNode = self.head
        if currentNode != None:
            while currentNode.value != position:
                currentNode = currentNode.next
            # print(currentNode.value, currentNode.next.value) 
            newNode = Node(data, currentNode.next)
            currentNode.next = newNode
        else:
            print("You must have an existing node!")
        if newNode.next == None:
            self.tail = newNode

    def insertBefore(self, position, data):
        currentNode = self.head
        if currentNode != None:
            if currentNode.value == position:
                newNode = Node(data, self.head)
                self.head = newNode
            else:
                while currentNode.next.value != position:
                    currentNode = currentNode.next
                # print(currentNode.value, currentNode.next.value) 
                newNode = Node(data, currentNode.next)
                currentNode.next = newNode
        else:
            print("You must have an existing node!")


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
    
    def deleteNode(self,position):
        currentNode = self.head
        selectedNode = None
        if currentNode != None:
            if self.head.value == position:
                selectedNode = self.head
                self.head = self.head.next
                selectedNode = None
            else:
                while currentNode.next.value != position:
                    currentNode = currentNode.next
                if currentNode.next == self.tail:
                    selectedNode = self.tail
                    self.tail = currentNode
                    self.tail.next = None
                    selectedNode=None
                else:
                    selectedNode = currentNode.next
                    currentNode.next = currentNode.next.next
                    selectedNode = None
        else:
            print("Cannot delete from an empty list")    

linkedList1 = linkedList()

linkedList1.insertFront(5)
linkedList1.insertFront(8)
linkedList1.insertBack(3)
linkedList1.insertBack(4)

linkedList1.deleteNode(8)
linkedList1.deleteNode(4)
linkedList1.deleteNode(5)
linkedList1.deleteNode(3)
# linkedList1.insertAfter(5,6)
# linkedList1.insertAfter(4,7)
# linkedList1.insertBefore(8,9)
linkedList1.printList()
print(f"\nHead: {linkedList1.head.value}\nTail: {linkedList1.tail.value}")
# 8-->5-->3-->4-->None
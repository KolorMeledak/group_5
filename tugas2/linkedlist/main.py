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
        print(
            f"Current Head: {self.head.value}, Head Next: {"None" if self.head.next == None else self.head.next.value}, Current Tail: {"None" if self.tail == None else self.tail.value}"
        )

    def insertBack(self, data):
        node = Node(data, next=None)
        self.head = node if self.head is None else self.head
        self.tail.next = node
        self.tail = node
        print(
            f"Current Head: {self.head.value}, Head Next: {"None" if self.head.next == None else self.head.next.value}, Current Tail: {"None" if self.tail == None else self.tail.value}"
        )


linkedList1 = linkedList()

linkedList1.insertFront(5)
linkedList1.insertFront(8)
linkedList1.insertBack(3)
linkedList1.insertBack(4)

linkedList1.printList()

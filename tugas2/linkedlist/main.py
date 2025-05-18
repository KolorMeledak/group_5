# Program Menambahkan, menghapus, mencari data dalam Linkedlist

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertFront(self, data):
        node = Node(data, self.head)
        self.head = node
        print(self.head.value, "None" if self.head.next == None else self.head.next.value )

linkedList1=linkedList()

linkedList1.insertFront(5)
linkedList1.insertFront(8)

print(linkedList1.head.value)    
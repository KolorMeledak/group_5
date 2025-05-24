# Program Menambahkan, menghapus, mencari data dalam Linkedlist (dengan kode dan nama)

class Node:
    def __init__(self, kode=None, nama=None, next=None):
        self.kode = kode
        self.nama = nama
        self.next = next

    def display(self):
        print(f"{self.kode} : {self.nama}")

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        print("Isi senarai berantai:")
        currentNode = self.head
        while currentNode:
            currentNode.display()
            currentNode = currentNode.next

    def searchList(self, targetKode):
        currentNode = self.head
        while currentNode and currentNode.kode != targetKode:
            currentNode = currentNode.next
        if currentNode is None:
            print(f"{targetKode} tidak ditemukan.")
        else:
            print("Hasil pencarian:")
            currentNode.display()

    def insertFront(self, kode, nama):
        node = Node(kode, nama, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node

    def insertBack(self, kode, nama):
        node = Node(kode, nama, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insertAfter(self, targetKode, kode, nama):
        currentNode = self.head
        while currentNode and currentNode.kode != targetKode:
            currentNode = currentNode.next
        if currentNode is None:
            print(f"Node dengan kode {targetKode} tidak ditemukan.")
            return
        newNode = Node(kode, nama, currentNode.next)
        currentNode.next = newNode
        if newNode.next is None:
            self.tail = newNode

    def insertBefore(self, targetKode, kode, nama):
        currentNode = self.head
        if currentNode is None:
            print("Senarai kosong.")
            return
        if currentNode.kode == targetKode:
            self.insertFront(kode, nama)
            return
        while currentNode.next and currentNode.next.kode != targetKode:
            currentNode = currentNode.next
        if currentNode.next is None:
            print(f"Node dengan kode {targetKode} tidak ditemukan.")
            return
        newNode = Node(kode, nama, currentNode.next)
        currentNode.next = newNode

    def deleteNode(self, targetKode):
        currentNode = self.head
        if currentNode is None:
            print("Senarai kosong. Tidak dapat menghapus.")
            return
        if self.head.kode == targetKode:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        while currentNode.next and currentNode.next.kode != targetKode:
            currentNode = currentNode.next
        if currentNode.next is None:
            print(f"Node dengan kode {targetKode} tidak ditemukan.")
            return
        if currentNode.next == self.tail:
            self.tail = currentNode
        currentNode.next = currentNode.next.next


# Pemakaian
linkedList1 = LinkedList()

linkedList1.insertFront("AGN", "Agnes Monica")
linkedList1.insertFront("FAR", "Farhan")
linkedList1.insertFront("RIN", "Rina Melati")
linkedList1.insertFront("ZAS", "Zaskia")
linkedList1.insertFront("AMN", "Aminudin")

print("Keadaan awal:")
linkedList1.printList()

# linkedList1.deleteNode("RIN")
# print("\nSetelah RIN dihapus:")
# linkedList1.printList()

# print("\nPencarian RIN:")
# linkedList1.searchList("RIN")

# print("\nPencarian FAR:")
# linkedList1.searchList("FAR")

print(f"\nHead: {linkedList1.head.nama if linkedList1.head != None else "None"}\nTail: {linkedList1.tail.nama if linkedList1.tail != None else "None"}")

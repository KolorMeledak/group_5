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
        print("Isi linked list:")
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






linkedList1 = LinkedList()
    # linkedList1.insertFront("AGN", "Agnes Monica")
    # linkedList1.insertFront("FAR", "Farhan")
    # linkedList1.insertFront("RIN", "Rina Melati")
    # linkedList1.insertFront("ZAS", "Zaskia")
    # linkedList1.insertFront("AMN", "Aminudin")
while True:
    if linkedList1.head:
        linkedList1.printList()
    else: 
        print("List is empty.")
    pilihan = input("Menu:\n1. Insert Front\n2. Insert Back\n3. Insert After\n4. Insert Before\n5. Delete\n6. Search\n7. Check Head and Tail\n0. Exit")
    match pilihan:
        case "1":
            kode = input("Masukkan kode: ")
            nama = input("Masukkan nama: ")
            linkedList1.insertFront(kode, nama)
        case "2":
            kode = input("Masukkan kode: ")
            nama = input("Masukkan nama: ")
            linkedList1.insertBack(kode, nama)
        case "3":
            posisi = input("Masukkan kode node sebelum posisi baru: ")
            kode = input("Masukkan kode baru: ")
            nama = input("Masukkan nama baru: ")
            linkedList1.insertAfter(posisi, kode, nama)
        case "4":
            posisi = input("Masukkan kode node setelah posisi baru: ")
            kode = input("Masukkan kode baru: ")
            nama = input("Masukkan nama baru: ")
            linkedList1.insertBefore(posisi, kode, nama)
        case "5":
            kode = input("Masukkan kode yang ingin dihapus: ")
            linkedList1.deleteNode(kode)
        case "6":
            kode = input("Masukkan kode yang ingin dicari: ")
            linkedList1.searchList(kode)
        case "7":
            print(f"\nHead: {linkedList1.head.nama if linkedList1.head != None else "None"}\nTail: {linkedList1.tail.nama if linkedList1.tail != None else "None"}")
        case "0":
            print("Tenks ges")
            break
        case _:
            print("Pilihan invalid.")

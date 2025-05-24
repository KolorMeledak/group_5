# Program Menambahkan, menghapus, mencari data dalam Linkedlist

class Node:
    def __init__(self, kode=None, nama=None, next=None):
        self.kode = kode
        self.nama = nama
        self.next = next

    def display(self):
        print(f"|{self.kode} : {self.nama}|{self.next.kode + "|" if self.next else ""}", end=f"{"-->" if self.next else ""}")

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def kodeExists(self, kode):
        current = self.head
        while current:
            if current.kode == kode:
                return True
            current = current.next
        return False

    def printList(self):
        print("\nIsi linked list:")
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
        if self.kodeExists(kode):
            print(f"Kode {kode} sudah ada. Gunakan kode unik.")
            return
        node = Node(kode, nama, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node

    def insertBack(self, kode, nama):
        if self.kodeExists(kode):
            print(f"Kode {kode} sudah ada. Gunakan kode unik.")
            return
        node = Node(kode, nama, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insertAfter(self, targetKode, kode, nama):
        if self.kodeExists(kode):
            print(f"Kode {kode} sudah ada. Gunakan kode unik.")
            return
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
        if self.kodeExists(kode):
            print(f"Kode {kode} sudah ada. Gunakan kode unik.")
            return
        currentNode = self.head
        if currentNode is None:
            print("List kosong.")
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
            print("List kosong. Tidak dapat menghapus.")
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
    print("\nMenu:\n1. Insert Front\n2. Insert Back\n3. Insert After\n4. Insert Before\n5. Delete\n6. Search\n7. Check Head and Tail\n0. Exit")
    pilihan = input("\nInput kamu: ")
    match pilihan:
        case "1":
            kode = input("Masukkan kode: ").strip().upper()
            raw_nama = input("Masukkan nama: ").strip().split()
            nama = ' '.join(raw_nama)
            if not nama:
                print("Nama jangan kosong.")
                break
            linkedList1.insertFront(kode, nama)

        case "2":
            kode = input("Masukkan kode: ").strip().upper()
            raw_nama = input("Masukkan nama: ").strip().split()
            nama = ' '.join(raw_nama)
            if not nama:
                print("Nama jangan kosong.")
                break
            linkedList1.insertBack(kode, nama)

        case "3":
            posisi = input("Masukkan kode node sebelum posisi baru: ").strip().upper()
            kode = input("Masukkan kode baru: ").strip().upper()
            raw_nama = input("Masukkan nama baru: ").strip().split()
            nama = ' '.join(raw_nama)
            if not nama:
                print("Nama jangan kosong.")
                break
            linkedList1.insertAfter(posisi, kode, nama)

        case "4":
            posisi = input("Masukkan kode node setelah posisi baru: ").strip().upper()
            kode = input("Masukkan kode baru: ").strip().upper()
            raw_nama = input("Masukkan nama baru: ").strip().split()
            nama = ' '.join(raw_nama)
            if not nama:
                print("Nama jangan kosong.")
                break
            linkedList1.insertBefore(posisi, kode, nama)

        case "5":
            kode = input("Masukkan kode yang ingin dihapus: ").strip().upper()
            linkedList1.deleteNode(kode)

        case "6":
            kode = input("Masukkan kode yang ingin dicari: ").strip().upper()
            linkedList1.searchList(kode)

        case "7":
            print(f"Head: {linkedList1.head.nama if linkedList1.head else 'None'}")
            print(f"Tail: {linkedList1.tail.nama if linkedList1.tail else 'None'}")

        case "0":
            print("Final List: ")
            if linkedList1.head:
                linkedList1.printList()
            else: 
                print("List is empty.")
            print("Tenks ges")
            break

        case _:
            print("Pilihan invalid.")

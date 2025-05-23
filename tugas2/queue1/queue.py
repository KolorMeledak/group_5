def penuh(queue, max_size):
    return len(queue) == max_size

def kosong(queue):
    return len(queue) == 0

def enqueue(queue, item, max_size):
    if penuh(queue, max_size):
        print("Antrian penuh! Tidak bisa menambahkan data.")
    else:
        queue.append(item)
        print(f"'{item}' ditambahkan ke antrian.")

def dequeue(queue):
    if kosong(queue):
        print("Antrian kosong! Tidak ada data untuk dihapus.")
    else:
        removed_item = queue.pop(0)
        print(f"'{removed_item}' dihapus dari antrian.")

def tampilkan_antrian(queue):
    if kosong(queue):
        print("Antrian kosong!")
    else: 
        print("Isi antrian:", queue)

def main():
    queue = []
    ukuran = int(input("Masukkan ukuran antrian: "))

    while True:
        print("\nMenu:")
        print("1. Tambah data ke antrian")
        print("2. Hapus data dari antrian")
        print("3. Tampilkan isi antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            item = input("Masukkan data yang ingin ditambahkan: ")
            enqueue(queue, item, ukuran)
        elif pilihan == '2':
            dequeue(queue)
        elif pilihan == '3':
            tampilkan_antrian(queue)
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()
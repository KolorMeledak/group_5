arr = ["Medan", "Pontianak", "Surabaya"]
arr.sort()


def add_item(list, item):
    if item in list:
        print("Item sudah ada")
        return
    for i in range(len(list)):
        if item < list[i]:
            list.insert(i, item)
            return
    list.append(item)


def remove_item(list, item):
    for i in range(len(list)):
        if list[i] == item:
            list.pop(i)
            return
    print("Item tidak ditemukan")


while True:
    print("1. Tambah data")
    print("2. Hapus data")
    print("3. Tampilkan data")
    print("0. Keluar")
    choice = input("Pilih menu: ")

    if choice == "1":
        new_item = input("Isi data: ")
        add_item(arr, new_item)

    elif choice == "2":
        del_item = input("Data yang ingin dihapus: ")
        remove_item(arr, del_item)

    elif choice == "3":
        print(f"Data saat ini: {' - '.join(arr)}")

    elif choice == "0":
        break

    else:
        print("Pilihan tidak valid")

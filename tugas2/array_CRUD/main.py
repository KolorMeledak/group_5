array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


def display(arr):
    if not arr:
        print("Array kosong.")
        return
    for i in range(len(arr)):
        print(f"Data ke-{i+1}: {arr[i]}")


def add(arr, data, location):
    index = location - 1
    new_arr = []
    for i in range(index):
        new_arr.append(arr[i])
    new_arr.append(data)
    for i in range(len(arr) - index):
        new_arr.append(arr[index + i])
    print(f"Data {data} telah ditambahkan di lokasi {location}")
    return new_arr


def delete(arr, location):
    index = location - 1
    new_arr = []
    for i in range(index):
        new_arr.append(arr[i])
    for i in range(len(arr) - index - 1):
        new_arr.append(arr[index + i + 1])
    print(f"Data di lokasi {location} telah dihapus")
    return new_arr


print("Operasi array")
while True:
    print("\n1. Tampilkan array")
    print("2. Tambah data")
    print("3. Hapus data")
    print("4. Keluar")

    choice = input("\nPilih operasi (1-4): ")

    if choice == "1":
        display(array)

    elif choice == "2":
        data = input("Masukkan data yang akan ditambahkan: ")
        data = " ".join(data.split())
        if not data:
            print("Input tidak boleh kosong")
            continue

        if len(array) == 0:
            location_input = "1"
        else:
            location_input = input(f"Masukkan lokasi penambahan (1-{len(array)+1}): ")
        if (
            not location_input.isdigit()
            or int(location_input) < 1
            or int(location_input) > len(array) + 1
        ):
            print("Lokasi invalid")
            continue
        array = add(array, data, int(location_input))

    elif choice == "3":
        if len(array) == 0:
            print("Array kosong, tidak ada data yang bisa dihapus.")
            continue
        elif len(array) == 1:
            print("Hanya ada satu data, data tersebut akan dihapus.")
            array = []
            continue
        location_input = input(
            f"Masukkan lokasi data yang akan dihapus (1-{len(array)}): "
        )
        if (
            not location_input.isdigit()
            or int(location_input) < 1
            or int(location_input) > len(array)
        ):
            print("Lokasi invalid")
            continue
        array = delete(array, int(location_input))

    elif choice == "4":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")

stack = []
MAX_DATA = 8

while True:
    print("\nPilihan:")
    print("1. Tambah item\n2. Hapus item terakhir\n0. Selesai")

    print("\nIsi Stack:\n"+ '\n'.join(stack[::-1]) if stack else "\nIsi Stack:\n(stack kosong)")

    pilihan = input("Masukkan pilihan (1/2/0): ")

    match pilihan:
        case '1': 
            user_input = input("Nama: ")
            item = " ".join(user_input.split())

            if not item:
                print("Input kosong, silahkan masukkan nama.")
                continue

            if len(stack) < MAX_DATA:
                stack.append(item)
                print(f"'{item}' ditambahkan. (Total item: {len(stack)}/{MAX_DATA})")
            else:
                print(f"Stack penuh! '{item}' tidak bisa ditambahkan.")
        
        case "2":
            if stack:
                removed = stack.pop()
                print(f"nama '{removed}' dihapus dari stack, (Sisa item: {len(stack)}/{MAX_DATA})")
            else:
                print("Stack kosong, tidak ada data yang dapat dihapus.")
        case "0" :
            break
        case _:
            print("Input tidak valid")
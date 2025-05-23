stack = []
while True:
    try:
        max_data = int(input("Masukkan limit datanya (angka > 0): "))
        if max_data <= 0:
            print("Limit harus lebih besar dari 0.")
            continue
        break                               
    except ValueError:
        print("Input tidak valid, masukkan angka bulat positif.")

while True:
    print("\nPilihan:")
    print("1. Tambah item\n2. Hapus item terakhir\n0. Selesai")

    print("\nIsi Stack:\n"+ '\n'.join(stack[::-1]) if stack else "\nIsi Stack:\n(stack kosong)")
    print("===========================================\n")

    pilihan = input("Masukkan pilihan (1/2/0): ")

    match pilihan:
        case '1': 
            user_input = input("Nama: ")
            item = " ".join(user_input.split()) #rafly rabbany

            if not item:
                print("Input kosong, silahkan masukkan nama.")
                continue

            if len(stack) < max_data:
                stack.append(item)
                print(f"'{item}' ditambahkan. (Total item: {len(stack)}/{max_data})")
            else:
                print(f"Stack penuh! '{item}' tidak bisa ditambahkan.")
        
        case "2":
            if stack:
                removed = stack.pop()
                print(f"nama '{removed}' dihapus dari stack, (Sisa item: {len(stack)}/{max_data})")
            else:
                print("Stack kosong, tidak ada data yang dapat dihapus.")

        case "0" :
            break
        
        case _:
            print("Input tidak valid, masukkan angka 1/2/0.")

print("Thanks!, Adios👋")
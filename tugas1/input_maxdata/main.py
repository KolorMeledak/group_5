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
    print("1. Tambah item\n2. Hapus item\n0. Selesai")

    print("\nIsi Stack:")
    if stack:
        for i, item in enumerate(stack[::-1], 1):
            print(f"{len(stack) - i + 1}. {item}")
    else:
        print("(stack kosong)")
    print("===========================================\n")

    pilihan = input("Masukkan pilihan (1/2/0): ")

    match pilihan:
        case '1': 
            user_input = input("Nama: ")
            item = " ".join(user_input.split())

            if not item:
                print("Input kosong, silahkan masukkan nama.")
                continue

            if len(stack) < max_data:
                stack.append(item)
                print(f"'{item}' ditambahkan. (Total item: {len(stack)}/{max_data})")
            else:
                print(f"Stack penuh! '{item}' tidak bisa ditambahkan.")
        
        case "2":
            if not stack:
                print("Stack kosong, tidak ada data yang dapat dihapus.")
                continue

            print("\nPilih nomor item yang ingin dihapus:")
            for i, val in enumerate(stack[::-1], 1):
                print(f"{len(stack) - i + 1}. {val}")
            pilihan_hapus = input("Nomor item (secara default akan menghapus item terakhir): ").strip()

            if not pilihan_hapus:
                removed = stack.pop()
                print(f"Nama '{removed}' dihapus dari stack. (Sisa item: {len(stack)}/{max_data})")
                continue

            try:
                pilihan_hapus = int(pilihan_hapus)
                if pilihan_hapus < 1 or pilihan_hapus > len(stack):
                    print("Nomor tidak valid.")
                    continue

                index_asli = pilihan_hapus - 1
                if index_asli == len(stack) - 1:
                    removed = stack.pop()
                    print(f"Nama '{removed}' dihapus dari stack. (Sisa item: {len(stack)}/{max_data})")
                else:
                    akan_terhapus = stack[index_asli:]
                    print(f"\nJika Anda menghapus '{stack[index_asli]}', maka Anda akan menghapus: {', '.join(akan_terhapus)}.")
                    konfirmasi = input("Apakah ingin melanjutkan penghapusan? (y/n): ").strip().lower()
                    if konfirmasi == 'y':
                        for _ in range(len(akan_terhapus)):
                            removed = stack.pop()
                        print(f"Item-item tersebut telah dihapus. (Sisa item: {len(stack)}/{max_data})")
                    else:
                        print("Penghapusan dibatalkan.")
            except ValueError:
                print("Input harus berupa angka atau tekan Enter untuk hapus item terakhir.")

        case "0":
            break
        
        case _:
            print("Input tidak valid, masukkan angka 1/2/0.")

print("Thanks!, Adios👋")

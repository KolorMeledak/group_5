queue = []
maxdata = 100

while True:
    print("\nPilihan:")
    print("1. Tambah kota")
    print("2. Hapus kota (paling depan)")
    print("3. Tampilkan daftar kota")
    print("4. Selesai")

    pilihan = input("Masukkan pilihan 1/2/3/4: ").strip()

    match pilihan:
        case '1':
            if len(queue) >= maxdata:
                print("Daftar kota penuh!")
            else:
                kota = input("  Nama kota: ").strip()
                queue.append(kota)
                print(f"  + '{kota}' (Total: {len(queue)})")

        case '2':
            if queue:
                removed = queue.pop(0)
                print(f"  – '{removed}' terhapus.")
            else:
                print("  (Antrian kosong)")

        case '3':
            if queue:
                print("\n-- Daftar Kota (urutan input) --")
                for i, kota in enumerate(queue, 1):
                    print(f"   {i}. {kota}")
                print("-- Selesai --")
            else:
                print("  (Antrian kosong)")

        case '4':
            print("Terima kasih, Adios.")
            break

        case _:
            print("Pilihan tidak valid. Ketik 1-4.")

queue = []

while True:
    try:
        maxdata = int(input("Masukkan limit jumlah kota (angka > 0): "))
        if maxdata <= 0:
            print("Limit harus lebih besar dari 0.")
            continue
        break                               
    except ValueError:
        print("Input tidak valid, masukkan angka bulat positif.")

while True:
    print("\n===========================================")
    print("Pilihan:")
    print("1. Tambah kota\n2. Hapus kota\n3. Tampilkan daftar kota\n4. Selesai")
    print("===========================================")

    pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()

    match pilihan:
        case '1':
            if len(queue) >= maxdata:
                print(f"Antrian kota penuh! Maksimal {maxdata} kota.")
            else:
                kota = input("  Nama kota: ").strip()
                kota = " ".join(kota.split())

                if not kota:
                    print("  Input kosong. Masukkan nama kota yang valid.")
                    continue

                queue.append(kota)
                print(f"  + Kota '{kota}' ditambahkan. (Total: {len(queue)}/{maxdata})")

        case '2':
            if not queue:
                print("  (Antrian kosong, tidak ada kota yang bisa dihapus.)")
                continue

            data = input("Masukkan nomor urutan atau nama kota yang ingin dihapus (Secara default akan menghapus kota pada urutan pertama): ").strip()

            if not data:
                removed = queue.pop(0)
                print(f"  - Kota '{removed}' dihapus dari antrian.")
                print(f"    (Sisa kota: {len(queue)}/{maxdata})")
                continue

            if data.isdigit():
                nomor = int(data)
                if nomor < 1 or nomor > len(queue):
                    print(f"  Nomor tidak valid. Pilih antara 1 hingga {len(queue)}.")
                    continue
                index_kota = nomor - 1
            else:
                index_kota = next((i for i, kota in enumerate(queue) if kota.lower() == data.lower()), -1)

                if index_kota == -1:
                    print(f"  Kota '{data}' tidak ditemukan dalam antrian.")
                    continue

            if index_kota == 0:
                removed = queue.pop(0)
                print(f"  - Kota '{removed}' dihapus dari antrian.")
                print(f"    (Sisa kota: {len(queue)}/{maxdata})")
            else:
                target_kota = queue[index_kota]
                kota_sebelumnya = queue[:index_kota]
                teks_kota_sebelumnya = ', '.join(kota_sebelumnya)
                konfirmasi = input(
                    f"  Menghapus kota {target_kota} akan menghapus juga: {teks_kota_sebelumnya}\n"
                    f"  Lanjutkan penghapusan? (y/n): "
                ).strip().lower()

                if konfirmasi == 'y':
                    removed = queue[:index_kota + 1]
                    del queue[:index_kota + 1]
                    print(f"  - Kota-kota '{', '.join(removed)}' telah dihapus.")
                    print(f"    (Sisa kota: {len(queue)}/{maxdata})")
                else:
                    print("  Penghapusan dibatalkan.")
        case '3':
            if queue:
                print("\n-- Daftar Kota (Sesuai Urutan Input) --")
                for i, kota in enumerate(queue, 1):
                    print(f"  {i}. {kota}")
                print("----------------------------------------")

                print("\n-- Daftar Kota (Urut Abjad) --")
                for i, kota in enumerate(sorted(queue, key=lambda x: x.lower()), 1):
                    print(f"  {i}. {kota}")
                print("--------------------------------")
            else:
                print("  (Antrian kosong)")

        case '4':
            print("Terima kasih! Adios 👋")
            break

        case _:
            print("Pilihan tidak valid. Masukkan angka 1/2/3/4.")

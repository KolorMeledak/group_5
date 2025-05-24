def input_limit():
    while True:
        try:
            maxdata = int(input("Masukkan limit jumlah kota (angka > 0): "))
            if maxdata <= 0:
                print("Limit harus lebih besar dari 0.")
                continue
            return maxdata
        except ValueError:
            print("Input tidak valid, masukkan angka bulat positif.")

def tambah_kota(queue, maxdata):
    if len(queue) >= maxdata:
        print(f"Antrian kota penuh! Maksimal {maxdata} kota.")
        return
    kota = input("  Nama kota: ").strip()
    kota = " ".join(kota.split())
    if not kota:
        print("  Input kosong. Masukkan nama kota yang valid.")
        return
    queue.append(kota)
    print(f"  + Kota '{kota}' ditambahkan. (Total: {len(queue)}/{maxdata})")

def hapus_kota(queue, maxdata):
    if not queue:
        print("  (Antrian kosong, tidak ada kota yang bisa dihapus.)")
        return

    print("\n-- Daftar Kota --")
    for i, kota in enumerate(queue, 1):
        print(f"  {i}. {kota}")
    print("------------------")

    data = input("Masukkan nomor urutan kota yang ingin dihapus (kosongkan untuk hapus kota pertama): ").strip()

    if not data:
        removed = queue.pop(0)
        print(f"  - Kota '{removed}' dihapus dari antrian.")
        print(f"    (Sisa kota: {len(queue)}/{maxdata})")
        return

    if not data.isdigit():
        print("  Input tidak valid. Masukkan nomor urutan kota.")
        return

    nomor = int(data)
    if nomor < 1 or nomor > len(queue):
        print(f"  Nomor tidak valid. Pilih antara 1 hingga {len(queue)}.")
        return

    index_kota = nomor - 1

    if index_kota == 0:
        removed = queue.pop(0)
        print(f"  - Kota '{removed}' dihapus dari antrian.")
        print(f"    (Sisa kota: {len(queue)}/{maxdata})")
        return

    target_kota = queue[index_kota]
    kota_sebelumnya = queue[:index_kota]
    teks_kota_sebelumnya = ', '.join(kota_sebelumnya)
    konfirmasi = input(
        f"  Menghapus kota '{target_kota}' akan menghapus juga: {teks_kota_sebelumnya}\n"
        f"  Lanjutkan penghapusan? (y/n): "
    ).strip().lower()

    if konfirmasi == 'y':
        removed = queue[:index_kota + 1]
        del queue[:index_kota + 1]
        print(f"  - Kota-kota '{', '.join(removed)}' telah dihapus.")
        print(f"    (Sisa kota: {len(queue)}/{maxdata})")
    else:
        print("  Penghapusan dibatalkan.")

def bubble_sort_kota(kota_list):
    daftar_urut = kota_list[:]
    n = len(daftar_urut)
    for i in range(n):
        for j in range(0, n - i - 1):
            if daftar_urut[j].lower() > daftar_urut[j + 1].lower():
                daftar_urut[j], daftar_urut[j + 1] = daftar_urut[j + 1], daftar_urut[j]
    return daftar_urut

def tampilkan_kota(queue):
    if not queue:
        print("  (Antrian kosong)")
        return
    print("\n-- Daftar Kota (Sesuai Urutan Input) --")
    for i, kota in enumerate(queue, 1):
        print(f"  {i}. {kota}")
    print("----------------------------------------")

    print("\n-- Daftar Kota (Sesuai Abjad) --")
    daftar_urut = bubble_sort_kota(queue)
    for i, kota in enumerate(daftar_urut, 1):
        print(f"  {i}. {kota}")
    print("--------------------------------")

def main():
    queue = []
    maxdata = input_limit()

    while True:
        print("\n===========================================")
        print("Pilihan:")
        print("1. Tambah kota\n2. Hapus kota\n3. Tampilkan daftar kota\n4. Selesai")
        print("===========================================")

        pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()

        match pilihan:
            case '1':
                tambah_kota(queue, maxdata)
            case '2':
                hapus_kota(queue, maxdata)
            case '3':
                tampilkan_kota(queue)
            case '4':
                print("Terima kasih! Adios 👋")
                break
            case _:
                print("Pilihan tidak valid. Masukkan angka 1/2/3/4.")

if __name__ == "__main__":
    main()

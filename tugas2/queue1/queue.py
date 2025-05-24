def kosong(queue):
    return len(queue) == 0

def tampilkan_antrian(queue):
    if kosong(queue):
        print("Antrian kosong!")
    else:
        print("\nPilih jenis tampilan:")
        print("1. Tampilkan sebagian data (dibatasi)")
        print("2. Tampilkan semua data")

        opsi = input("Masukkan pilihan (1/2): ")
        if opsi == '1':
            try:
                batas = int(input("Masukkan jumlah data yang ingin ditampilkan: "))
                print("Isi antrian terbatas:", queue[:batas])
                if batas < len(queue):
                    sisa = queue[batas:]
                    print("Data berikut tidak masuk ke antrian karena penuh:", ", ".join(sisa))
                elif batas > len(queue):
                    kurang = batas - len(queue)
                    print(f"Jumlah data yang diminta ({batas}) masih ada {kurang} antrian yang kosong.")
            except ValueError:
                print("Input tidak valid.")
        elif opsi == '2':
            print("Isi antrian lengkap:", queue)
        else:
            print("Pilihan tidak valid.")

def main():
    queue = []
    data_input = input("Masukkan semua data antrian (pisahkan dengan koma): ")
    queue = [i.strip() for i in data_input.split(",")]
    print("Data antrian berhasil dimasukkan.")
    print("Isi antrian:", queue)

    while True:
        print("\nMenu:")
        print("1. Tampilkan isi antrian")
        print("2. Keluar")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == '1':
            tampilkan_antrian(queue)
        elif pilihan == '2':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()
def bubble_sort(data, ascending=True):
    n = len(data)
    urutan = "ASCENDING" if ascending else "DESCENDING"
    print(f"\n===== PROSES BUBBLE SORT ({urutan}) =====")
    print("\nSebelum diurutkan:", data_angka)
    for i in range(n):
        print(f"\nIterasi ke-{i + 1}:")
        for j in range(0, n - i - 1):
            print(f"Bandingkan {data[j]} dan {data[j + 1]}", end="")
            if (ascending and data[j] > data[j + 1]) or (not ascending and data[j] < data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
                print(f" → Tukar {data[j]} dan {data[j + 1]} → {data}")
            else:
                print(" → Tidak perlu ditukar")
        print(f"Data setelah iterasi ke-{i + 1}: {data}")
    return data


data_terakhir = []

while True:
    # Tanya apakah ingin input data baru
    if not data_terakhir:
        pakai_data_lama = 'n'
    else:
        pakai_data_lama = input("Apakah ingin menggunakan data sebelumnya? (y/n): ")

    if pakai_data_lama.lower() != 'y':
        input_data = input("Masukkan data yang ingin diurutkan (pisahkan dengan koma): ")
        input_list = input_data.split(",")

        data_angka = []
        for angka in input_list:
            angka_koma = float(angka)
            if angka_koma.is_integer():
                data_angka.append(int(angka_koma))
            else:
                data_angka.append(angka_koma)
        data_terakhir = data_angka.copy()  # Simpan sebagai data terakhir
    else:
        data_angka = data_terakhir.copy()

    # Menu pilihan
    print("\nPilihan urutan pengurutan data:")
    print("1. Urutkan dari kecil ke besar (ascending)")
    print("2. Urutkan dari besar ke kecil (descending)")
    print("3. Tampilkan keduanya (ascending dan descending)")

    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        print("\nMengurutkan data dari kecil ke besar...")
        hasil = bubble_sort(data_angka.copy(), ascending=True)
        print("\nSetelah diurutkan (ascending):", hasil)

    elif pilihan == "2":
        print("\nMengurutkan data dari besar ke kecil...")
        hasil = bubble_sort(data_angka.copy(), ascending=False)
        print("\nSetelah diurutkan (descending):", hasil)

    elif pilihan == "3":
        hasil_asc = bubble_sort(data_angka.copy(), ascending=True)
        print("\nSetelah diurutkan (ascending):", hasil_asc)

        hasil_desc = bubble_sort(data_angka.copy(), ascending=False)
        print("\nSetelah diurutkan (descending):", hasil_desc)

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
        continue

    while True:
        ulang = input("\nApakah Anda ingin mengulangi program? (y/n): ")
        if ulang.lower() == 'y':
            print("\nMengulang program...\n")
            break
        elif ulang.lower() == 'n':
            print("Program dihentikan.")
            exit()
        else:
            print("Pilihan tidak valid. Harap pilih 'y' atau 'n'.")

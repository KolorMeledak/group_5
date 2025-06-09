def bubble_sort(data, ascending=True):
    n = len(data)
    for i in range(n):
        print(f"iterasi ke-{i + 1}:")
        for j in range(0, n - i - 1):
            print(f" Bandingkan {data[j]} dan {data[j + 1]}", end="")
            if (ascending and data[j] > data[j + 1]) or (not ascending and data[j] < data[j + 1]):
                data [j], data[j + 1] = data[j + 1], data[j]
                print(f" Tukar {data[j]} dan {data[j + 1]}")
            else:
                print(" Tidak perlu ditukar")
        print(f"Data setelah iterasi ke-{i + 1}: {data}")
    return data

while True:
    #Input datanya
    input_data = input("Masukkan data yang ingin diurutkan (pisahkan dengan koma): ")
    input_list = input_data.split(",")

    data_angka = []
    for angka in input_list:
        angka_koma = float(angka)
        if angka_koma.is_integer():
            data_angka.append(int(angka_koma))
        else:
            data_angka.append(angka_koma)

    #Pilihan mau diurut dari mana ke mana
    print("\nPilihan urutan pengurutan data:")
    print("1. Urutkan dari kecil ke besar (ascending)")
    print("2. Urutkan dari besar ke kecil (descending)")
    pilihan = input("Masukkan pilihan (1/2): ")
    
    if pilihan == "2":
        ancending = False
        print("\nMengurutkan data dari besar ke kecil...")
    else:
        ancending = True
        print("\nMengurutkan data dari kecil ke besar...")

    #Display
    print("\nSebelum diurutkan:", data_angka)
    hasil = bubble_sort(data_angka, ancending)
    print("\nSetelah diurutkan:", hasil)
    
    while True:
        ulang = input("\nApakah Anda ingin mengulangi program? (y/n): ")
        if ulang.lower() == 'y':
            print("Program dilanjutkan.")
            break
        elif ulang.lower() == 'n':
            print("Program dihentikan.")
            exit()
        else:
            print("Pilihan tidak valid. Pilih (y/n).")
            
            
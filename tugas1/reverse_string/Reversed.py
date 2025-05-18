while True:
    isi = input("Masukkan sebuah data atau kalimat:")
    print(f"\nisi yang dimasukkan: {isi}")

    stack = []
    print("\n[1] menyimpan karakter ke dalam stack")

    for char in isi:
        stack.append(char)
        print(f" Push: {char} -> Stack sekarang: {stack}")

    reversed_string = ""
    print ("\n[2] mengeluarkan karakter dari stack (pop): ")
    while stack:
        popped_char = stack.pop()
        reversed_string += popped_char
        print(f" Pop: {popped_char} -> Hasil sementara: {reversed_string}")

    print(f"\n[3] isi stack setelah dibalik: {reversed_string}")

    #Untuk membalik string paragraf
    # print("\n[4] isi stack setelah dibalik (paragraf)")
    # try:
    #     with open("paragraf.txt", "r", encoding="utf-8") as file:
    #         isi_paragraf = file.read()
    #         daftar_paragraf = isi_paragraf.split("\n\n")

    #         for paragraf in daftar_paragraf:
    #             # print(f"\nIsi paragraf: {paragraf}")

    #             stack_paragraf = []
    #             for char in paragraf:
    #                 stack_paragraf.append(char)
    #                 # print(f" Push: {char} -> Stack sekarang: {stack_paragraf}")

    #             reversed_paragraf = ""
    #             while stack_paragraf:
    #                 popped_char = stack_paragraf.pop()
    #                 reversed_paragraf += popped_char
    #                 # print(f" Pop: {popped_char} -> Hasil sementara: {reversed_paragraf}")

    #             print(f"\n{reversed_paragraf}")
    
    # except FileNotFoundError:
    #     print("File 'paragraf.txt' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama dengan skrip ini.")


    while True:
        pilihan_lanjut = input("\nApakah Anda ingin melakukan pembalikan lagi? (y/n): ")
        if pilihan_lanjut.lower() == 'y':
            print("Program dilanjutkan.")
            break
        elif pilihan_lanjut.lower() == 'n':
            print("Program dihentikan.")
            exit()
        else:
            print("Pilihan tidak valid. Pilih (y/n).")
            
        
        
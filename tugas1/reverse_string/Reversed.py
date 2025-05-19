while True:
        print("\nMasukkan beberapa paragraf (ketik enter 2x untuk menyelesaikan):")
        
        daftar_paragraf = []
        paragraf_list = []
        while True:
            baris = input()
            if baris.strip() == "":
                if paragraf_list:
                 paragraf = "\n".join(paragraf_list)
                 daftar_paragraf.append(paragraf)
                 paragraf_list = []   
                else:
                   break
            else:
             paragraf_list.append(baris)
       
        for paragraf in daftar_paragraf:
            # print (f"\nIsi paragraf: {paragraf}")
            stack = []
            # print("\n[1] menyimpan karakter ke dalam stack")

            for char in paragraf:
                stack.append(char)
                # print(f" Push: {char} -> Stack sekarang: {stack}")

            reversed_string = ""
            # print ("\n[2] mengeluarkan karakter dari stack (pop): ")
            while stack:
                popped_char = stack.pop()
                reversed_string += popped_char
                # print(f" Pop: {popped_char} -> Hasil sementara: {reversed_string}")
            print(f"\n{reversed_string}")

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
                
            
        
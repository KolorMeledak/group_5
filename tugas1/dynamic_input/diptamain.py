import numremover as nr
tumpukan = ["Pras","Rafly","Dipta","Yoga"]

while True:
    print(f"\nCurrent Stack: \n{"\n".join(reversed(tumpukan))}\n")
    selection = input("MENU\n1. Tambah Stack\n2. Kurangi Stack\n0. Exit\n")

    match selection:
        case "1":
            raw_nama= nr.removeNum(str(input("Masukkan nama yang ingin ditambah:\n"))).split() 
            nama = ' '.join(raw_nama)
            if nama == ('' and ' ' and '\n'):
                print("Jangan input selain nama.\n")
            else:
                print(f"Added {nama}\n")
                tumpukan.append(nama)
        case "2":
            if tumpukan:
                print(f"Removed {tumpukan[-1]}")
                tumpukan.pop()
            else:
                 print("Gabisa mengurangi stack kosong.\n")
        case"0": 
            break
        case _: 
            print("Jangan input selain yang disediakan.\n")

print(f"Final Stack: \n{"\n".join(reversed(tumpukan))}")

    # selection = input("1. Tambah Stack\n2. Kurangi Stack\n3. Lihat Paling Atas Stack\n4. Cek Stack\n5. Ukuran Stack\n0. Exit\n")

        # case "3":
        #     print(f"Top of Stack is {tumpukan[-1]}")
        # case "4":
        #     if not tumpukan:
        #         print("The stack is empty")
        #     else:
        #         print("Stack is not empty")
        # case "5":
        #         print(f"Stack is {len(tumpukan)} item(s) long.")
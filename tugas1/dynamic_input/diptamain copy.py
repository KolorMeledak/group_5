tumpukan = ["Pras","Rafly","Dipta","Yoga"]

while True:
    print(f"\nCurrent Stack: \n{"\n".join(reversed(tumpukan))}\n")
    selection = input("MENU\n1. Tambah Stack\n2. Kurangi Stack\n0. Exit\n")

    match selection:
        case "1":
            raw_nama= str(input("Masukkan nama yang ingin ditambah:\n")).split() 
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
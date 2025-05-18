# - Dynamic input program with static array with stack structure, input in the form of name

repeater = True
tumpukan = ["agus","beni","budy","ianto"]

while repeater:
    print(*tumpukan, sep=', ')
    selection = input("1. Tambah Stek\n2. Kurangi Stek\n3. Lihat Paling Atas Stek\n4. Cek Stek\n5. Ukuran Stek\n0. Exit")

    match selection:
        case "1":
            nama = input("Masukkan nama yang ingin ditambah:\n")
            print(f"Added {nama}\n")
            tumpukan.append(nama)
        case "2":
            if tumpukan:
                print(f"Removed {tumpukan[-1]}")
                tumpukan.pop(-1)
            else:
                 print("Can't remove from an empty stack")
        case "3":
            print(f"Top of Stack is {tumpukan[-1]}")
        case "4":
            if not tumpukan:
                print("The stack is empty")
            else:
                print("Stack is not empty")
        case "5":
                print(f"Stack is {len(tumpukan)} item(s) long.")
        case"0": 
              repeater = False
print("Thanks")
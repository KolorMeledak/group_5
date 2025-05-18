stack = []
maxdata = 8

print("Masukkan nama item untuk ditambahkan ke stack.")
print(f"Maksimal item: {maxdata}.")
print("Ketik 'q' untuk keluar dan menampilkan isi stack.\n")

while True:
    user_input = input("Tambah item (atau 'q' untuk keluar): ").strip()
    if user_input.lower() == 'q':
        break

    if len(stack) < maxdata:
        stack.append(user_input)
        print(f"'{user_input}' ditambahkan. (Total item: {len(stack)}/{maxdata})")
    else:
        print(f"Stack penuh! '{user_input}' tidak bisa ditambahkan.")

print("\nIsi Stack")
while stack:
    print(stack.pop())

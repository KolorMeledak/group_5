stack = []
maxdata = 8
items_to_add = ['Amira', 'Baidah', 'Citra', 'Dody', 'Edy', 'Falino', 'Gading', 'Imelda', 'Harahap', 'Jonathan', 'Karina']

for item in items_to_add:
    if len(stack) < maxdata:
        stack.append(item)
    else:
        print("Tumpukan penuh! Elemen yang tidak dimasukkan:", ", ".join(items_to_add[maxdata:]))
        break

print("\nIsi Tumpukan:")
while stack:
    print(stack.pop())

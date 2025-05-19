stack = []
limit = int(input("masukkan limit datanya: "))

while True:
    user_input = input("masukkan nama (atau '0' jika sudah selesai): ").strip()
    if user_input == "0":
        break
    stack.append(user_input)

    item = " ".join(user_input.split())

    if not item:
        print("Input kosong, silahkan masukkan nama.")
        continue

removed = []
while len(stack) > limit:
    removed.append(stack.pop())

print("\nisi stack:")
for item in (stack[::-1]):
    print(item)

if removed:
    removed = removed[::-1]

    if len(removed) == 1:
        msg = removed[0]
    elif len(removed) == 2:
        msg = f"{removed[0]} dan {removed[1]}"
    else:
        msg = ", ".join(removed[:-1]) + f", dan {removed[-1]}"

    print(f"\nstack penuh! {msg} tidak dapat dimasukkan")
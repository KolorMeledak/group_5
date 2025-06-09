def show(obj):
    if isinstance(obj, list):
        return ', '.join([str(int(n)) if n % 1 == 0 else str(n) for n in obj])
    else:
        return str(int(obj)) if obj % 1 == 0 else str(obj)

def selection_sort(nums, ascending):
    print("Data awal:", show(nums))
    for i in range(len(nums)):
        min_idx = i
        arah = "terkecil" if ascending else "terbesar"
        print(f"\nIterasi ke-{i+1}: Cari elemen {arah} dari {show(nums[i:])}")
        for j in range(i + 1, len(nums)):
            compare = nums[j] < nums[min_idx] if ascending else nums[j] > nums[min_idx]
            if compare:
                min_idx = j
        print(f"{arah.capitalize()} adalah {show(nums[min_idx])} di indeks {min_idx}")
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            print(f"Tukar {show(nums[min_idx])} dengan {show(nums[i])} => {show(nums)}")
        else:
            print("Tidak perlu tukar")
    print("\nData terurut:", show(nums))

data_input = input('Tulis angka yang akan diurutkan(pisahkan dengan spasi): ').split()
data_input = [float(i) for i in data_input]

while True:
    arah = input('Urutkan dari yang terkecil ke terbesar? (y/n): ').strip().lower()
    if arah in ('y', 'n'):
        selection_sort(data_input, True if arah == 'y' else False)
        break
    else:
        print("Input harus 'y' atau 'n'")
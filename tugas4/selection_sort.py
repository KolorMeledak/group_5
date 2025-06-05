def show(arr):
    return ', '.join(map(str, [int(n) if n % 1 == 0 else n for n in arr]))

def selection_sort(nums, ascending):
    print("Data awal:", show(nums))
    n = len(nums)
    for i in range(n):
        min_idx = i
        arah = "terkecil" if ascending else "terbesar"
        print(f"\nIterasi ke-{i+1}: Cari elemen {arah} dari {nums[i:]}")
        for j in range(i + 1, n):
            if ascending:
                if nums[j] < nums[min_idx]:
                    min_idx = j
            else:
                if nums[j] > nums[min_idx]:
                    min_idx = j
        print(f"{arah.capitalize()} adalah {nums[min_idx]} di indeks {min_idx}")
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            print(f"Tukar {nums[min_idx]} dengan {nums[i]} => {show(nums)}")
        else:
            print("Tidak perlu tukar")
    print("\nData terurut:", show(nums))

data_input = input('Tulis angka yang akan diurutkan(pisahkan dengan spasi): ').split()
data_input = [float(i) for i in data_input]

arah = input('Urutkan dari yang terkecil ke terbesar? (y/n): ').strip().lower()
try:
    if arah not in ('y', 'n'):
        raise ValueError("Input harus 'y' atau 'n'")
    selection_sort(data_input, True if arah == 'y' else False)
except ValueError as e:
    print(e)
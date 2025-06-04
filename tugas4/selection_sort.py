def selection_sort(nums, ascending=True):
    print("Data awal:", nums)
    n = len(nums)
    for i in range(n):
        min_idx = i
        print(f"\nIterasi ke-{i+1}: Cari elemen terkecil dari {nums[i:]}")
        for j in range(i + 1, n):
            if ascending:
                if nums[j] < nums[min_idx]:
                    min_idx = j
            else:
                if nums[j] > nums[min_idx]:
                    min_idx = j
        print(f"  Terkecil adalah {nums[min_idx]} di indeks {min_idx}")
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            print(f"  Tukar {nums[min_idx]} dengan {nums[i]} => {nums}")
        else:
            print("  Tidak perlu tukar")
    print("\nData terurut:", nums)

data_input = input('Tulis angka yang akan diurutkan(pisahkan dengan spasi): ').split()
data_input = [int(i) for i in data_input if i.isdigit()]

arah = input('Urutkan dari yang terkecil ke terbesar? (y/n): ').strip().lower()
if arah == 'y':
    selection_sort(data_input, True)
else:
    selection_sort(data_input, False)

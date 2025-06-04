def insertion_sort(nums, ascending=True):
    print("Data awal:", nums)
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        print(f"\nIterasi ke-{i}: Masukkan {key} ke bagian yang sudah terurut {nums[:i]}")
        while j >= 0 and ((ascending and nums[j] > key) or (not ascending and nums[j] < key)):
            nums[j + 1] = nums[j]
            print(f"  Geser {nums[j]} ke kanan => {nums}")
            j -= 1
        nums[j + 1] = key
        print(f"  Tempatkan {key} di posisi {j+1} => {nums}")
    print("\nData terurut:", nums)

data_input = input('Tulis angka yang akan diurutkan(pisahkan dengan spasi): ').split()
data_input = [int(i) for i in data_input if i.isdigit()]

arah = input('Urutkan dari yang terkecil ke terbesar? (y/n): ').strip().lower()
if arah == 'y':
    insertion_sort(data_input, True)
else:
    insertion_sort(data_input, False)
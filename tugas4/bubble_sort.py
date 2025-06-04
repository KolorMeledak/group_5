def bubble_sort(nums, ascending=True):
    n = len(nums)
    print("Data awal:", nums)
    for i in range(n):
        print(f"\nIterasi ke-{i+1}:")
        swapped = False
        for j in range(0, n - i - 1):
            print(f"  Bandingkan {nums[j]} dan {nums[j+1]}", end="")
            if ascending:
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
                    print(f" => Tukar => {nums}")
                else:
                    print(" => Tidak ditukar")
            else:
                if nums[j] < nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
                    print(f" => Tukar => {nums}")
                else:
                    print(" => Tidak ditukar")
        if not swapped:
            print("  Tidak ada pertukaran, data sudah terurut.")
            break
    print("\nData terurut:", nums)

data_input = input('Tulis angka yang akan diurutkan(pisahkan dengan spasi): ').split()
data_input = [int(i) for i in data_input if i.isdigit()]

arah = input ('Urutkan dari yang terkecil ke terbesar? (y/n): ').strip().lower()
if arah == 'y':
    bubble_sort(data_input, True)
else:
    bubble_sort(data_input, False)
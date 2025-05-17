def insertion_sort(nums):
    print("Data awal:", nums)
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        print(f"\nIterasi ke-{i}: Masukkan {key} ke bagian yang sudah terurut {nums[:i]}")
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            print(f"  Geser {nums[j]} ke kanan => {nums}")
            j -= 1
        nums[j + 1] = key
        print(f"  Tempatkan {key} di posisi {j+1} => {nums}")
    print("\nData terurut:", nums)

data = [5, 1, 4, 2, 8]
insertion_sort(data)

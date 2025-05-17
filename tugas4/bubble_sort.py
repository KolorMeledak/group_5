def bubble_sort(nums):
    n = len(nums)
    print("Data awal:", nums)
    for i in range(n):
        print(f"\nIterasi ke-{i+1}:")
        swapped = False
        for j in range(0, n - i - 1):
            print(f"  Bandingkan {nums[j]} dan {nums[j+1]}", end="")
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
                print(f" => Tukar => {nums}")
            else:
                print(" => Tidak ditukar")
        if not swapped:
            print("  Tidak ada pertukaran, data sudah terurut.")
            break
    print("\nData terurut:", nums)

data = [5, 1, 4, 2, 8]
bubble_sort(data)

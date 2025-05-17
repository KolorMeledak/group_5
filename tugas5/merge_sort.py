def merge_sort(nums, depth=0):
    indent = "  " * depth 
    if len(nums) > 1:
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        print(f"{indent}Bagi: {nums} -> {left_half} dan {right_half}")

        merge_sort(left_half, depth + 1)
        merge_sort(right_half, depth + 1)

        i = j = k = 0
        print(f"{indent}Gabungkan: {left_half} dan {right_half}")
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                print(f"{indent}  Ambil {left_half[i]} dari kiri")
                i += 1
            else:
                nums[k] = right_half[j]
                print(f"{indent}  Ambil {right_half[j]} dari kanan")
                j += 1
            k += 1

        while i < len(left_half):
            nums[k] = left_half[i]
            print(f"{indent}  Sisa kiri: ambil {left_half[i]}")
            i += 1
            k += 1

        while j < len(right_half):
            nums[k] = right_half[j]
            print(f"{indent}  Sisa kanan: ambil {right_half[j]}")
            j += 1
            k += 1

        print(f"{indent}Setelah merge: {nums}")

data = [38, 27, 43, 3, 9, 82, 10]
print("=== Merge Sort Proses ===")
merge_sort(data)
print("\nHasil akhir:", data)

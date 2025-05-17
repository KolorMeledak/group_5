def shell_sort(nums):
    data = nums.copy()
    n = len(data)
    gap = n // 2
    print("=== Shell Sort (non-in-place) ===")

    while gap > 0:
        print(f"\nGap = {gap}")
        for i in range(gap, n):
            temp = data[i]
            j = i
            print(f"  Ambil {temp}, bandingkan dengan elemen tiap gap ke belakang")
            while j >= gap and data[j - gap] > temp:
                print(f"    {data[j - gap]} > {temp} → geser ke kanan")
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        print(f"Hasil sementara: {data}")
        gap //= 2

    print("\nHasil akhir:", data)
    return data

data = [34, 7, 23, 32, 5, 62]
sorted_shell = shell_sort(data)
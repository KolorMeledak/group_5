def show(obj):
    if isinstance(obj, list):
        return ', '.join([str(int(n)) if n % 1 == 0 else str(n) for n in obj])
    return str(int(obj)) if obj % 1 == 0 else str(obj)

def selection_sort(nums, ascending):
    print(f'Data awal: {show(nums)}')
    for i in range(0, len(nums)):
        i_min = i
        arah = "terkecil" if ascending else "terbesar"
        print(f'\nIterasi ke-{i + 1}: Cari elemen {arah} dari {show(nums[i:])}')
        for j in range (i + 1, len(nums)):
            compare = nums[j] < nums[i_min] if ascending else nums[j] > nums[i_min]
            if compare:
                i_min = j
        print(f'{arah.capitalize()} adalah {show(nums[i_min])} di indeks {i_min}')
        if i_min != i:
            min = nums.pop(i_min)
            print(f'Geser {show(min)} ke indeks {i}')
            nums.insert(i, min)
        else:
            print(f'Index ke {i} ({show(nums[i])}) sudah benar')
        print(f'Hasil iterasi ke-{i + 1}: {show(nums)}')
    print(f'\nData terurut: {show(nums)}')

data_input = input('Tulis angka yang akan diurutkan(pisahkan dengan spasi): ').split()
data_input = [float(i) for i in data_input]

while True:
    arah = input('Urutkan dari yang terkecil ke terbesar? (yna): ').strip().lower()
    if arah in ['y', 'n']:
        selection_sort(data_input, True if arah == 'y' else False)
        break
    elif arah == 'a':
        print("-------------------------\nTerkecil ke terbesar:")
        selection_sort(data_input, True)
        print("-------------------------\nTerbesar ke terkecil:")
        selection_sort(data_input, False)
        break
    else:
        print("Input harus 'y' atau 'n'")
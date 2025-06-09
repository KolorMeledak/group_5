def insertion_sort(nums, ascending=True):
    print("Data Awal:", nums)
    for i in range(1, len(nums)):
        elemen_saat_ini = nums[i]
        j = i - 1
        print(f"\nIterasi ke-{i}: Masukkan {elemen_saat_ini} ke bagian yang sudah terurut {nums[:i]}")
        
        while j >= 0 and ((ascending and nums[j] > elemen_saat_ini) or (not ascending and nums[j] < elemen_saat_ini)):
            nilai_digeser = nums[j]
            nums[j + 1] = nums[j]
            
            list_tampilan = nums[:] 
            list_tampilan[j] = '...'
            # list_tampilan.append(elemen_saat_ini)
            
            print(f"   Geser {nilai_digeser} ke kanan => {list_tampilan}")
            j -= 1

        nums[j + 1] = elemen_saat_ini
        print(f"   Tempatkan {elemen_saat_ini} di posisi ke-{j + 2} => {nums}")
    print("\nData Terurut:", nums)

while True:
    input_pengguna_str = input('\nMasukkan angka yang akan diurutkan (pisahkan dengan spasi): ').split()

    nums = []
    for item in input_pengguna_str:
        try:
            if '.' in item:
                nums.append(float(item))
            else:
                nums.append(int(item)) 
        except ValueError:
            print(f"Peringatan: '{item}' bukan angka yang valid dan akan diabaikan.")
            continue
            
    if not nums:
        print("Tidak ada angka valid yang dimasukkan. Silakan coba lagi.")
        continue

    arah_urut = input('Urutkan dari yang terkecil ke terbesar? (y/n): ').strip().lower()
    if arah_urut == 'y':
        insertion_sort(nums, True)
    else:
        insertion_sort(nums, False)

    ulang_program = input('\nJalankan program kembali? (y/n): ').strip().lower()
    if ulang_program != 'y':
        print("Thanks! Adios👋")
        break
def insertion_sort(nums, ascending=True):
    print("--- Insertion Sort Dimulai ---")
    print(f"Awal: {nums}\n")

    n = len(nums)

    sort_order_text = "Naik (Kecil ke Besar)" if ascending else "Turun (Besar ke Kecil)"
    print(f"Urutan: {sort_order_text}\n")

    if n > 0:
        print(f"Pass 0 (Base): [{nums[0]}] | Sisa: {nums[1:]}")
    else:
        print("\n--- Insertion Sort Selesai ---")
        print(f"Hasil Akhir: {nums}")
        return

    for i in range(1, n):
        elemen_saat_ini = nums[i]
        j = i - 1

        print(f"\n--- Pass {i}: Sisipkan {elemen_saat_ini} ---")
        print(f"  Ambil: {elemen_saat_ini}")
        print(f"  Bandingkan dengan: {nums[:i]}")

        geser = False
        while j >= 0:
            should_shift = False
            if ascending:
                should_shift = nums[j] > elemen_saat_ini
            else:
                should_shift = nums[j] < elemen_saat_ini

            if should_shift:
                geser = True
                nilai_digeser = nums[j]
                nums[j + 1] = nums[j]
                
                temp_list = nums[:]
                temp_list[j] = '...'
                comparison_symbol = ">" if ascending else "<"
                print(f"    {nilai_digeser} {comparison_symbol} {elemen_saat_ini} => {nilai_digeser} geser ke kanan. State: {temp_list}")
                j -= 1
            else:
                break

        if not geser:
            print(f"    {elemen_saat_ini} sudah pada tempatnya, tidak perlu geser.")

        nums[j + 1] = elemen_saat_ini
        print(f"  Sisipkan {elemen_saat_ini} di posisi ke-{j + 2}. Data: {nums}")
        print(f"  Terurut: {nums[:i+1]} | Sisa: {nums[i+1:]}")

    print("\n--- Insertion Sort Selesai ---")
    print(f"Hasil Akhir: {nums}")

while True:
    input_user = input('\nMasukkan angka yang akan diurutkan (pisahkan dengan spasi): ').split()

    nums_original = []
    for item in input_user:
        try:
            if '.' in item:
                nums_original.append(float(item))
            else:
                nums_original.append(int(item)) 
        except ValueError:
            print(f"Peringatan: '{item}' bukan angka yang valid dan akan diabaikan.")
            continue
            
    if not nums_original:
        print("Tidak ada angka valid yang dimasukkan. Silakan coba lagi.")
        continue

    print("\nPilih opsi pengurutan:")
    print("1. Urutkan secara Ascending (Kecil ke Besar)")
    print("2. Urutkan secara Descending (Besar ke Kecil)")
    print("3. Urutkan Ascending dan Descending")

    choice = input("Masukkan pilihan Anda (1/2/3): ").strip()

    match choice:
        case '1':
            insertion_sort(list(nums_original), True)
        case '2':
            insertion_sort(list(nums_original), False)
        case '3':
            print("\n===== Urutan Ascending =====")
            insertion_sort(list(nums_original), True)
            print("\n===== Urutan Descending =====")
            insertion_sort(list(nums_original), False)
        case _:
            print("Pilihan tidak valid. Silakan coba lagi.")

    repeat = input('\nJalankan program kembali? (y/n): ').strip().lower()
    if repeat != 'y':
        print("Thanks! Adios👋")
        break
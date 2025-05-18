def conversion(target, number, precision = 5):
    dec_point = precision
    symbols = "0123456789ABCDEF"
    if number < 0:
        return "-" + conversion(target, -number)
        
    result = ""
    int_number = int(number)
    frac_number = number - int_number
    
    if number == 0:
        return "0"
    else:
        while int_number > 0:
            result = symbols[int_number % target] + result
            int_number //= target

        if frac_number > 0:
            if result == "":
                result = "0"
            result += "."
            while frac_number > 0 and precision > 0:
                precision -= 1
                frac_number *= target
                result += symbols[int(frac_number)]
                frac_number -= int(frac_number)
            if precision == 0 and frac_number > 0:
                result += f"... (dibulatkan ke {dec_point} angka di belakang koma)" 
        return result
    
while True:
    print("KONVERSI BILANGAN")    
    conversion_target = input("\nMasukkan basis bilangan tujuan diantara 2 dan 16 (jika ingin mengubah ke beberapa basis, pisahkan dengan spasi): ")
    
    conversion_target = conversion_target.split()
    if not all(i.isdigit() and 2 <= int(i) <= 16 for i in conversion_target):
        print("Semua basis harus berupa angka antara 2 dan 16!")
        continue
    
    conversion_number = input("\nMasukkan angka yang akan dikonversi: ")
    try:
        conversion_number = float(conversion_number)
    except ValueError:
        print("Input harus berupa bilangan!")
        continue

    precision = input('\nMasukan jumlah angka di belakang koma (default 5): ')
    if precision.isdigit():
        precision = int(precision)

    for i in conversion_target:
        print(f"Angka {conversion_number} dalam basis {i} adalah: {conversion(int(i), conversion_number, precision)}")

    print("Coba lagi? (y/n)")
    if input().lower() != 'y':
        break
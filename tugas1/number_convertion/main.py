def conversion(target, number):

    symbols = "0123456789ABCDEF"
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
            while frac_number > 0:
                frac_number *= target
                result += symbols[int(frac_number)]
                frac_number -= int(frac_number)

        return result
while True:
    print("KONVERSI BILANGAN")    
    conversion_target = int(input("Masukkan basis bilangan tujuan (2, 8, 16): "))
    conversion_number = float(input("Masukkan angka yang akan dikonversi: "))
    print(f"Angka {conversion_number} dalam basis {conversion_target} adalah: {conversion(conversion_target, conversion_number)}")
    print("Coba lagi? (y/n)")
    if input().lower() != 'y':
        break
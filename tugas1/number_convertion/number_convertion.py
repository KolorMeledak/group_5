def convert_to_biner(decimal):
    int_res = ""
    frac_res = ""

    int_part = int(decimal)
    frac_part = decimal - int_part

    if int_part == 0:
        int_res = "0"
    else:
        while int_part > 0 :
            int_res = str(int_part % 2) + int_res
            int_part //= 2
    
    while frac_part > 0:
        frac_part *= 2
        x = int(frac_part)
        frac_res += str(x)
        frac_part -= x

    res = int_res + ("." + frac_res if frac_res else "")
    print(res)

convert_to_biner(13.5)
def number_convertion(num):
    if num == 0:
        return {"binary": "0", "octal": "0", "hexadecimal": "0"}
    
    bases = {2: "binary", 8: "octal", 16: "hexadecimal"}
    results = {}

    for base, name in bases.items():
        steps = []
        result = ""
        original = num
        temp_n = num

        while temp_n > 0:
            quotient = temp_n // base
            remainder = temp_n % base
            symbols = "0123456789ABCDEF"
            steps.append(f"{temp_n} : {base} = {quotient}, remainder {symbols[remainder]}")
            result = symbols[remainder] + result
            temp_n = quotient

        print(f"Converting {original} to {name}:")
        print("\n".join(steps))
        print(f"Final result: {result}\n")

        results[name] = result
    
    return results

while True:
    user_input = input("Enter a decimal number (or 'q' to quit): ")
    if user_input.lower() == "q":
        break
    
    num = int(user_input)
    number_convertion(num)

print("Thanks!")

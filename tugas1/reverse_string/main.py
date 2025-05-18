def reverse_string(text):
    chars = []

    for char in text:
        chars.append(char)

    res = ''
    while chars:
        res += chars.pop()

    return res

while True:
    input_string = input('input text (or "q" to quit): ')
    if input_string.lower() == "q" or input_string.lower() == "quit":
        break
    print(reverse_string(input_string))
print("Thanks!")
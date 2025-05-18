import os

array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def display(arr):
    for i in range(len(arr)):
        print(f'Data ke-{i+1}: {arr[i]}')
        
def add(arr, data, location):
    index = location - 1
    if index < 0 or index > len(arr):
        print("Lokasi invalid")
        return arr
    new_arr = []
    for i in range(index):
        new_arr.append(arr[i])
    new_arr.append(data)
    for i in range(len(arr) - index):
        new_arr.append(arr[index + i])
    print(f'Data {data} telah ditambahkan di lokasi {location}')
    return new_arr

def delete(arr, location):
    index = location - 1
    if index < 0 or index >= len(arr):
        print("Lokasi invalid")
        return arr
    new_arr = []
    for i in range(index):
        new_arr.append(arr[i])
    for i in range(len(arr) - index - 1):
        new_arr.append(arr[index + i + 1])
    print(f'Data di lokasi {location} telah dihapus')
    return new_arr

os.system('cls')
print('Operasi array')
while True:
    print("1. Tampilkan array")
    print("2. Tambah data")
    print("3. Hapus data")
    print("4. Keluar")
    
    choice = input("Pilih operasi (1-4): ")
     
    if choice == '1':
        print('\n')
        display(array)
    elif choice == '2':
        print('\n')
        data = input("Masukkan data yang akan ditambahkan: ")
        location_input = input("Masukkan lokasi penambahan (1-{}): ".format(len(array)))
        if not location_input.isdigit():
            print("Lokasi invalid")
            continue
        array = add(array, data, int(location_input))
    elif choice == '3':
        print('\n')
        location_input = input("Masukkan lokasi data yang akan dihapus (1-{}): ".format(len(array)))
        if not location_input.isdigit():
            print("Lokasi invalid")
            continue
        array = delete(array, int(location_input))
    elif choice == '4':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
    
    print('\n')


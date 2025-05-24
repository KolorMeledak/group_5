array = ['aa', 'ab', 'bb']
array.sort()

def add(list, item):
    if item in list:
        print("Item sudah ada")
        return
    for i in range(len(list)):
        if item < list[i]:
            list.insert(i, item)
            return
        
def remove(list, item):
    for i in range(len(list)):
        if list[i] == item:
            list.pop(i)
            return
    print("Item tidak ditemukan")
        
while True:
    print('1. Tambah data')
    print('2. Hapus data')
    print('3. Tampilkan data')
    print('0. Keluar')
    choice = input("Pilih menu: ")
    
    match choice:
        case '1':
            new_item = input("Isi data: ")
            try:
                if not new_item.strip():
                    raise ValueError("Input tidak boleh kosong")
                add(array, new_item)
            except ValueError as e:
                print(e)
        case '2':
            del_item = input("Data yang ingin dihapus: ")
            try:
                if not del_item.strip():
                    raise ValueError("Input tidak boleh kosong")
                remove(array, del_item)
            except ValueError as e:
                print(e)
        case '3':
            print(f"Data saat ini: {', '.join(array)}")
        case '0':
            break
        case _:
            print("Pilihan tidak valid")
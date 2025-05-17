from collections import deque

class AntrianArray:
    def __init__(self, ukuran):
        self.data = [None] * ukuran
        self.depan = 0
        self.belakang = 0
        self.maks_elemen = ukuran

    def insert(self, x):
        posisi_belakang = (self.belakang + 1) % self.maks_elemen

        if posisi_belakang == self.depan:
            print("Antrian Penuh")
            print(f"{x} tidak dimasukkan")
        else:
            self.belakang = posisi_belakang
            self.data[self.belakang] = x

    def remove(self):
        if self.empty():
            print("Antrian kosong")
            return ""
        self.depan = (self.depan + 1) % self.maks_elemen
        return self.data[self.depan]

    def empty(self):
        return self.depan == self.belakang

def antrian_deque():
    daftar = deque()
    daftar.extend([
        "Aminudin",
        "Bahtiar Rivai",
        "Cita Citata",
        "Dul Sumbang",
        "Engel Lelga",
        "Farah Nurlaela",
        "Galih",
        "Herwantyoko",
        "Indah Kusuma"
    ])

    print("\n[Deque] Isi Antrian:")
    while daftar:
        nama = daftar.popleft()
        print(nama)

def main():
    print("Isi Antrian:")
    ukuran = 8
    daftar_array = AntrianArray(ukuran)

    nama_nama = [
        "Aminudin",
        "Bahtiar Rivai",
        "Cita Citata",
        "Dul Sumbang",
        "Engel Lelga",
        "Farah Nurlaela",
        "Galih",
        "Herwantyoko",
        "Indah Kusuma"
    ]

    for nama in nama_nama:
        daftar_array.insert(nama)

    while not daftar_array.empty():
        print(daftar_array.remove())

    antrian_deque()


if __name__ == "__main__":
    main()

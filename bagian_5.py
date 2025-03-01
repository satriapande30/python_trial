# =========================================================================
# LATIHAN PYTHON DASAR - BAGIAN 4
# Struktur Data: List dan Tuple
# =========================================================================

# 4.1 Struktur Data: List
def struktur_data_list():
    """Mendemonstrasikan penggunaan list di Python"""
    print("=== Struktur Data: List ===")
    
    # Membuat list
    buah = ["apel", "pisang", "mangga", "jeruk"]
    angka = [1, 2, 3, 4, 5]
    campuran = [1, "dua", 3.0, True]
    
    print(f"List buah: {buah}")
    print(f"List angka: {angka}")
    print(f"List campuran: {campuran}")
    
    # Akses elemen list
    print("\n-- Akses elemen list --")
    print(f"Elemen pertama: {buah[0]}")
    print(f"Elemen terakhir: {buah[-1]}")
    
    # Slicing list
    print("\n-- Slicing list --")
    print(f"Dua elemen pertama: {buah[0:2]}")
    print(f"Dua elemen terakhir: {buah[-2:]}")
    print(f"Semua kecuali elemen pertama: {buah[1:]}")
    print(f"Semua kecuali elemen terakhir: {buah[:-1]}")
    
    # Menggabungkan list
    print("\n-- Menggabungkan list --")
    gabungan = buah + angka
    print(f"List gabungan: {gabungan}")
    
    # Mengubah elemen list
    print("\n-- Mengubah elemen list --")
    buah[1] = "anggur"
    print(f"List setelah perubahan: {buah}")
    
    # Menambah elemen ke list
    print("\n-- Menambah elemen ke list --")
    buah.append("durian")
    print(f"List setelah append: {buah}")
    
    buah.insert(1, "nanas")
    print(f"List setelah insert: {buah}")
    
    # Menghapus elemen dari list
    print("\n-- Menghapus elemen dari list --")
    buah.remove("mangga")
    print(f"List setelah remove: {buah}")
    
    elemen_terakhir = buah.pop()
    print(f"Elemen terakhir yang dihapus: {elemen_terakhir}")
    print(f"List setelah pop: {buah}")
    
    # Mengurutkan list
    print("\n-- Mengurutkan list --")
    buah.sort()
    print(f"List setelah sort: {buah}")
    
    buah.reverse()
    print(f"List setelah reverse: {buah}")
    
    # List comprehension
    print("\n-- List comprehension --")
    angka = [1, 2, 3, 4, 5]
    kuadrat = [x**2 for x in angka]
    print(f"List angka: {angka}")
    print(f"List kuadrat angka: {kuadrat}")
    
    # List comprehension dengan kondisi
    angka_genap = [x for x in range(10) if x % 2 == 0]
    print(f"Angka genap 0-9: {angka_genap}")
    
    # Fungsi built-in untuk list
    print("\n-- Fungsi built-in untuk list --")
    angka = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"List angka: {angka}")
    print(f"Jumlah elemen: {len(angka)}")
    print(f"Nilai minimum: {min(angka)}")
    print(f"Nilai maksimum: {max(angka)}")
    print(f"Jumlah nilai: {sum(angka)}")
    print(f"Jumlah kemunculan nilai 5: {angka.count(5)}")
    print(f"Indeks pertama nilai 5: {angka.index(5)}")

# 4.2 Struktur Data: Tuple
def struktur_data_tuple():
    """Mendemonstrasikan penggunaan tuple di Python"""
    print("\n=== Struktur Data: Tuple ===")
    
    # Membuat tuple
    koordinat = (3, 5)
    warna = ("merah", "hijau", "biru")
    campuran = (1, "dua", 3.0, True)
    tuple_tunggal = (5,)  # perhatikan koma
    
    print(f"Tuple koordinat: {koordinat}")
    print(f"Tuple warna: {warna}")
    print(f"Tuple campuran: {campuran}")
    print(f"Tuple tunggal: {tuple_tunggal}")
    
    # Akses elemen tuple
    print("\n-- Akses elemen tuple --")
    print(f"Elemen pertama: {warna[0]}")
    print(f"Elemen terakhir: {warna[-1]}")
    
    # Slicing tuple
    print("\n-- Slicing tuple --")
    print(f"Dua elemen pertama: {warna[0:2]}")
    
    # Tuple tidak bisa diubah (immutable)
    print("\n-- Tuple bersifat immutable --")
    print("warna[1] = 'kuning'  # Ini akan error: 'tuple' object does not support item assignment")
    
    # Unpacking tuple
    print("\n-- Unpacking tuple --")
    x, y = koordinat
    print(f"Koordinat x: {x}, y: {y}")
    
    # Fungsi tuple
    print("\n-- Fungsi dengan tuple --")
    warna_list = list(warna)  # Konversi tuple ke list
    print(f"Tuple sebagai list: {warna_list}")
    
    # Menggabungkan tuple
    print("\n-- Menggabungkan tuple --")
    warna_tambahan = ("kuning", "ungu")
    semua_warna = warna + warna_tambahan
    print(f"Tuple gabungan: {semua_warna}")
    
    # Mengulang tuple
    print("\n-- Mengulang tuple --")
    koordinat_ganda = koordinat * 3
    print(f"Tuple diulang 3x: {koordinat_ganda}")
    
    # Fungsi built-in untuk tuple
    print("\n-- Fungsi built-in untuk tuple --")
    angka = (3, 1, 4, 1, 5, 9, 2)
    print(f"Tuple angka: {angka}")
    print(f"Jumlah elemen: {len(angka)}")
    print(f"Nilai minimum: {min(angka)}")
    print(f"Nilai maksimum: {max(angka)}")
    print(f"Jumlah nilai: {sum(angka)}")
    print(f"Jumlah kemunculan nilai 1: {angka.count(1)}")
    print(f"Indeks pertama nilai 5: {angka.index(5)}")

# Menjalankan contoh
if __name__ == "__main__":
    struktur_data_list()
    struktur_data_tuple()

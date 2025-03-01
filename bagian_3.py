# =========================================================================
# LATIHAN PYTHON DASAR - BAGIAN 3
# Input, Output, dan Struktur Kendali
# =========================================================================

# 3.1 Input dan Output Dasar
def input_output_dasar():
    """Mendemonstrasikan input dan output dasar"""
    print("=== Input dan Output Dasar ===")
    
    # Input dasar
    nama = input("Masukkan nama Anda: ")
    umur = int(input("Masukkan umur Anda: "))
    
    # Output dengan format string
    print(f"Halo, {nama}! Tahun depan umur Anda akan menjadi {umur + 1} tahun.")
    
    # Berbagai cara formatting output
    print("Halo, %s! Umur Anda %d tahun." % (nama, umur))  # Format lama
    print("Halo, {}! Umur Anda {} tahun.".format(nama, umur))  # Format .format()
    print(f"Halo, {nama}! Umur Anda {umur} tahun.")  # f-string (Python 3.6+)

# 3.2 Struktur Kendali: Percabangan
def struktur_kendali_percabangan():
    """Mendemonstrasikan struktur kendali percabangan"""
    print("\n=== Struktur Kendali: Percabangan ===")
    
    # Input
    nilai = int(input("Masukkan nilai (0-100): "))
    
    # If-else sederhana
    print("\n-- If-else sederhana --")
    if nilai >= 60:
        print("Anda lulus!")
    else:
        print("Anda belum lulus.")
    
    # If-elif-else
    print("\n-- If-elif-else --")
    if nilai >= 90:
        grade = "A"
    elif nilai >= 80:
        grade = "B"
    elif nilai >= 70:
        grade = "C"
    elif nilai >= 60:
        grade = "D"
    else:
        grade = "E"
    
    print(f"Grade Anda: {grade}")
    
    # Operator ternary
    print("\n-- Operator ternary --")
    status = "Lulus" if nilai >= 60 else "Tidak Lulus"
    print(f"Status: {status}")

# 3.3 Struktur Kendali: Perulangan
def struktur_kendali_perulangan():
    """Mendemonstrasikan struktur kendali perulangan"""
    print("\n=== Struktur Kendali: Perulangan ===")
    
    # Perulangan for dengan range
    print("\n-- Perulangan for dengan range --")
    print("for i in range(5):")
    for i in range(5):
        print(i, end=" ")  # 0 1 2 3 4
    print()
    
    # Perulangan for dengan range (start, stop)
    print("\n-- Perulangan for dengan range (start, stop) --")
    print("for i in range(1, 6):")
    for i in range(1, 6):
        print(i, end=" ")  # 1 2 3 4 5
    print()
    
    # Perulangan for dengan range (start, stop, step)
    print("\n-- Perulangan for dengan range (start, stop, step) --")
    print("for i in range(0, 10, 2):")
    for i in range(0, 10, 2):
        print(i, end=" ")  # 0 2 4 6 8
    print()
    
    # Perulangan for dengan list
    print("\n-- Perulangan for dengan list --")
    buah = ["apel", "pisang", "mangga", "jeruk"]
    print("for item in buah:")
    for item in buah:
        print(item, end=" ")  # apel pisang mangga jeruk
    print()
    
    # Perulangan for dengan enumerate
    print("\n-- Perulangan for dengan enumerate --")
    print("for indeks, item in enumerate(buah):")
    for indeks, item in enumerate(buah):
        print(f"Indeks {indeks}: {item}")
    
    # Perulangan while
    print("\n-- Perulangan while --")
    print("while counter < 5:")
    counter = 0
    while counter < 5:
        print(counter, end=" ")
        counter += 1
    print()
    
    # Break dan continue
    print("\n-- Penggunaan break --")
    print("for i in range(10): if i == 5: break")
    for i in range(10):
        if i == 5:
            break
        print(i, end=" ")  # 0 1 2 3 4
    print()
    
    print("\n-- Penggunaan continue --")
    print("for i in range(10): if i % 2 == 0: continue")
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i, end=" ")  # 1 3 5 7 9
    print()

# Menjalankan contoh
if __name__ == "__main__":
    input_output_dasar()
    struktur_kendali_percabangan()
    struktur_kendali_perulangan()

# =========================================================================
# LATIHAN PYTHON DASAR - BAGIAN 1
# Hello World, Variabel, dan Tipe Data
# =========================================================================

# 1.1 Hello World - Program pertama
def hello_world():
    """Program Python pertama"""
    print("Hello, World!")

# 1.2 Variabel dan Tipe Data
def variabel_dan_tipe_data():
    """Mendemonstrasikan tipe data dasar di Python"""
    # Tipe data dasar
    angka_bulat = 10  # Integer
    angka_desimal = 3.14  # Float
    teks = "Belajar Python"  # String
    boolean = True  # Boolean
    
    # Menampilkan nilai dan tipe data
    print(f"Angka bulat: {angka_bulat}, tipe: {type(angka_bulat)}")
    print(f"Angka desimal: {angka_desimal}, tipe: {type(angka_desimal)}")
    print(f"Teks: {teks}, tipe: {type(teks)}")
    print(f"Boolean: {boolean}, tipe: {type(boolean)}")
    
    # Konversi tipe data
    print(f"Konversi float ke int: {int(angka_desimal)}")
    print(f"Konversi int ke float: {float(angka_bulat)}")
    print(f"Konversi int ke string: {str(angka_bulat)}")

# 1.3 Contoh Penggunaan Fungsi
def contoh_penggunaan():
    """Contoh cara menggunakan fungsi yang sudah dibuat"""
    # Menjalankan hello_world
    print("Menjalankan fungsi hello_world:")
    hello_world()
    
    # Menjalankan variabel_dan_tipe_data
    print("\nMenjalankan fungsi variabel_dan_tipe_data:")
    variabel_dan_tipe_data()

# Menjalankan contoh jika file ini dijalankan langsung
if __name__ == "__main__":
    contoh_penggunaan()

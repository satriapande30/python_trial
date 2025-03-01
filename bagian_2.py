# =========================================================================
# LATIHAN PYTHON DASAR - BAGIAN 2
# Operator dan Ekspresi
# =========================================================================

# 2.1 Operator dan Ekspresi
def operator_dan_ekspresi():
    """Mendemonstrasikan operator di Python"""
    # Operator aritmatika
    a, b = 10, 3
    print("=== Operator Aritmatika ===")
    print(f"Penjumlahan: {a} + {b} = {a + b}")
    print(f"Pengurangan: {a} - {b} = {a - b}")
    print(f"Perkalian: {a} * {b} = {a * b}")
    print(f"Pembagian: {a} / {b} = {a / b}")
    print(f"Pembagian bulat: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Perpangkatan: {a} ** {b} = {a ** b}")
    
    # Operator perbandingan
    print("\n=== Operator Perbandingan ===")
    print(f"Sama dengan: {a} == {b} adalah {a == b}")
    print(f"Tidak sama dengan: {a} != {b} adalah {a != b}")
    print(f"Lebih besar: {a} > {b} adalah {a > b}")
    print(f"Lebih kecil: {a} < {b} adalah {a < b}")
    print(f"Lebih besar sama dengan: {a} >= {b} adalah {a >= b}")
    print(f"Lebih kecil sama dengan: {a} <= {b} adalah {a <= b}")
    
    # Operator logika
    print("\n=== Operator Logika ===")
    x, y = True, False
    print(f"AND: {x} and {y} adalah {x and y}")
    print(f"OR: {x} or {y} adalah {x or y}")
    print(f"NOT: not {x} adalah {not x}")
    print(f"NOT: not {y} adalah {not y}")
    
    # Operator assignment
    print("\n=== Operator Assignment ===")
    c = 5
    print(f"Nilai awal c: {c}")
    
    c += 2  # c = c + 2
    print(f"Setelah c += 2: {c}")
    
    c -= 1  # c = c - 1
    print(f"Setelah c -= 1: {c}")
    
    c *= 3  # c = c * 3
    print(f"Setelah c *= 3: {c}")
    
    c /= 2  # c = c / 2
    print(f"Setelah c /= 2: {c}")
    
    # Operator identitas
    print("\n=== Operator Identitas ===")
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    
    print(f"list1 is list2: {list1 is list2}")
    print(f"list1 is list3: {list1 is list3}")
    print(f"list1 is not list2: {list1 is not list2}")
    
    # Operator keanggotaan
    print("\n=== Operator Keanggotaan ===")
    buah = ["apel", "pisang", "mangga"]
    print(f"'apel' in buah: {'apel' in buah}")
    print(f"'jeruk' in buah: {'jeruk' in buah}")
    print(f"'jeruk' not in buah: {'jeruk' not in buah}")

# Menjalankan contoh
if __name__ == "__main__":
    operator_dan_ekspresi()

def luas_persegi(sisi):
    return sisi * sisi

def hitung_kembalian(total_belanja, uang_dibayar):
    return uang_dibayar - total_belanja

def operasi_dua_angka(a, b):
    return {
        'Penjumlahan': a + b,
        'Pengurangan': a - b,
        'Perkalian': a * b,
        'Pembagian': a / b if b != 0 else 'Tidak bisa dibagi nol'
    }

def total_setelah_diskon(harga):
    return harga * 0.8

def hitung_keuntungan(jumlah_domba):
    harga_dasar = 2500000
    harga_jual = 3000000
    total_modal = harga_dasar * jumlah_domba
    total_penjualan = harga_jual * jumlah_domba
    keuntungan = total_penjualan - total_modal
    return total_modal, keuntungan

def tukar_nilai(x, y):
    x, y = y, x
    return x, y

def rata_rata_tiga_angka(a, b, c):
    return (a + b + c) / 3

def luas_keliling_segitiga_siku_siku(a, b):
    import math
    luas = (a * b) / 2
    c = math.sqrt(a**2 + b**2)
    keliling = a + b + c
    return luas, keliling


print("Luas Persegi:", luas_persegi(4))
print("Kembalian:", hitung_kembalian(45000, 50000))
print("Operasi Dua Angka:", operasi_dua_angka(10, 5))
print("Total Setelah Diskon:", total_setelah_diskon(100000))
modal, untung = hitung_keuntungan(3)
print(f"Total Modal: {modal}, Keuntungan: {untung}")
x, y = tukar_nilai(10, 20)
print(f"Nilai setelah ditukar: x={x}, y={y}")
print("Rata-rata Tiga Angka:", rata_rata_tiga_angka(10, 20, 30))
luas, keliling = luas_keliling_segitiga_siku_siku(3, 4)
print(f"Luas Segitiga: {luas}, Keliling Segitiga: {keliling}")

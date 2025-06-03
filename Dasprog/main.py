from ecommerce.pricing import hitung_diskon, hitung_pajak, hitung_total
from ecommerce.order import generate_order_id

def main():
    nama_pelangan = input("masukan nama pelangan: ")
    nama_produk = input("masukan nama produ: ")
    harga_asli = float(input("masukan harga asli: "))
    persentase_diskon = float(input("masukan persentase diskon: "))
    psersentase_pajak = float(input("masukan persentase pajak: "))

    diskon = harga_asli * (persentase_diskon / 100)
    total = hitung_total(harga_asli, persentase_diskon, psersentase_pajak)
    generate_order_id = generate_order_id()

    print("="*40)
    print("         RINCIAN PEMBELIAN")
    print("="*40)
    print(f"{'id pesanan' :20}: {generate_order_id}")
    print(f"{'nama pelangan' :20}: {nama_pelangan}")
    print(f"{'nama produk' :20}: {nama_produk}")
    print(f"{'harga asli' :20}: Rp {harga_asli:,.2f}")
    print(f"{'diskon' :20}: Rp {diskon:,.2f}")
    print(f"{'pajak' :20}: Rp {hitung_pajak(harga_asli - diskon, psersentase_pajak):,.2f}")
    print("-"*40)
    print(f"{'total belanja':20}: Rp {total:,.2f}")
    print("="*40)

if __name__ == "__main__":
        main()

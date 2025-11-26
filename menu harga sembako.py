# Program Python: Sistem Harga Jualan Pasar

# Daftar barang dan harga per satuan
barang_pasar = {
    "Beras (1 kg)": 15000,
    "Gula (1 kg)": 14000,
    "Minyak Goreng (1 L)": 13000,
    "Telur (1 kg)": 26000,
    "Cabai Merah (1 kg)": 55000,
    "Tomat (1 kg)": 8000,
    "Ayam Potong (1 kg)": 35000,
    "Kentang (1 kg)": 10000,
    "Bawang Merah (1 kg)": 40000,
    "Bawang Putih (1 kg)": 38000
}

print("=== SISTEM HARGA JUALAN PASAR ===")
print("Daftar Barang dan Harga:")
for barang, harga in barang_pasar.items():
    print(f"- {barang}: Rp{harga}")

keranjang = []
total = 0

while True:
    pilihan = input("\nMasukkan nama barang yang ingin dibeli (atau ketik 'selesai'): ")
    if pilihan.lower() == "selesai":
        break
    elif pilihan in barang_pasar:
        jumlah = int(input("Masukkan jumlah (kg/satuan): "))
        subtotal = barang_pasar[pilihan] * jumlah
        keranjang.append((pilihan, jumlah, subtotal))
        total += subtotal
        print(f"Ditambahkan: {jumlah} x {pilihan} = Rp{subtotal}")
    else:
        print("Barang tidak ditemukan. Silakan pilih barang lain.")

print("\n=== STRUK PEMBELIAN PASAR ===")
for item, qty, subtotal in keranjang:
    print(f"- {item} ({qty}): Rp{subtotal}")
print(f"Total Bayar: Rp{total}")
print("Terima kasih telah berbelanja!")
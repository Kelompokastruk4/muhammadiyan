# Program Python Sederhana: Sistem Menu Warteg

menu = {
    "Nasi": 5000,
    "Ayam Goreng": 12000,
    "Ikan Goreng": 10000,
    "Tahu": 2000,
    "Tempe": 2000,
    "Sayur Lodeh": 5000,
    "Sayur Asem": 5000,
    "Telur Balado": 6000,
    "Sambal": 1000
}

print("=== Selamat Datang di Warteg AI ===")
print("Menu Hari Ini:")
for item, harga in menu.items():
    print(f"- {item}: Rp{harga}")

pesanan = []
total = 0

while True:
    pilihan = input("\nMasukkan nama makanan (atau ketik 'selesai' untuk selesai): ")
    if pilihan.lower() == "selesai":
        break
    elif pilihan in menu:
        pesanan.append(pilihan)
        total += menu[pilihan]
        print(f"{pilihan} ditambahkan. Subtotal: Rp{total}")
    else:
        print("Menu tidak tersedia. Silakan pilih menu lain.")

print("\n=== Struk Pembelian ===")
for item in pesanan:
    print(f"- {item}: Rp{menu[item]}")
print(f"Total Bayar: Rp{total}")
print("Terima kasih sudah makan di Warteg AI!")

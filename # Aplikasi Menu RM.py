# Aplikasi Menu RM. Sari Bungo Minang
# Dibuat dengan Python

def tampilkan_menu():
    print("=" * 40)
    print("     RM. PADANG WARJO")
    print("          Masakan Padang")
    print("=" * 40)
    print("Daftar Menu:")
    menu = {
        "Nasi Sayur": 6000,
        "Nasi Perkedel": 9000,
        "Nasi Telur": 10000,
        "Nasi Amplak": 10000,
        "Nasi Ayam Goreng": 10000,
        "Nasi Ayam Balado/Bakar/Gulai": 12000,
        "Nasi Lele": 13000,
        "Nasi Nila": 13000,
        "Nasi Babat": 14000,
        "Nasi Tuna": 14000,
        "Nasi Kembung": 15000,
        "Nasi Rendang": 15000,
        "Nasi Udang": 15000,
        "Nasi Cincang": 18000,
        "Nasi Kikil": 25000,
        "Nasi Kepala Kakap": 35000
    }

    for i, (nama, harga) in enumerate(menu.items(), 1):
        print(f"{i}. {nama:30} Rp{harga:,}")

    return menu


def pesan_makanan(menu):
    pesanan = []
    total = 0
    while True:
        pilihan = input("\nMasukkan nama menu yang ingin dipesan (atau ketik 'selesai' untuk selesai): ").title()
        if pilihan.lower() == "selesai":
            break
        elif pilihan in menu:
            jumlah = int(input(f"Berapa porsi {pilihan}? "))
            subtotal = menu[pilihan] * jumlah
            pesanan.append((pilihan, jumlah, subtotal))
            total += subtotal
            print(f"{pilihan} x{jumlah} ditambahkan ke pesanan.")
        else:
            print("Menu tidak ditemukan. Silakan coba lagi.")

    print("\n--- Struk Pesanan ---")
    for item, jumlah, subtotal in pesanan:
        print(f"{item:30} x{jumlah} = Rp{subtotal:,}")
    print(f"\nTotal Bayar: Rp{total:,}")
    print("===============================")
    print("Terima kasih telah memesan di RM. PADANG WARJO!")


if __name__ == "__main__":
    daftar_menu = tampilkan_menu()
    pesan_makanan(daftar_menu)

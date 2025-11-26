# Aplikasi Menu RM. Sari Bungo Minang menggunakan match-case (mirip switch)
# Pastikan Python kamu versi 3.10 atau lebih baru

def tampilkan_menu():
    print("=" * 40)
    print("     RM. BAROKAH")
    print("          Masakan Padang")
    print("=" * 40)
    print("""
1. Nasi Sayur              Rp6.000
2. Nasi Perkedel           Rp9.000
3. Nasi Telur              Rp10.000
4. Nasi Amplak             Rp10.000
5. Nasi Ayam Goreng        Rp10.000
6. Nasi Ayam Balado/Bakar/Gulai Rp12.000
7. Nasi Lele               Rp13.000
8. Nasi Nila               Rp13.000
9. Nasi Babat              Rp14.000
10. Nasi Tuna              Rp14.000
11. Nasi Kembung           Rp15.000
12. Nasi Rendang           Rp15.000
13. Nasi Udang             Rp15.000
14. Nasi Cincang           Rp18.000
15. Nasi Kikil             Rp25.000
16. Nasi Kepala Kakap      Rp35.000
0. total
""")


def hitung_harga(pilihan):
    match pilihan:
        case 1: return "Nasi Sayur", 6000
        case 2: return "Nasi Perkedel", 9000
        case 3: return "Nasi Telur", 10000
        case 4: return "Nasi Amplak", 10000
        case 5: return "Nasi Ayam Goreng", 10000
        case 6: return "Nasi Ayam Balado/Bakar/Gulai", 12000
        case 7: return "Nasi Lele", 13000
        case 8: return "Nasi Nila", 13000
        case 9: return "Nasi Babat", 14000
        case 10: return "Nasi Tuna", 14000
        case 11: return "Nasi Kembung", 15000
        case 12: return "Nasi Rendang", 15000
        case 13: return "Nasi Udang", 15000
        case 14: return "Nasi Cincang", 18000
        case 15: return "Nasi Kikil", 25000
        case 16: return "Nasi Kepala Kakap", 35000
        case _: return None,0


def main():
    total = 0
    pesanan = []

    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Masukkan nomor menu: "))
        except ValueError:
            print("Masukkan angka yang benar!\n")
            continue

        if pilihan == 0:
            break

        nama, harga = hitung_harga(pilihan)
        if nama:
            jumlah = int(input(f"Berapa porsi {nama}? "))
            subtotal = harga * jumlah
            pesanan.append((nama, jumlah, subtotal))
            total += subtotal
            print(f"{nama} x{jumlah} berhasil ditambahkan.\n")
        else:
            print("Nomor menu tidak tersedia.\n")

    print("\n=== STRUK PEMBAYARAN ===")
    for item, jml, sub in pesanan:
        print(f"{item:30} x{jml} = Rp{sub:,}")
    print(f"TOTAL BAYAR: Rp{total:,}")
    print("Terima kasih telah makan di RM. BAROKAH!")


if __name__ == "__main__":
    main()

  # Inisialisasi data barang
  barang = {
      "Pensil": [5000, 10],
      "Buku": [7500, 5],
      "Penggaris": [12000, 4],
      "Pulpen": [5500, 10],
      "Buku Gambar": [4000, 7],
      "Pensil Warna": [15000, 5]
  }

  # a. Menampilkan Nama Barang, Harga Satuan, dan Stok
  print("Daftar Barang:")
  for nama, info in barang.items():
      harga, stok = info
      print(f"{nama}: Harga Rp {harga}, Stok {stok}")

  # b. Input nama barang dan jumlah
  nama_barang = input("Masukkan nama barang yang ingin dibeli: ")
  if nama_barang not in barang:
      print("Barang tidak ditemukan.")
      exit()

  jumlah_beli = int(input("Masukkan jumlah barang yang ingin dibeli: "))
  harga, stok = barang[nama_barang]

  # c. Hitung total harga
  if jumlah_beli > stok:
      print("Stok tidak cukup.")
      exit()

  total_harga = harga * jumlah_beli
  print(f"Total harga: Rp {total_harga}")

  # d. Kurangi stok
  barang[nama_barang][1] -= jumlah_beli

  # e. Cek stok habis
  if barang[nama_barang][1] == 0:
      print("Stok barang habis.")
      
def bubble_sort(arr):
    n = len(arr)
    # Loop untuk setiap elemen dalam list
    for i in range(n):
        # Loop untuk membandingkan elemen berdekatan
        for j in range(0, n - i - 1):
            # Tukar jika elemen sekarang lebih besar dari elemen berikutnya
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
print("Data sebelum diurutkan:", data)

bubble_sort(data)
print("Data setelah diurutkan:", data)
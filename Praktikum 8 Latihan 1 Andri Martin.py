def penjumlahan(angka = 0, j = 0, a =1):
    if ( j <= 0):
        return 0
    else:
        angka = int(input("Masukan bilangan ke-" + str(a) + ":"))
        if (j == 1):
            return angka        
        else:
            a +=1
            return angka + penjumlahan (angka, j-1, a)
jumlah = int(input("Masukan Jumlah: "))
nilai = penjumlahan(j = jumlah)
print("Hasil dari penjumlahan adalah: " + str(nilai))
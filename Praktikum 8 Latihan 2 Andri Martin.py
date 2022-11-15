def nilai():
    print()
    print("Ini merupakan program pemangkatan negatif dan positif, Tekan enter untuk berhenti")
    a = input("Masukkan Angka: ")
    if a == '':
        print("Terima Kasih telah menggunakan Program ini. Program selesai")
        return 0
    p = input("Masukkan Pangkatnya: ")
    hasil = int(a)**int(p)
    print("Hasilnya adalah: ",hasil)
    nilai()

nilai()
pg = []

anggota = []

while True:
    print("Selamat Datang!")
    print("1.Menambah data")
    print("2.Menampilkan data")
    print("3.Keluar")
    
    choice = int(input("Silahkan masukkan pilihan anda: "))
    
    if choice == 1:
        msnp = input("Masukkan Nama Pelanggan: ")
        pg.append(msnp)
        msjm = input("Masukkan Jenis Member: ")
        anggota.append(msjm)
        print ("Data Sudah Berhasil Ditambahkan!\n\n")
        
    elif choice == 2:
        print("----------------------")
        print("Pg\tanggota")
        print(pg[0],"\t\t",anggota[0])
        print()
        
else:
    print("SIE SIE")
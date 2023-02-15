print("===============MAKANAN===============")
print("1. Telur bakar           : Rp 7.000 ")
print("2. Lele Terbang Mas Bhe  : Rp 10.000 ")
print("3. Es Coklat Lempu       : Rp 5.000 ")
print("4. Es Doger Langensari   : Rp 13.000")
print("==============PESANAN===============")
listmakan=str(input(" Masukkan Nomor Yang Ingin dipesan = "))
jumlahyangdipesan=int(input("Jumlah yang dibeli = "))
if listmakan == "1":
    namamakan= "Telur bakar"
    hargabayar=(7000*jumlahyangdipesan)
    if jumlahyangdipesan >= 5:
        totalyangharusdibayar=int(hargabayar)
    else:
        totalyangharusdibayar=int(hargabayar)
elif listmakan == "2":
    namamakan= "Lele Terbang Mas Bhe"
    hargabayar=(10000*jumlahyangdipesan)
    if jumlahyangdipesan >= 5:
        totalyangharusdibayar=int(hargabayar)
    else:
        totalyangharusdibayar=int(hargabayar)
elif listmakan == "3":
    namamakan= "Es Coklat"
    hargabayar=(5000*jumlahyangdipesan)
    totalyangharusdibayar=int(hargabayar)
elif listmakan == "4":
    namamakan= "Es Doger"
    hargabayar=(13000*jumlahyangdipesan)
    totalyangharusdibayar=int(hargabayar)
   
else:
    Menu=input(" Maaf,Menu yang anda minta tidak tersedia di restoran UKDW ")

print("===============TOTAL==============")
print(" Makan :",namamakan)
print("Jumlah Yang Dipesan :",jumlahyangdipesan)
print("Harga Yang Harus Dibayar :",hargabayar)
print(" Jumlah total biaya yang harus dibayar adalah :",totalyangharusdibayar)


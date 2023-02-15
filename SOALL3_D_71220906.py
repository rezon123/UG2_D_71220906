tootalll1 = int(input("Berapa harga barang H&M: "))
tootalll2 = int(input("Berapa harga barang fendi: "))
tootalll3 = int(input("Berapa harga barang LV: "))
tootalll4 = int(input("Berapa harga barang Dior: "))
stl_diskon1 = tootalll1
stl_diskon2 = tootalll2
stl_diskon3 = tootalll3
stl_diskon4 = tootalll4
if tootalll1 < 2000000:
    stl_diskon1 = tootalll * (0.1/100)
else
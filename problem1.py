iter = int(input("Masukkan banyak barang : "))
harga=[]
for x in range(1,iter+1):
    h = int(input("Masukkan harga awal barang ke-{} : ".format(x)))
    harga.append(h);
for x in range(1,iter+1):
    d = int(input("diskon {} : ".format(x)))
    harga[x-1]=(int(harga[x-1]*(d/100)))

#karna ga bole pake max() pake cara panjang
maks = 0
print(harga)
for item in harga:
    if item>maks:
        maks = item
print("Barang {} memiliki diskon paling besar yaitu {}".format(harga.index(maks)+1,maks))       
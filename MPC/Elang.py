angka = list(map(int,input().split('+')))
angka = sorted(angka)
hasil = ""
for i in  range(0,len(angka)):
    hasil += str(angka[i])
    if(i<len(angka)-1):
        hasil+='+'
print(hasil)
arr = [2, 3, 4, 2, 2, 6, 8]
cari = int(input())
ketemu = 0
lokasi = ''
for i in range(len(arr)):
    if(cari == arr[i]):
        ketemu += 1
        lokasi += str(i)+' '

if(ketemu > 0): #jika ditemukan
    print(cari, "ditemukan sebanyak %d di indeks ke %s" %(ketemu, lokasi))
else:
    print(cari, "tidak ditemukan pada array")
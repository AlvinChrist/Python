N = int(input("Masukkan Nilai N : "))
K = int(input("Masukkan Nilai K : "))
hasil = 0
for x in range(1,N+1):
    y = int(input("Masukkan digit ke {}: ".format(x)))
    hasil += y*K**(N-x)
print("Bilangan dalam basis 10 adalah {}".format(hasil))
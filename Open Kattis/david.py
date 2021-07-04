x=0
y=3
while x<=0 and y>0:
    x = int(input("Masukkan Angka : "))
    if(x>0):
        print("*"*x)
        break
    else:
        y-=1
        print("Invalid, anda punya "+str(y)+" kesempatan lagi")
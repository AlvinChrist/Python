X = int(input("Masukkan X: "))
if(0<x<10):
    print("Bilangan cantik terkecil yang habis dibagi {} adalah {}".format(X,X))
else:
    for key in keylist:
        if X%3==0:
            print("Bilangan cantik terkecil yang habis dibagi {} adalah {}".format(X,X*37))
        elif X%37==0:
            print("Bilangan cantik terkecil yang habis dibagi {} adalah {}".format(X,str(int(X/37))*3)
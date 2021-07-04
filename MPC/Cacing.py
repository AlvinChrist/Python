arr = []
a = int(input())
arr.append(a)
b = int(input())
arr.append(b)
c = int(input())
arr.append(c)
if 1 in arr:
    if a==1:
        if(b==1):
            if(c==1):
                print(a+b+c)
            else:
                print((a+b)*c)    
        elif c==1:
            print(a+b+c)
        else:
            print((a+b)*c)
    elif b==1:
        if(a<c):
            print((a+b)*c)
        else:
            print(a*(b+c))
    elif c==1:
        print(a*(b+c))
else:
    print((int(a*b*c)))
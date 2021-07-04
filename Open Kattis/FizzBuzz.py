x = list(map(int,input().split()))
for y in range(1,x[2]+1):
    shout = y
    if(y%x[0]==0):
        shout="Fizz"
    if(y%x[1]==0):
        if(shout!=y):
            shout+="Buzz"
        else:
            shout="Buzz"
    print(shout)
    
x = list(map(int,input().split()))
for i in range(0,x[1]):
    if(x[0]%10==0):
        x[0]=int(x[0]/10)
    else:
        x[0]-=1
print(x[0])        
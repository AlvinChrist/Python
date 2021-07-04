x = list(map(int,input().split()))
res = 4
if(x[0]-x[1]>x[1]):
    res*=x[0]-x[1]
else:
    res*=x[1]
if(x[0]-x[2]>x[2]):
    res*=x[0]-x[2]
else:
    res*=x[2]
print(res)